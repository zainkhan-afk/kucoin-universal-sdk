import unittest
from .model_add_isolated_margin_req import AddIsolatedMarginReq
from .model_add_isolated_margin_resp import AddIsolatedMarginResp
from .model_add_order_req import AddOrderReq
from .model_add_order_resp import AddOrderResp
from .model_add_order_test_req import AddOrderTestReq
from .model_add_order_test_resp import AddOrderTestResp
from .model_add_tpsl_order_req import AddTpslOrderReq
from .model_add_tpsl_order_resp import AddTpslOrderResp
from .model_cancel_order_by_client_oid_req import CancelOrderByClientOidReq
from .model_cancel_order_by_client_oid_resp import CancelOrderByClientOidResp
from .model_cancel_order_by_id_req import CancelOrderByIdReq
from .model_cancel_order_by_id_resp import CancelOrderByIdResp
from .model_get_max_open_size_req import GetMaxOpenSizeReq
from .model_get_max_open_size_resp import GetMaxOpenSizeResp
from .model_get_max_withdraw_margin_req import GetMaxWithdrawMarginReq
from .model_get_max_withdraw_margin_resp import GetMaxWithdrawMarginResp
from .model_modify_auto_deposit_status_req import ModifyAutoDepositStatusReq
from .model_modify_auto_deposit_status_resp import ModifyAutoDepositStatusResp
from .model_modify_isolated_margin_risk_limt_req import ModifyIsolatedMarginRiskLimtReq
from .model_modify_isolated_margin_risk_limt_resp import ModifyIsolatedMarginRiskLimtResp
from .model_remove_isolated_margin_req import RemoveIsolatedMarginReq
from .model_remove_isolated_margin_resp import RemoveIsolatedMarginResp
from kucoin_universal_sdk.model.common import RestResponse


class FuturesAPITest(unittest.TestCase):

    def test_add_order_req_model(self):
        """
       add_order
       Add Order
       /api/v1/copy-trade/futures/orders
       """
        data = "{\"clientOid\": \"5c52e11203aa677f33e493fb\", \"side\": \"buy\", \"symbol\": \"XBTUSDTM\", \"leverage\": 3, \"type\": \"limit\", \"remark\": \"order remarks\", \"reduceOnly\": false, \"marginMode\": \"ISOLATED\", \"price\": \"0.1\", \"size\": 1, \"timeInForce\": \"GTC\"}"
        req = AddOrderReq.from_json(data)

    def test_add_order_resp_model(self):
        """
        add_order
        Add Order
        /api/v1/copy-trade/futures/orders
        """
        data = "{\n    \"code\": \"200000\",\n    \"data\": {\n        \"orderId\": \"263485113055133696\",\n        \"clientOid\": \"5c52e11203aa677f331e493fb\"\n    }\n}"
        common_response = RestResponse.from_json(data)
        resp = AddOrderResp.from_dict(common_response.data)

    def test_add_order_test_req_model(self):
        """
       add_order_test
       Add Order Test
       /api/v1/copy-trade/futures/orders/test
       """
        data = "{\"clientOid\": \"5c52e11203aa677f33e493fb\", \"side\": \"buy\", \"symbol\": \"XBTUSDTM\", \"leverage\": 3, \"type\": \"limit\", \"remark\": \"order remarks\", \"reduceOnly\": false, \"marginMode\": \"ISOLATED\", \"price\": \"0.1\", \"size\": 1, \"timeInForce\": \"GTC\"}"
        req = AddOrderTestReq.from_json(data)

    def test_add_order_test_resp_model(self):
        """
        add_order_test
        Add Order Test
        /api/v1/copy-trade/futures/orders/test
        """
        data = "{\n    \"code\": \"200000\",\n    \"data\": {\n        \"orderId\": \"234125150956625920\",\n        \"clientOid\": \"5c52e11203aa677f33e493fb\"\n    }\n}"
        common_response = RestResponse.from_json(data)
        resp = AddOrderTestResp.from_dict(common_response.data)

    def test_add_tpsl_order_req_model(self):
        """
       add_tpsl_order
       Add Take Profit And Stop Loss Order
       /api/v1/copy-trade/futures/st-orders
       """
        data = "{\"clientOid\": \"5c52e11203aa677f33e493fb\", \"side\": \"buy\", \"symbol\": \"XBTUSDTM\", \"leverage\": 3, \"type\": \"limit\", \"remark\": \"order remarks\", \"reduceOnly\": false, \"marginMode\": \"ISOLATED\", \"price\": \"0.2\", \"size\": 1, \"timeInForce\": \"GTC\", \"triggerStopUpPrice\": \"0.3\", \"triggerStopDownPrice\": \"0.1\", \"stopPriceType\": \"TP\"}"
        req = AddTpslOrderReq.from_json(data)

    def test_add_tpsl_order_resp_model(self):
        """
        add_tpsl_order
        Add Take Profit And Stop Loss Order
        /api/v1/copy-trade/futures/st-orders
        """
        data = "{\n    \"code\": \"200000\",\n    \"data\": {\n        \"orderId\": \"234125150956625920\",\n        \"clientOid\": \"5c52e11203aa677f33e493fb\"\n    }\n}"
        common_response = RestResponse.from_json(data)
        resp = AddTpslOrderResp.from_dict(common_response.data)

    def test_cancel_order_by_id_req_model(self):
        """
       cancel_order_by_id
       Cancel Order By OrderId
       /api/v1/copy-trade/futures/orders
       """
        data = "{\"orderId\": \"263485113055133696\"}"
        req = CancelOrderByIdReq.from_json(data)

    def test_cancel_order_by_id_resp_model(self):
        """
        cancel_order_by_id
        Cancel Order By OrderId
        /api/v1/copy-trade/futures/orders
        """
        data = "{\n    \"code\": \"200000\",\n    \"data\": {\n        \"cancelledOrderIds\": [\n            \"263485113055133696\"\n        ]\n    }\n}"
        common_response = RestResponse.from_json(data)
        resp = CancelOrderByIdResp.from_dict(common_response.data)

    def test_cancel_order_by_client_oid_req_model(self):
        """
       cancel_order_by_client_oid
       Cancel Order By ClientOid
       /api/v1/copy-trade/futures/orders/client-order
       """
        data = "{\"symbol\": \"XBTUSDTM\", \"clientOid\": \"5c52e11203aa677f331e493fb\"}"
        req = CancelOrderByClientOidReq.from_json(data)

    def test_cancel_order_by_client_oid_resp_model(self):
        """
        cancel_order_by_client_oid
        Cancel Order By ClientOid
        /api/v1/copy-trade/futures/orders/client-order
        """
        data = "{\n    \"code\": \"200000\",\n    \"data\": {\n        \"clientOid\": \"5c52e11203aa677f331e4913fb\"\n    }\n}"
        common_response = RestResponse.from_json(data)
        resp = CancelOrderByClientOidResp.from_dict(common_response.data)

    def test_get_max_open_size_req_model(self):
        """
       get_max_open_size
       Get Max Open Size
       /api/v1/copy-trade/futures/get-max-open-size
       """
        data = "{\"symbol\": \"XBTUSDTM\", \"price\": \"example_string_default_value\", \"leverage\": 123456}"
        req = GetMaxOpenSizeReq.from_json(data)

    def test_get_max_open_size_resp_model(self):
        """
        get_max_open_size
        Get Max Open Size
        /api/v1/copy-trade/futures/get-max-open-size
        """
        data = "{\n    \"code\": \"200000\",\n    \"data\": {\n        \"symbol\": \"XBTUSDTM\",\n        \"maxBuyOpenSize\": 8,\n        \"maxSellOpenSize\": 5\n    }\n}"
        common_response = RestResponse.from_json(data)
        resp = GetMaxOpenSizeResp.from_dict(common_response.data)

    def test_get_max_withdraw_margin_req_model(self):
        """
       get_max_withdraw_margin
       Get Max Withdraw Margin
       /api/v1/copy-trade/futures/position/margin/max-withdraw-margin
       """
        data = "{\"symbol\": \"example_string_default_value\"}"
        req = GetMaxWithdrawMarginReq.from_json(data)

    def test_get_max_withdraw_margin_resp_model(self):
        """
        get_max_withdraw_margin
        Get Max Withdraw Margin
        /api/v1/copy-trade/futures/position/margin/max-withdraw-margin
        """
        data = "{\n    \"code\": \"200000\",\n    \"data\": \"21.1135719252\"\n}"
        common_response = RestResponse.from_json(data)
        resp = GetMaxWithdrawMarginResp.from_dict(common_response.data)

    def test_add_isolated_margin_req_model(self):
        """
       add_isolated_margin
       Add Isolated Margin
       /api/v1/copy-trade/futures/position/margin/deposit-margin
       """
        data = "{\"symbol\": \"string\", \"margin\": 0, \"bizNo\": \"string\"}"
        req = AddIsolatedMarginReq.from_json(data)

    def test_add_isolated_margin_resp_model(self):
        """
        add_isolated_margin
        Add Isolated Margin
        /api/v1/copy-trade/futures/position/margin/deposit-margin
        """
        data = "{\n    \"code\": \"200000\",\n    \"data\": {\n        \"id\": \"6200c9b83aecfb000152ddcd\",\n        \"symbol\": \"XBTUSDTM\",\n        \"autoDeposit\": false,\n        \"maintMarginReq\": 0.005,\n        \"riskLimit\": 500000,\n        \"realLeverage\": 18.72,\n        \"crossMode\": false,\n        \"delevPercentage\": 0.66,\n        \"openingTimestamp\": 1646287090131,\n        \"currentTimestamp\": 1646295055021,\n        \"currentQty\": 1,\n        \"currentCost\": 43.388,\n        \"currentComm\": 0.0260328,\n        \"unrealisedCost\": 43.388,\n        \"realisedGrossCost\": 0,\n        \"realisedCost\": 0.0260328,\n        \"isOpen\": true,\n        \"markPrice\": 43536.65,\n        \"markValue\": 43.53665,\n        \"posCost\": 43.388,\n        \"posCross\": 0.000024985,\n        \"posInit\": 2.1694,\n        \"posComm\": 0.02733446,\n        \"posLoss\": 0,\n        \"posMargin\": 2.19675944,\n        \"posMaint\": 0.24861326,\n        \"maintMargin\": 2.34540944,\n        \"realisedGrossPnl\": 0,\n        \"realisedPnl\": -0.0260328,\n        \"unrealisedPnl\": 0.14865,\n        \"unrealisedPnlPcnt\": 0.0034,\n        \"unrealisedRoePcnt\": 0.0685,\n        \"avgEntryPrice\": 43388,\n        \"liquidationPrice\": 41440,\n        \"bankruptPrice\": 41218,\n        \"userId\": 1234321123,\n        \"settleCurrency\": \"USDT\"\n    }\n}"
        common_response = RestResponse.from_json(data)
        resp = AddIsolatedMarginResp.from_dict(common_response.data)

    def test_remove_isolated_margin_req_model(self):
        """
       remove_isolated_margin
       Remove Isolated Margin
       /api/v1/copy-trade/futures/position/margin/withdraw-margin
       """
        data = "{\"symbol\": \"XBTUSDTM\", \"withdrawAmount\": \"0.0000001\"}"
        req = RemoveIsolatedMarginReq.from_json(data)

    def test_remove_isolated_margin_resp_model(self):
        """
        remove_isolated_margin
        Remove Isolated Margin
        /api/v1/copy-trade/futures/position/margin/withdraw-margin
        """
        data = "{\n    \"code\": \"200000\",\n    \"data\": \"0.1\"\n}"
        common_response = RestResponse.from_json(data)
        resp = RemoveIsolatedMarginResp.from_dict(common_response.data)

    def test_modify_isolated_margin_risk_limt_req_model(self):
        """
       modify_isolated_margin_risk_limt
       Modify Isolated Margin Risk Limit
       /api/v1/copy-trade/futures/position/risk-limit-level/change
       """
        data = "{\"symbol\": \"XBTUSDTM\", \"level\": 1}"
        req = ModifyIsolatedMarginRiskLimtReq.from_json(data)

    def test_modify_isolated_margin_risk_limt_resp_model(self):
        """
        modify_isolated_margin_risk_limt
        Modify Isolated Margin Risk Limit
        /api/v1/copy-trade/futures/position/risk-limit-level/change
        """
        data = "{\n    \"code\": \"200000\",\n    \"data\": true\n}"
        common_response = RestResponse.from_json(data)
        resp = ModifyIsolatedMarginRiskLimtResp.from_dict(common_response.data)

    def test_modify_auto_deposit_status_req_model(self):
        """
       modify_auto_deposit_status
       Modify Isolated Margin Auto-Deposit Status
       /api/v1/copy-trade/futures/position/margin/auto-deposit-status
       """
        data = "{\"symbol\": \"XBTUSDTM\", \"status\": true}"
        req = ModifyAutoDepositStatusReq.from_json(data)

    def test_modify_auto_deposit_status_resp_model(self):
        """
        modify_auto_deposit_status
        Modify Isolated Margin Auto-Deposit Status
        /api/v1/copy-trade/futures/position/margin/auto-deposit-status
        """
        data = "{\n    \"code\": \"200000\",\n    \"data\": true\n}"
        common_response = RestResponse.from_json(data)
        resp = ModifyAutoDepositStatusResp.from_dict(common_response.data)
