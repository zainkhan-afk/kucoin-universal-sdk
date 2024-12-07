import os
import unittest
import uuid

from kucoin_universal_sdk.api.client import DefaultClient
from kucoin_universal_sdk.extension.interceptor.logging import LoggingInterceptor
from kucoin_universal_sdk.generate.margin.order.model_add_order_req import AddOrderReqBuilder, AddOrderReq
from kucoin_universal_sdk.generate.margin.order.model_add_order_test_req import AddOrderTestReqBuilder, AddOrderTestReq
from kucoin_universal_sdk.generate.margin.order.model_add_order_test_v1_req import AddOrderTestV1ReqBuilder, \
    AddOrderTestV1Req
from kucoin_universal_sdk.generate.margin.order.model_add_order_v1_req import AddOrderV1ReqBuilder, AddOrderV1Req
from kucoin_universal_sdk.generate.margin.order.model_cancel_all_orders_by_symbol_req import \
    CancelAllOrdersBySymbolReqBuilder, CancelAllOrdersBySymbolReq
from kucoin_universal_sdk.generate.margin.order.model_cancel_order_by_client_oid_req import \
    CancelOrderByClientOidReqBuilder
from kucoin_universal_sdk.generate.margin.order.model_cancel_order_by_order_id_req import CancelOrderByOrderIdReqBuilder
from kucoin_universal_sdk.generate.margin.order.model_get_closed_orders_req import GetClosedOrdersReqBuilder, \
    GetClosedOrdersReq
from kucoin_universal_sdk.generate.margin.order.model_get_open_orders_req import GetOpenOrdersReqBuilder, \
    GetOpenOrdersReq
from kucoin_universal_sdk.generate.margin.order.model_get_order_by_client_oid_req import GetOrderByClientOidReqBuilder
from kucoin_universal_sdk.generate.margin.order.model_get_order_by_order_id_req import GetOrderByOrderIdReqBuilder
from kucoin_universal_sdk.generate.margin.order.model_get_symbols_with_open_order_req import \
    GetSymbolsWithOpenOrderReqBuilder, GetSymbolsWithOpenOrderReq
from kucoin_universal_sdk.generate.margin.order.model_get_trade_history_req import GetTradeHistoryReqBuilder, \
    GetTradeHistoryReq
from kucoin_universal_sdk.generate.margin.risklimit.model_get_margin_risk_limit_req import GetMarginRiskLimitReqBuilder
from kucoin_universal_sdk.model.client_option import ClientOptionBuilder
from kucoin_universal_sdk.model.constants import GLOBAL_API_ENDPOINT, GLOBAL_BROKER_API_ENDPOINT, \
    GLOBAL_FUTURES_API_ENDPOINT
from kucoin_universal_sdk.model.transport_option import TransportOptionBuilder


class MarginApiTest(unittest.TestCase):
    def setUp(self):
        key = os.getenv("API_KEY")
        secret = os.getenv("API_SECRET")
        passphrase = os.getenv("API_PASSPHRASE")

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
            .set_transport_option(http_transport_option)
            .build()
        )

        # create API client
        client = DefaultClient(client_option)
        kucoin_rest_api = client.rest_service()
        self.api = kucoin_rest_api.get_margin_service().get_risk_limit_api()

    def test_get_margin_risk_limit_req(self):
        """
            get_margin_risk_limit
            Get Margin Risk Limit
            /api/v3/margin/currencies
        """

        builder = GetMarginRiskLimitReqBuilder()
        builder.set_is_isolated(False).set_currency("BTC")
        req = builder.build()
        try:
            resp = self.api.get_margin_risk_limit(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e