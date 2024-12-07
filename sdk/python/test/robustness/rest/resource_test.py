import asyncio
import gc
import os
import tracemalloc
import unittest
from time import sleep

import psutil

from kucoin_universal_sdk.api.client import DefaultClient
from kucoin_universal_sdk.extension.interceptor.logging import LoggingInterceptor
from kucoin_universal_sdk.generate.account.account.model_get_futures_account_req import GetFuturesAccountReqBuilder
from kucoin_universal_sdk.generate.account.account.model_get_futures_ledger_req import GetFuturesLedgerReqBuilder
from kucoin_universal_sdk.generate.account.account.model_get_spot_ledger_req import GetSpotLedgerReqBuilder
from kucoin_universal_sdk.model.client_option import ClientOptionBuilder
from kucoin_universal_sdk.model.constants import GLOBAL_API_ENDPOINT, GLOBAL_FUTURES_API_ENDPOINT, \
    GLOBAL_BROKER_API_ENDPOINT
from kucoin_universal_sdk.model.transport_option import TransportOptionBuilder


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
            .build()
        )

        # create API client
        client = DefaultClient(client_option)
        kucoin_rest_api = client.rest_service()
        self.api = kucoin_rest_api.get_account_service().get_account_api()

    def spot_func_sync(self):
        resp = self.api.get_spot_ledger(GetSpotLedgerReqBuilder().build())
        assert len(resp.items) > 0
        print("spot_func_1 ok")

    async def spot_func_1(self):
        resp = await asyncio.to_thread(self.api.get_spot_ledger, GetSpotLedgerReqBuilder().build())
        assert len(resp.items) > 0
        print("spot_func_1 ok")

    async def spot_func_2(self):
        resp = await asyncio.to_thread(self.api.get_apikey_info)
        assert len(resp.api_key) > 0
        print("spot_func_2 ok")

    async def futures_func1(self):
        resp = await asyncio.to_thread(self.api.get_futures_ledger, GetFuturesLedgerReqBuilder().build())
        print("futures_func_1 ok")

    async def futures_func2(self):
        resp = await asyncio.to_thread(self.api.get_futures_account,
                                       GetFuturesAccountReqBuilder().set_currency('XBT').build())
        assert resp.account_equity is not None
        print("futures_func_2 ok")

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

    def test_concurrent_requests(self):
        async def _run():
            tasks = []
            for _ in range(10):
                tasks.append(self.spot_func_1())
                tasks.append(self.spot_func_2())
                tasks.append(self.futures_func1())
                tasks.append(self.futures_func2())

            await asyncio.gather(*tasks)

        asyncio.run(_run())

    def test_resource_leak(self):
        tracemalloc.start()
        start_fd = self.get_fd_size()
        current, peak = tracemalloc.get_traced_memory()
        print(f"Current memory usage: {current / 1024:.2f} KB; Peak: {peak / 1024:.2f} KB")
        for _ in range(10):
            async def _run():
                tasks = []
                for _ in range(6):
                    tasks.append(self.spot_func_1())
                    tasks.append(self.spot_func_2())
                    tasks.append(self.futures_func1())
                    tasks.append(self.futures_func2())

                await asyncio.gather(*tasks)

            asyncio.run(_run())
            gc.collect()

            current, peak = tracemalloc.get_traced_memory()
            print(f"Current memory usage: {current / 1024:.2f} KB; Peak: {peak / 1024:.2f} KB")
            sleep(10)

        end_fd = self.get_fd_size()
        print(f"done, start_fd:{start_fd}, end_fd:{end_fd}")

        conn_size = self.get_tcp_connection_size()
        self.assertTrue(conn_size <= 4)

        current, peak = tracemalloc.get_traced_memory()
        print(f"Current memory usage: {current / 1024:.2f} KB; Peak: {peak / 1024:.2f} KB")
        tracemalloc.stop()
