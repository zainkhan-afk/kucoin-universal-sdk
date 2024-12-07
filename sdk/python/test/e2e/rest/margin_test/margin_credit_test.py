import os
import unittest

from kucoin_universal_sdk.api.client import DefaultClient
from kucoin_universal_sdk.extension.interceptor.logging import LoggingInterceptor
from kucoin_universal_sdk.generate.margin.credit.model_get_loan_market_interest_rate_req import \
    GetLoanMarketInterestRateReqBuilder
from kucoin_universal_sdk.generate.margin.credit.model_get_loan_market_req import GetLoanMarketReqBuilder
from kucoin_universal_sdk.generate.margin.credit.model_get_purchase_orders_req import GetPurchaseOrdersReqBuilder, \
    GetPurchaseOrdersReq
from kucoin_universal_sdk.generate.margin.credit.model_get_redeem_orders_req import GetRedeemOrdersReqBuilder, \
    GetRedeemOrdersReq
from kucoin_universal_sdk.generate.margin.credit.model_modify_purchase_req import ModifyPurchaseReqBuilder
from kucoin_universal_sdk.generate.margin.credit.model_purchase_req import PurchaseReqBuilder
from kucoin_universal_sdk.generate.margin.credit.model_redeem_req import RedeemReqBuilder
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
        self.api = kucoin_rest_api.get_margin_service().get_credit_api()

    def test_modify_purchase_req(self):
        """
            modify_purchase
            Modify Purchase
            /api/v3/lend/purchase/update
        """

        builder = ModifyPurchaseReqBuilder()
        builder.set_currency("DOGE").set_interest_rate("0.02").set_purchase_order_no("67467d4b7e9f470007e55df6")
        req = builder.build()
        try:
            resp = self.api.modify_purchase(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_get_loan_market_req(self):
        """
            get_loan_market
            Get Loan Market
            /api/v3/project/list
        """

        builder = GetLoanMarketReqBuilder()
        builder.set_currency("DOGE")
        req = builder.build()
        try:
            resp = self.api.get_loan_market(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_get_loan_market_interest_rate_req(self):
        """
            get_loan_market_interest_rate
            Get Loan Market Interest Rate
            /api/v3/project/marketInterestRate
        """

        builder = GetLoanMarketInterestRateReqBuilder()
        builder.set_currency("DOGE")
        req = builder.build()
        try:
            resp = self.api.get_loan_market_interest_rate(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_get_purchase_orders_req(self):
        """
            get_purchase_orders
            Get Purchase Orders
            /api/v3/purchase/orders
        """

        builder = GetPurchaseOrdersReqBuilder()
        builder.set_currency("DOGE").set_purchase_order_no("67467d4b7e9f470007e55df6").set_status(
            GetPurchaseOrdersReq.StatusEnum.PENDING)
        req = builder.build()
        try:
            resp = self.api.get_purchase_orders(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_purchase_req(self):
        """
            purchase
            Purchase
            /api/v3/purchase
        """

        builder = PurchaseReqBuilder()
        builder.set_currency("DOGE").set_size("10").set_interest_rate("0.01")
        req = builder.build()
        try:
            resp = self.api.purchase(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_get_redeem_orders_req(self):
        """
            get_redeem_orders
            Get Redeem Orders
            /api/v3/redeem/orders
        """

        builder = GetRedeemOrdersReqBuilder()
        builder.set_currency("DOGE").set_status(GetRedeemOrdersReq.StatusEnum.DONE)
        req = builder.build()
        try:
            resp = self.api.get_redeem_orders(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_redeem_req(self):
        """
            redeem
            Redeem
            /api/v3/redeem
        """

        builder = RedeemReqBuilder()
        builder.set_currency("DOGE").set_size("10").set_purchase_order_no("67467d4b7e9f470007e55df6")
        req = builder.build()
        try:
            resp = self.api.redeem(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e
