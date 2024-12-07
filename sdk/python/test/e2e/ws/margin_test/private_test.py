import logging
import os
import threading
import unittest

from kucoin_universal_sdk.api.client import DefaultClient
from kucoin_universal_sdk.model.client_option import ClientOptionBuilder
from kucoin_universal_sdk.model.constants import GLOBAL_API_ENDPOINT, GLOBAL_FUTURES_API_ENDPOINT, \
    GLOBAL_BROKER_API_ENDPOINT
from kucoin_universal_sdk.model.websocket_option import WebSocketClientOptionBuilder

logging.basicConfig(level=logging.DEBUG)


class MarginPrivateWsTest(unittest.TestCase):
    def setUp(self):
        key = os.getenv("API_KEY")
        secret = os.getenv("API_SECRET")
        passphrase = os.getenv("API_PASSPHRASE")

        if not key or not secret or not passphrase:
            self.fail("Environment variables API_KEY, API_SECRET, and API_PASSPHRASE must be set.")

        def even_callback(event, msg, msg2=None):
            logging.info(f"Event: {event}, Msg1: {msg}, Msg2: {msg2 or 'Default value'}")

        # Create client option
        ws_client_option = WebSocketClientOptionBuilder().with_event_callback(even_callback).build()
        client_option = (
            ClientOptionBuilder()
            .set_key(key)
            .set_secret(secret)
            .set_passphrase(passphrase)
            .set_websocket_client_option(ws_client_option)
            .set_spot_endpoint(GLOBAL_API_ENDPOINT)
            .set_futures_endpoint(GLOBAL_FUTURES_API_ENDPOINT)
            .set_broker_endpoint(GLOBAL_BROKER_API_ENDPOINT)
            .build()
        )

        # Create WebSocket client
        client = DefaultClient(client_option)
        kucoin_ws_client = client.ws_service()
        self.api = kucoin_ws_client.new_margin_private_ws()
        self.api.start()

    def tearDown(self):
        self.api.stop()

    def _test_subscription(self, subscribe_method, *args):
        message_count = 0
        event = threading.Event()

        def callback(topic: str, subject: str, data):
            nonlocal message_count
            message_count += 1
            print(f"Received message {message_count} on topic: {topic}, subject: {subject}, data: {data.to_json()}")
            if message_count == 1:
                print("Received 1 messages. Unsubscribe...")
                event.set()

        subscription_id = subscribe_method(*args, callback)
        print(f"subscribe id {subscription_id}")
        try:
            event.wait()
        finally:
            self.api.unsubscribe(subscription_id)

    def test_private_cross_margin_position(self):
        self._test_subscription(self.api.cross_margin_position)

    def test_private_isolated_margin_position(self):
        self._test_subscription(self.api.isolated_margin_position, "DOGE-USDT")