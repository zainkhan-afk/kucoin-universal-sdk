import os
import unittest

from kucoin_universal_sdk.api.client import DefaultClient
from kucoin_universal_sdk.extension.interceptor.logging import LoggingInterceptor
from kucoin_universal_sdk.generate.account.fee.model_get_basic_fee_req import GetBasicFeeReqBuilder, GetBasicFeeReq
from kucoin_universal_sdk.generate.account.fee.model_get_futures_actual_fee_req import GetFuturesActualFeeReqBuilder
from kucoin_universal_sdk.generate.account.fee.model_get_spot_actual_fee_req import GetSpotActualFeeReqBuilder
from kucoin_universal_sdk.generate.account.withdrawal.model_get_withdrawal_history_old_req import \
    GetWithdrawalHistoryOldReqBuilder
from kucoin_universal_sdk.generate.account.withdrawal.model_get_withdrawal_history_req import \
    GetWithdrawalHistoryReqBuilder
from kucoin_universal_sdk.model.client_option import ClientOptionBuilder
from kucoin_universal_sdk.model.constants import GLOBAL_API_ENDPOINT, GLOBAL_FUTURES_API_ENDPOINT, \
    GLOBAL_BROKER_API_ENDPOINT
from kucoin_universal_sdk.model.transport_option import TransportOptionBuilder


class AccountApiTest(unittest.TestCase):
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
        self.api = kucoin_rest_api.get_account_service().get_fee_api()

    def test_get_basic_fee_req(self):
        """
            get_basic_fee
            Get Basic Fee - Spot/Margin
            /api/v1/base-fee
        """

        builder = GetBasicFeeReqBuilder()
        builder.set_currency_type(GetBasicFeeReq.CurrencyTypeEnum.T_0)
        req = builder.build()
        try:
            resp = self.api.get_basic_fee(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_get_futures_actual_fee_req(self):
        """
            get_futures_actual_fee
            Get Actual Fee - Futures
            /api/v1/trade-fees
        """

        builder = GetFuturesActualFeeReqBuilder()
        builder.set_symbol("XBTUSDM")
        req = builder.build()
        try:
            resp = self.api.get_futures_actual_fee(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_get_spot_actual_fee_req(self):
        """
            get_spot_actual_fee
            Get Actual Fee - Spot/Margin
            /api/v1/trade-fees
        """

        builder = GetSpotActualFeeReqBuilder()
        builder.set_symbols("BTC-USDT")
        req = builder.build()
        try:
            resp = self.api.get_spot_actual_fee(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

