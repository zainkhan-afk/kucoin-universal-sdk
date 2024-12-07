import os
import unittest
import uuid

from kucoin_universal_sdk.api.client import DefaultClient
from kucoin_universal_sdk.extension.interceptor.logging import LoggingInterceptor
from kucoin_universal_sdk.generate.futures.order.model_add_order_req import AddOrderReqBuilder, AddOrderReq
from kucoin_universal_sdk.generate.futures.order.model_add_order_test_req import AddOrderTestReqBuilder, AddOrderTestReq
from kucoin_universal_sdk.generate.futures.order.model_add_tpsl_order_req import AddTpslOrderReqBuilder, AddTpslOrderReq
from kucoin_universal_sdk.generate.futures.order.model_batch_add_orders_item import BatchAddOrdersItemBuilder, \
    BatchAddOrdersItem
from kucoin_universal_sdk.generate.futures.order.model_batch_add_orders_req import BatchAddOrdersReqBuilder
from kucoin_universal_sdk.generate.futures.order.model_batch_cancel_orders_client_oids_list import \
    BatchCancelOrdersClientOidsListBuilder
from kucoin_universal_sdk.generate.futures.order.model_batch_cancel_orders_req import BatchCancelOrdersReqBuilder
from kucoin_universal_sdk.generate.futures.order.model_cancel_all_orders_req import CancelAllOrdersReqBuilder
from kucoin_universal_sdk.generate.futures.order.model_cancel_all_stop_orders_req import CancelAllStopOrdersReqBuilder
from kucoin_universal_sdk.generate.futures.order.model_cancel_order_by_client_oid_req import \
    CancelOrderByClientOidReqBuilder
from kucoin_universal_sdk.generate.futures.order.model_cancel_order_by_id_req import CancelOrderByIdReqBuilder
from kucoin_universal_sdk.generate.futures.order.model_get_open_order_value_req import GetOpenOrderValueReqBuilder
from kucoin_universal_sdk.generate.futures.order.model_get_order_by_client_oid_req import GetOrderByClientOidReqBuilder
from kucoin_universal_sdk.generate.futures.order.model_get_order_by_order_id_req import GetOrderByOrderIdReqBuilder
from kucoin_universal_sdk.generate.futures.order.model_get_order_list_req import GetOrderListReqBuilder, GetOrderListReq
from kucoin_universal_sdk.generate.futures.order.model_get_recent_closed_orders_req import \
    GetRecentClosedOrdersReqBuilder
from kucoin_universal_sdk.generate.futures.order.model_get_recent_trade_history_req import \
    GetRecentTradeHistoryReqBuilder
from kucoin_universal_sdk.generate.futures.order.model_get_stop_order_list_req import GetStopOrderListReqBuilder, \
    GetStopOrderListReq
from kucoin_universal_sdk.generate.futures.order.model_get_trade_history_req import GetTradeHistoryReqBuilder, \
    GetTradeHistoryReq
from kucoin_universal_sdk.model.client_option import ClientOptionBuilder
from kucoin_universal_sdk.model.constants import GLOBAL_API_ENDPOINT, GLOBAL_BROKER_API_ENDPOINT, \
    GLOBAL_FUTURES_API_ENDPOINT
from kucoin_universal_sdk.model.transport_option import TransportOptionBuilder


class FuturesApiTest(unittest.TestCase):
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
        self.api = kucoin_rest_api.get_futures_service().get_order_api()

    def test_get_trade_history_req(self):
        """
            get_trade_history
            Get Trade History
            /api/v1/fills
        """

        builder = GetTradeHistoryReqBuilder()
        builder.set_side(GetTradeHistoryReq.SideEnum.BUY).set_type(GetTradeHistoryReq.TypeEnum.MARKET).set_start_at(
            1732550400000).set_end_at(1732723200000)
        req = builder.build()
        try:
            resp = self.api.get_trade_history(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_get_open_order_value_req(self):
        """
            get_open_order_value
            Get Open Order Value
            /api/v1/openOrderStatistics
        """

        builder = GetOpenOrderValueReqBuilder()
        builder.set_symbol("DOGEUSDTM")
        req = builder.build()
        try:
            resp = self.api.get_open_order_value(req)
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
            /api/v1/orders/byClientOid
        """

        builder = GetOrderByClientOidReqBuilder()
        builder.set_client_oid("df2e52bb-1d11-44d9-91a9-26899f3f46cb")
        req = builder.build()
        try:
            resp = self.api.get_order_by_client_oid(req)
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
            /api/v1/orders/client-order/{clientOid}
        """

        builder = CancelOrderByClientOidReqBuilder()
        builder.set_symbol("XBTUSDTM").set_client_oid("340cbc2a-13a7-468a-85e7-d05a9c607a67")
        req = builder.build()
        try:
            resp = self.api.cancel_order_by_client_oid(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_cancel_all_orders_req(self):
        """
            cancel_all_orders
            Cancel All Orders
            /api/v1/orders
        """

        builder = CancelAllOrdersReqBuilder()
        builder.set_symbol("XBTUSDTM")
        req = builder.build()
        try:
            resp = self.api.cancel_all_orders(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_get_order_list_req(self):
        """
            get_order_list
            Get Order List
            /api/v1/orders
        """

        builder = GetOrderListReqBuilder()
        builder.set_symbol("XBTUSDTM").set_side(GetOrderListReq.SideEnum.BUY).set_type(
            GetOrderListReq.TypeEnum.LIMIT).set_start_at(1732550400000).set_end_at(1732723200000)
        req = builder.build()
        try:
            resp = self.api.get_order_list(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_batch_cancel_orders_req(self):
        """
            batch_cancel_orders
            Batch Cancel Orders
            /api/v1/orders/multi-cancel
        """

        o1 = BatchCancelOrdersClientOidsListBuilder().set_client_oid(
            "59872a92-c10d-4027-a7f5-9eebe966eda6").set_symbol("XBTUSDTM").build()
        o2 = BatchCancelOrdersClientOidsListBuilder().set_client_oid(
            "4bd8e0c5-a57a-4627-a23b-3d5f3d87184b").set_symbol("XBTUSDTM").build()

        builder = BatchCancelOrdersReqBuilder()
        builder.set_order_ids_list(['251157545060700160', '251157545257832449']).set_client_oids_list([o1, o2])
        req = builder.build()
        try:
            resp = self.api.batch_cancel_orders(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_batch_add_orders_req(self):
        """
            batch_add_orders
            Batch Add Orders
            /api/v1/orders/multi
        """

        builder = BatchAddOrdersReqBuilder()

        order1 = BatchAddOrdersItemBuilder().set_client_oid(uuid.uuid4().__str__()).set_side(
            BatchAddOrdersItem.SideEnum.BUY).set_symbol("XBTUSDTM").set_leverage(1).set_type(
            BatchAddOrdersItem.TypeEnum.LIMIT).set_remark("sdk_test").set_margin_mode(
            BatchAddOrdersItem.MarginModeEnum.CROSS).set_price("10000").set_size(1).build()

        order2 = BatchAddOrdersItemBuilder().set_client_oid(uuid.uuid4().__str__()).set_side(
            BatchAddOrdersItem.SideEnum.BUY).set_symbol("XBTUSDTM").set_leverage(1).set_type(
            BatchAddOrdersItem.TypeEnum.LIMIT).set_remark("sdk_test").set_margin_mode(
            BatchAddOrdersItem.MarginModeEnum.CROSS).set_price("10000").set_size(1).build()
        builder.set_items([order1, order2])
        req = builder.build()

        try:
            resp = self.api.batch_add_orders(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_cancel_order_by_id_req(self):
        """
            cancel_order_by_id
            Cancel Order By OrderId
            /api/v1/orders/{orderId}
        """

        builder = CancelOrderByIdReqBuilder()
        builder.set_order_id("251138988260249600")
        req = builder.build()
        try:
            resp = self.api.cancel_order_by_id(req)
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
            /api/v1/orders/{order-id}
        """

        builder = GetOrderByOrderIdReqBuilder()
        builder.set_order_id("251138988260249600")
        req = builder.build()
        try:
            resp = self.api.get_order_by_order_id(req)
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
            /api/v1/orders
        """

        builder = AddOrderReqBuilder()
        builder.set_client_oid(uuid.uuid4().__str__()).set_side(
            AddOrderReq.SideEnum.BUY).set_symbol("XBTUSDTM").set_leverage(1).set_type(
            AddOrderReq.TypeEnum.LIMIT).set_remark("sdk_test").set_margin_mode(
            AddOrderReq.MarginModeEnum.CROSS).set_price("10000").set_size(1)
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
            /api/v1/orders/test
        """

        builder = AddOrderTestReqBuilder()
        builder.set_client_oid(uuid.uuid4().__str__()).set_side(
            AddOrderTestReq.SideEnum.BUY).set_symbol("XBTUSDTM").set_leverage(1).set_type(
            AddOrderTestReq.TypeEnum.LIMIT).set_remark("sdk_test").set_margin_mode(
            AddOrderTestReq.MarginModeEnum.CROSS).set_price("10000").set_size(1)
        req = builder.build()
        try:
            resp = self.api.add_order_test(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_get_recent_closed_orders_req(self):
        """
            get_recent_closed_orders
            Get Recent Closed Orders
            /api/v1/recentDoneOrders
        """

        builder = GetRecentClosedOrdersReqBuilder()
        builder.set_symbol("DOGEUSDTM")
        req = builder.build()
        try:
            resp = self.api.get_recent_closed_orders(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_get_recent_trade_history_req(self):
        """
            get_recent_trade_history
            Get Recent Trade History
            /api/v1/recentFills
        """

        builder = GetRecentTradeHistoryReqBuilder()
        builder.set_symbol("DOGEUSDTM")
        req = builder.build()
        try:
            resp = self.api.get_recent_trade_history(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_add_tpsl_order_req(self):
        """
            add_tpsl_order
            Add Take Profit And Stop Loss Order
            /api/v1/st-orders
        """

        builder = AddTpslOrderReqBuilder()
        builder.set_client_oid(uuid.uuid4().__str__()).set_side(
            AddTpslOrderReq.SideEnum.BUY).set_symbol("XBTUSDTM").set_leverage(1).set_type(
            AddTpslOrderReq.TypeEnum.LIMIT).set_remark("sdk_test").set_margin_mode(
            AddTpslOrderReq.MarginModeEnum.CROSS).set_price("10000").set_size(1).set_stop_price_type(
            AddTpslOrderReq.StopPriceTypeEnum.TRADE_PRICE).set_trigger_stop_up_price(
            "12000").set_trigger_stop_down_price("8000")
        req = builder.build()
        try:
            resp = self.api.add_tpsl_order(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_cancel_all_stop_orders_req(self):
        """
            cancel_all_stop_orders
            Cancel All Stop orders
            /api/v1/stopOrders
        """

        builder = CancelAllStopOrdersReqBuilder()
        builder.set_symbol("XBTUSDTM")
        req = builder.build()
        try:
            resp = self.api.cancel_all_stop_orders(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_get_stop_order_list_req(self):
        """
            get_stop_order_list
            Get Stop Order List
            /api/v1/stopOrders
        """

        builder = GetStopOrderListReqBuilder()
        builder.set_symbol("XBTUSDTM").set_side(GetStopOrderListReq.SideEnum.BUY)
        req = builder.build()
        try:
            resp = self.api.get_stop_order_list(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e
