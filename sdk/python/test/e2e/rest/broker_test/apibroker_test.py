import os
import unittest

from kucoin_universal_sdk.api.client import DefaultClient
from kucoin_universal_sdk.extension.interceptor.logging import LoggingInterceptor
from kucoin_universal_sdk.generate.broker.apibroker.model_get_rebase_req import GetRebaseReqBuilder, GetRebaseReq
from kucoin_universal_sdk.model.client_option import ClientOptionBuilder
from kucoin_universal_sdk.model.constants import GLOBAL_API_ENDPOINT, GLOBAL_BROKER_API_ENDPOINT, \
    GLOBAL_FUTURES_API_ENDPOINT
from kucoin_universal_sdk.model.transport_option import TransportOptionBuilder


class BrokerApiTest(unittest.TestCase):
    def setUp(self):
        key = os.getenv("API_KEY")
        secret = os.getenv("API_SECRET")
        passphrase = os.getenv("API_PASSPHRASE")
        broker_name = os.getenv("BROKER_NAME")
        broker_key = os.getenv("BROKER_KEY")
        broker_partner = os.getenv("BROKER_PARTNER")

        # create http transport option
        http_transport_option = (
            TransportOptionBuilder()
            .set_interceptors([LoggingInterceptor()])
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
            .set_broker_name(broker_name)
            .set_broker_partner(broker_partner)
            .set_broker_key(broker_key)
            .set_transport_option(http_transport_option)
            .build()
        )

        # create API client
        client = DefaultClient(client_option)
        kucoin_rest_api = client.rest_service()
        self.api = kucoin_rest_api.get_broker_service().get_api_broker_api()

    # TODO no permission
    def test_get_rebase_req(self):
        """
            get_rebase
            Get Broker Rebate
            /api/v1/broker/api/rebase/download
        """

        builder = GetRebaseReqBuilder()
        builder.set_begin("20240610").set_end("20241010").set_trade_type(GetRebaseReq.TradeTypeEnum.T_1)
        req = builder.build()
        try:
            resp = self.api.get_rebase(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e
