import os
import os
import unittest

from kucoin_universal_sdk.api.client import DefaultClient
from kucoin_universal_sdk.extension.interceptor.logging import LoggingInterceptor
from kucoin_universal_sdk.generate.account.account.model_get_spot_ledger_req import GetSpotLedgerReqBuilder
from kucoin_universal_sdk.model.client_option import ClientOptionBuilder
from kucoin_universal_sdk.model.constants import GLOBAL_API_ENDPOINT, GLOBAL_FUTURES_API_ENDPOINT, \
    GLOBAL_BROKER_API_ENDPOINT
from kucoin_universal_sdk.model.transport_option import TransportOptionBuilder


class ReliabilityTest(unittest.TestCase):
    def test_timeout_retry(self):
        key = os.getenv("API_KEY")
        secret = os.getenv("API_SECRET")
        passphrase = os.getenv("API_PASSPHRASE")

        # create http transport option
        http_transport_option = (
            TransportOptionBuilder()
            .set_interceptors([LoggingInterceptor()])
            .set_max_connection_per_pool(2)
            .set_max_pool_size(2)
            .set_max_retries(2)
            .set_connect_timeout(0.1)
            .set_read_timeout(0.01)
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
        api = kucoin_rest_api.get_account_service().get_account_api()
        try:
            resp = api.get_spot_ledger(GetSpotLedgerReqBuilder().build())
        except Exception as e:
            self.assertIsNotNone(e)
            print(e.__str__())

    def test_proxy(self):
        key = os.getenv("API_KEY")
        secret = os.getenv("API_SECRET")
        passphrase = os.getenv("API_PASSPHRASE")

        # create http transport option
        http_transport_option = (
            TransportOptionBuilder()
            .set_interceptors([LoggingInterceptor()])
            .set_max_connection_per_pool(2)
            .set_max_pool_size(2)
            .set_max_retries(2)
            .set_connect_timeout(0.1)
            .set_read_timeout(0.01)
            .set_proxy(({'http': '192.168.1.1', 'https': '192.168.1.1'}))
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
        api = kucoin_rest_api.get_account_service().get_account_api()
        try:
            resp = api.get_spot_ledger(GetSpotLedgerReqBuilder().build())
        except Exception as e:
            self.assertIsNotNone(e)
            print(e.__str__())
