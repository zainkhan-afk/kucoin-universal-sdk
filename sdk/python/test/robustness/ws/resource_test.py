import gc
import os
import tracemalloc
import unittest
from time import sleep
import logging
import psutil

from kucoin_universal_sdk.api.client import DefaultClient
from kucoin_universal_sdk.extension.interceptor.logging import LoggingInterceptor
from kucoin_universal_sdk.model.client_option import ClientOptionBuilder
from kucoin_universal_sdk.model.constants import GLOBAL_API_ENDPOINT, GLOBAL_FUTURES_API_ENDPOINT, \
    GLOBAL_BROKER_API_ENDPOINT
from kucoin_universal_sdk.model.transport_option import TransportOptionBuilder
from kucoin_universal_sdk.model.websocket_option import WebSocketClientOptionBuilder

logging.basicConfig(level=logging.DEBUG)

class ResourceTest(unittest.TestCase):
    def setUp(self):
        key = os.getenv("API_KEY")
        secret = os.getenv("API_SECRET")
        passphrase = os.getenv("API_PASSPHRASE")

        # create http transport option
        http_transport_option = (
            TransportOptionBuilder()
            .set_interceptors([LoggingInterceptor()])
            .set_max_connection_per_pool(2)
            .set_max_pool_size(2)
            .build()
        )

        websocket_client_option = WebSocketClientOptionBuilder().build()

        # create client option
        client_option = (
            ClientOptionBuilder()
            .set_key(key)
            .set_secret(secret)
            .set_passphrase(passphrase)
            .set_spot_endpoint(GLOBAL_API_ENDPOINT)
            .set_futures_endpoint(GLOBAL_FUTURES_API_ENDPOINT)
            .set_broker_endpoint(GLOBAL_BROKER_API_ENDPOINT)
            .set_transport_option(http_transport_option)
            .set_websocket_client_option(websocket_client_option)
            .build()
        )

        # create API client
        client = DefaultClient(client_option)
        self.kucoin_ws_api = client.ws_service()
        self.api = self.kucoin_ws_api.new_spot_public_ws()
        self.api.start()

    def tearDown(self):
        self.api.stop()

    def get_fd_size(self):
        process = psutil.Process(os.getpid())
        return process.num_fds()

    def get_tcp_connection_size(self):
        pid = psutil.Process().pid
        print(f"Current PID: {pid}")
        connections = psutil.Process(pid).net_connections(kind="tcp")
        if connections:
            print("TCP connections for the current process:")
            for conn in connections:
                laddr = f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else "N/A"
                raddr = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "N/A"
                print(f"Status: {conn.status}, Local: {laddr}, Remote: {raddr}")
            return len(connections)
        else:
            print("No active TCP connections for the current process.")

    def test_resource_leak(self):
        tracemalloc.start()
        start_fd = self.get_fd_size()
        current, peak = tracemalloc.get_traced_memory()
        print(f"Current memory usage: {current / 1024:.2f} KB; Peak: {peak / 1024:.2f} KB")

        cnt = 0

        def print_cb(topic, subject, data):
            data.to_json()
            nonlocal cnt
            cnt = cnt + 1
            pass

        self.api.all_tickers(print_cb)

        for i in range(30):
            current, peak = tracemalloc.get_traced_memory()
            print(f"Current memory usage: {current / 1024:.2f} KB; Peak: {peak / 1024:.2f} KB")
            sleep(1)
            gc.collect()

        end_fd = self.get_fd_size()
        print(f"done, start_fd:{start_fd}, end_fd:{end_fd}, total data:{cnt}")

        conn_size = self.get_tcp_connection_size()
        print(f"conn size: {conn_size}")
        self.assertTrue(conn_size <= 2)

        current, peak = tracemalloc.get_traced_memory()
        print(f"Current memory usage: {current / 1024:.2f} KB; Peak: {peak / 1024:.2f} KB")
        tracemalloc.stop()

    def test_tcp_connection(self):
        conn_size_start = self.get_tcp_connection_size()

        ws1 = self.kucoin_ws_api.new_spot_public_ws()
        ws2 = self.kucoin_ws_api.new_spot_public_ws()
        ws3 = self.kucoin_ws_api.new_futures_public_ws()
        ws4 = self.kucoin_ws_api.new_futures_public_ws()

        ws1.start()
        ws2.start()
        ws3.start()
        ws4.start()

        sleep(1)

        ws1.stop()
        ws2.stop()
        ws3.stop()
        ws4.stop()

        sleep(2)
        conn_size_end = self.get_tcp_connection_size()

        print(f"{conn_size_start} {conn_size_end}")
        self.assertEqual(conn_size_start, conn_size_end)
