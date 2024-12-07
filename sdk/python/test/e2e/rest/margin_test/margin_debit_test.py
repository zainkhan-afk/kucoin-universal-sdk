import os
import unittest

from kucoin_universal_sdk.api.client import DefaultClient
from kucoin_universal_sdk.extension.interceptor.logging import LoggingInterceptor
from kucoin_universal_sdk.generate.margin.debit.model_borrow_req import BorrowReqBuilder, BorrowReq
from kucoin_universal_sdk.generate.margin.debit.model_get_borrow_history_req import GetBorrowHistoryReqBuilder
from kucoin_universal_sdk.generate.margin.debit.model_get_interest_history_req import GetInterestHistoryReqBuilder
from kucoin_universal_sdk.generate.margin.debit.model_get_repay_history_req import GetRepayHistoryReqBuilder
from kucoin_universal_sdk.generate.margin.debit.model_modify_leverage_req import ModifyLeverageReqBuilder
from kucoin_universal_sdk.generate.margin.debit.model_repay_req import RepayReqBuilder
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
        self.api = kucoin_rest_api.get_margin_service().get_debit_api()

    def test_get_borrow_history_req(self):
        """
            get_borrow_history
            Get Borrow History
            /api/v3/margin/borrow
        """

        builder = GetBorrowHistoryReqBuilder()
        builder.set_currency("USDT").set_is_isolated(True).set_symbol("BTC-USDT")
        req = builder.build()
        try:
            resp = self.api.get_borrow_history(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_borrow_req(self):
        """
            borrow
            Borrow
            /api/v3/margin/borrow
        """

        builder = BorrowReqBuilder()
        builder.set_currency("USDT").set_size(10.0).set_time_in_force(BorrowReq.TimeInForceEnum.IOC).set_symbol(
            "BTC-USDT").set_is_isolated(True).set_is_hf(True)
        req = builder.build()
        try:
            resp = self.api.borrow(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_get_interest_history_req(self):
        """
            get_interest_history
            Get Interest History
            /api/v3/margin/interest
        """

        builder = GetInterestHistoryReqBuilder()
        builder.set_currency("USDT").set_is_isolated(True).set_symbol("BTC-USDT")
        req = builder.build()
        try:
            resp = self.api.get_interest_history(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_get_repay_history_req(self):
        """
            get_repay_history
            Get Repay History
            /api/v3/margin/repay
        """

        builder = GetRepayHistoryReqBuilder()
        builder.set_currency("USDT").set_is_isolated(True).set_symbol("BTC-USDT").set_order_no(
            "67467fcefc3d5000075c5ec2")
        req = builder.build()
        try:
            resp = self.api.get_repay_history(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_repay_req(self):
        """
            repay
            Repay
            /api/v3/margin/repay
        """

        builder = RepayReqBuilder()
        builder.set_currency("USDT").set_size(10).set_symbol("BTC-USDT").set_is_isolated(True).set_is_hf(True)
        req = builder.build()
        try:
            resp = self.api.repay(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_modify_leverage_req(self):
        """
            modify_leverage
            Modify Leverage
            /api/v3/position/update-user-leverage
        """

        builder = ModifyLeverageReqBuilder()
        builder.set_symbol("BTC-USDT").set_is_isolated(True).set_leverage("3.1")
        req = builder.build()
        try:
            resp = self.api.modify_leverage(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e
