import os
import os
import threading
import unittest
import logging
from time import sleep

from kucoin_universal_sdk.api.client import DefaultClient
from kucoin_universal_sdk.extension.interceptor.logging import LoggingInterceptor
from kucoin_universal_sdk.model.client_option import ClientOptionBuilder
from kucoin_universal_sdk.model.constants import GLOBAL_API_ENDPOINT, GLOBAL_FUTURES_API_ENDPOINT, \
    GLOBAL_BROKER_API_ENDPOINT
from kucoin_universal_sdk.model.transport_option import TransportOptionBuilder
from kucoin_universal_sdk.model.websocket_option import WebSocketClientOptionBuilder

logging.basicConfig(level=logging.DEBUG)

class ReliabilityTest(unittest.TestCase):

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

    def test_resubscribe(self):

        def print_cb(topic, subject, data):
            print(data.to_json())

        sub1 = self.api.ticker(["ETH-USDT", "BTC-USDT"], print_cb)
        sleep(1)
        try:
            sub2 = self.api.ticker(["ETH-USDT", "BTC-USDT"], print_cb)
        except Exception as e:
            self.assertIsNotNone(e)
            print(e.__str__())

    def test_resubscribe_2(self):
        doge = threading.Event()
        btc = threading.Event()
        eth = threading.Event()

        def print_cb(topic, subject, data):
            if topic == "/market/ticker:ETH-USDT":
                eth.set()
            if topic == "/market/ticker:BTC-USDT":
                btc.set()
            if topic == "/market/ticker:DOGE-USDT":
                doge.set()
            print(data.to_json())

        sub1 = self.api.ticker(["ETH-USDT", "BTC-USDT"], print_cb)
        sleep(1)
        sub2 = self.api.ticker(["DOGE-USDT", "BTC-USDT"], print_cb)
        sleep(1)

        self.assertTrue(doge.is_set())
        self.assertTrue(btc.is_set())
        self.assertTrue(eth.is_set())

        self.api.unsubscribe(sub2)
        sleep(1)
        doge.clear()
        sleep(1)
        self.assertTrue(not doge.is_set())

    def test_concurrent_resubscribe(self):
        t1 = threading.Event()
        t2 = threading.Event()
        o1 = threading.Event()
        o2 = threading.Event()
        o3 = threading.Event()

        def print_cb(topic, subject, data):
            if subject == 'trade.ticker':
                t1.set()
            if subject == 'trade.l3match':
                t2.set()
            if subject == 'level1':
                o1.set()
            if subject == 'level2':
                o2.set()
            if subject == 'trade.l2update':
                o3.set()
            print(data.to_json())

        self.api.ticker(["ETH-USDT", "BTC-USDT"], print_cb)
        self.api.trade(["ETH-USDT", "BTC-USDT"], print_cb)
        self.api.orderbook_level1(["ETH-USDT", "BTC-USDT"], print_cb)
        self.api.orderbook_level5(["ETH-USDT", "BTC-USDT"], print_cb)
        self.api.orderbook_level50(["ETH-USDT", "BTC-USDT"], print_cb)

        sleep(10)

        self.assertTrue(t1.is_set())
        self.assertTrue(t2.is_set())
        self.assertTrue(o1.is_set())
        self.assertTrue(o2.is_set())
        self.assertTrue(o3.is_set())

    def test_reconnect(self):
        def print_cb(topic, subject, data):
            print(data.to_json())

        self.api.ticker(["ETH-USDT", "BTC-USDT"], print_cb)

        sleep(100)

    def test_read_buffer_with_event(self):
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

        def event_cb(type, data, msg):
            print(f"event: {str(type)}, {data}, {msg}")
            sleep(1)

        websocket_client_option = WebSocketClientOptionBuilder().with_event_callback(event_cb).with_read_message_buffer(
            1).build()

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
        client = DefaultClient(client_option)
        kucoin_ws_api = client.ws_service()
        api = kucoin_ws_api.new_spot_public_ws()
        api.start()

        def print_cb(topic, subject, data):
            print(data.to_json())
            sleep(2)

        api.orderbook_level50(["ETH-USDT", "BTC-USDT"], print_cb)

        sleep(10)
        print('done!')
