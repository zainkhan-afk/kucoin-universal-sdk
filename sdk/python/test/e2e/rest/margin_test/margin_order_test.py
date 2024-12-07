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
        self.api = kucoin_rest_api.get_margin_service().get_order_api()

    def test_add_order_v1_req(self):
        """
            add_order_v1
            Add Order(V1)
            /api/v1/margin/order
        """

        builder = AddOrderV1ReqBuilder()
        builder.set_client_oid(uuid.uuid4().__str__()).set_side(AddOrderV1Req.SideEnum.BUY).set_symbol(
            "BTC-USDT").set_type(AddOrderV1Req.TypeEnum.LIMIT).set_price("10000").set_size("0.001").set_auto_repay(
            False).set_auto_borrow(False).set_margin_model(AddOrderV1Req.MarginModelEnum.ISOLATED)
        req = builder.build()
        try:
            resp = self.api.add_order_v1(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_add_order_test_v1_req(self):
        """
            add_order_test_v1
            Add Order Test(V1)
            /api/v1/margin/order/test
        """

        builder = AddOrderTestV1ReqBuilder()
        builder.set_client_oid(uuid.uuid4().__str__()).set_side(AddOrderTestV1Req.SideEnum.BUY).set_symbol(
            "BTC-USDT").set_type(AddOrderTestV1Req.TypeEnum.LIMIT).set_price("10000").set_size("0.001").set_auto_repay(
            False).set_auto_borrow(False).set_margin_model(AddOrderTestV1Req.MarginModelEnum.ISOLATED)
        req = builder.build()
        try:
            resp = self.api.add_order_test_v1(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_get_trade_history_req(self):
        """
            get_trade_history
            Get Trade History
            /api/v3/hf/margin/fills
        """

        builder = GetTradeHistoryReqBuilder()
        builder.set_symbol("DOGE-USDT").set_trade_type(GetTradeHistoryReq.TradeTypeEnum.MARGIN_TRADE)
        req = builder.build()
        try:
            resp = self.api.get_trade_history(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_get_symbols_with_open_order_req(self):
        """
            get_symbols_with_open_order
            Get Symbols With Open Order
            /api/v3/hf/margin/order/active/symbols
        """

        builder = GetSymbolsWithOpenOrderReqBuilder()
        builder.set_trade_type(GetSymbolsWithOpenOrderReq.TradeTypeEnum.MARGIN_ISOLATED_TRADE)
        req = builder.build()
        try:
            resp = self.api.get_symbols_with_open_order(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_add_order_req(self):
        """
            add_order
            Add Order
            /api/v3/hf/margin/order
        """

        builder = AddOrderReqBuilder()
        builder.set_client_oid(uuid.uuid4().__str__()).set_side(AddOrderReq.SideEnum.BUY).set_symbol(
            "BTC-USDT").set_type(AddOrderReq.TypeEnum.LIMIT).set_price("10000").set_size("0.001").set_auto_repay(
            False).set_auto_borrow(False).set_is_isolated(True)
        req = builder.build()
        try:
            resp = self.api.add_order(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_add_order_test_req(self):
        """
            add_order_test
            Add Order Test
            /api/v3/hf/margin/order/test
        """

        builder = AddOrderTestReqBuilder()
        builder.set_client_oid(uuid.uuid4().__str__()).set_side(AddOrderTestReq.SideEnum.BUY).set_symbol(
            "BTC-USDT").set_type(AddOrderTestReq.TypeEnum.LIMIT).set_price("10000").set_size("0.001").set_auto_repay(
            False).set_auto_borrow(False).set_is_isolated(True)
        req = builder.build()
        try:
            resp = self.api.add_order_test(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_get_open_orders_req(self):
        """
            get_open_orders
            Get Open Orders
            /api/v3/hf/margin/orders/active
        """

        builder = GetOpenOrdersReqBuilder()
        builder.set_symbol("BTC-USDT").set_trade_type(GetOpenOrdersReq.TradeTypeEnum.MARGIN_ISOLATED_TRADE)
        req = builder.build()
        try:
            resp = self.api.get_open_orders(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_cancel_order_by_client_oid_req(self):
        """
            cancel_order_by_client_oid
            Cancel Order By ClientOid
            /api/v3/hf/margin/orders/client-order/{clientOid}
        """

        builder = CancelOrderByClientOidReqBuilder()
        builder.set_client_oid("f024fabd-2b82-49e2-b05d-135c8ad3b3d6").set_symbol("BTC-USDT")
        req = builder.build()
        try:
            resp = self.api.cancel_order_by_client_oid(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_get_order_by_client_oid_req(self):
        """
            get_order_by_client_oid
            Get Order By ClientOid
            /api/v3/hf/margin/orders/client-order/{clientOid}
        """

        builder = GetOrderByClientOidReqBuilder()
        builder.set_symbol("BTC-USDT").set_client_oid("b25db7e1-92de-40d9-9671-3022df3358d0")
        req = builder.build()
        try:
            resp = self.api.get_order_by_client_oid(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_cancel_all_orders_by_symbol_req(self):
        """
            cancel_all_orders_by_symbol
            Cancel All Orders By Symbol
            /api/v3/hf/margin/orders
        """

        builder = CancelAllOrdersBySymbolReqBuilder()
        builder.set_symbol("BTC-USDT").set_trade_type(CancelAllOrdersBySymbolReq.TradeTypeEnum.MARGIN_ISOLATED_TRADE)
        req = builder.build()
        try:
            resp = self.api.cancel_all_orders_by_symbol(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_get_closed_orders_req(self):
        """
            get_closed_orders
            Get Closed Orders
            /api/v3/hf/margin/orders/done
        """

        builder = GetClosedOrdersReqBuilder()
        builder.set_symbol("BTC-USDT").set_trade_type(
            GetClosedOrdersReq.TradeTypeEnum.MARGIN_ISOLATED_TRADE).set_side(
            GetClosedOrdersReq.SideEnum.BUY)
        req = builder.build()
        try:
            resp = self.api.get_closed_orders(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_cancel_order_by_order_id_req(self):
        """
            cancel_order_by_order_id
            Cancel Order By OrderId
            /api/v3/hf/margin/orders/{orderId}
        """

        builder = CancelOrderByOrderIdReqBuilder()
        builder.set_symbol("BTC-USDT").set_order_id("6746840ec5ba7400070e8d50")
        req = builder.build()
        try:
            resp = self.api.cancel_order_by_order_id(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_get_order_by_order_id_req(self):
        """
            get_order_by_order_id
            Get Order By OrderId
            /api/v3/hf/margin/orders/{orderId}
        """

        builder = GetOrderByOrderIdReqBuilder()
        builder.set_symbol("BTC-USDT").set_order_id("6746840ec5ba7400070e8d50")
        req = builder.build()
        try:
            resp = self.api.get_order_by_order_id(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e
