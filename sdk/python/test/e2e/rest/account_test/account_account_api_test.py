import os
import unittest

from kucoin_universal_sdk.api.client import DefaultClient
from kucoin_universal_sdk.extension.interceptor.logging import LoggingInterceptor
from kucoin_universal_sdk.generate.account.account.model_get_cross_margin_account_req import \
    GetCrossMarginAccountReqBuilder, GetCrossMarginAccountReq
from kucoin_universal_sdk.generate.account.account.model_get_futures_account_req import GetFuturesAccountReqBuilder
from kucoin_universal_sdk.generate.account.account.model_get_futures_ledger_req import GetFuturesLedgerReqBuilder
from kucoin_universal_sdk.generate.account.account.model_get_isolated_margin_account_detail_v1_req import \
    GetIsolatedMarginAccountDetailV1ReqBuilder
from kucoin_universal_sdk.generate.account.account.model_get_isolated_margin_account_list_v1_req import \
    GetIsolatedMarginAccountListV1ReqBuilder, GetIsolatedMarginAccountListV1Req
from kucoin_universal_sdk.generate.account.account.model_get_isolated_margin_account_req import \
    GetIsolatedMarginAccountReqBuilder, GetIsolatedMarginAccountReq
from kucoin_universal_sdk.generate.account.account.model_get_margin_hf_ledger_req import GetMarginHfLedgerReqBuilder
from kucoin_universal_sdk.generate.account.account.model_get_spot_account_detail_req import \
    GetSpotAccountDetailReqBuilder
from kucoin_universal_sdk.generate.account.account.model_get_spot_account_list_req import GetSpotAccountListReqBuilder, \
    GetSpotAccountListReq
from kucoin_universal_sdk.generate.account.account.model_get_spot_hf_ledger_req import GetSpotHfLedgerReqBuilder, \
    GetSpotHfLedgerReq
from kucoin_universal_sdk.generate.account.account.model_get_spot_ledger_req import GetSpotLedgerReqBuilder
from kucoin_universal_sdk.model.client_option import ClientOptionBuilder
from kucoin_universal_sdk.model.constants import GLOBAL_API_ENDPOINT, GLOBAL_BROKER_API_ENDPOINT, \
    GLOBAL_FUTURES_API_ENDPOINT
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
        self.api = kucoin_rest_api.get_account_service().get_account_api()

    def test_get_futures_account_req(self):
        """
            get_futures_account
            Get Account - Futures
            /api/v1/account-overview
        """

        builder = GetFuturesAccountReqBuilder()
        builder.set_currency('XBT')
        req = builder.build()
        try:
            resp = self.api.get_futures_account(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_get_spot_account_detail_req(self):
        """
            get_spot_account_detail
            Get Account Detail - Spot
            /api/v1/accounts/{accountId}
        """

        builder = GetSpotAccountDetailReqBuilder()
        builder.set_account_id('671badb050647f0007d94011')
        req = builder.build()
        try:
            resp = self.api.get_spot_account_detail(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_get_spot_account_list_req(self):
        """
            get_spot_account_list
            Get Account List - Spot
            /api/v1/accounts
        """

        builder = GetSpotAccountListReqBuilder()
        builder.set_type(GetSpotAccountListReq.TypeEnum.MAIN)
        req = builder.build()
        try:
            resp = self.api.get_spot_account_list(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_get_spot_ledger_req(self):
        """
            get_spot_ledger
            Get Account Ledgers - Spot/Margin
            /api/v1/accounts/ledgers
        """

        builder = GetSpotLedgerReqBuilder()
        (builder.set_currency("USDT").set_start_at(1732032000000).
         set_end_at(1732118400000).set_current_page(1).set_page_size(100))
        req = builder.build()
        try:
            resp = self.api.get_spot_ledger(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_get_spot_hf_ledger_req(self):
        """
            get_spot_hf_ledger
            Get Account Ledgers - Trade_hf
            /api/v1/hf/accounts/ledgers
        """

        builder = GetSpotHfLedgerReqBuilder()
        (builder.set_currency('USDT').set_direction(GetSpotHfLedgerReq.DirectionEnum.OUT).
         set_biz_type(GetSpotHfLedgerReq.BizTypeEnum.TRANSFER))
        req = builder.build()
        try:
            resp = self.api.get_spot_hf_ledger(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_get_spot_account_type_req(self):
        """
            get_spot_account_type
            Get Account Type - Spot
            /api/v1/hf/accounts/opened
        """

        try:
            resp = self.api.get_spot_account_type()
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_get_isolated_margin_account_detail_v1_req(self):
        """
            get_isolated_margin_account_detail_v1
            Get Account Detail - Isolated Margin V1
            /api/v1/isolated/account/{symbol}
        """

        builder = GetIsolatedMarginAccountDetailV1ReqBuilder()
        builder.set_symbol("BTC-USDT")
        req = builder.build()
        try:
            resp = self.api.get_isolated_margin_account_detail_v1(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_get_isolated_margin_account_list_v1_req(self):
        """
            get_isolated_margin_account_list_v1
            Get Account List - Isolated Margin V1
            /api/v1/isolated/accounts
        """

        builder = GetIsolatedMarginAccountListV1ReqBuilder()
        builder.set_balance_currency(GetIsolatedMarginAccountListV1Req.BalanceCurrencyEnum.BTC)
        req = builder.build()
        try:
            resp = self.api.get_isolated_margin_account_list_v1(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_get_margin_account_detail_req(self):
        """
            get_margin_account_detail
            Get Account Detail - Margin
            /api/v1/margin/account
        """

        try:
            resp = self.api.get_margin_account_detail()
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_get_futures_ledger_req(self):
        """
            get_futures_ledger
            Get Account Ledgers - Futures
            /api/v1/transaction-history
        """

        builder = GetFuturesLedgerReqBuilder()
        builder.set_currency('DOT').set_type('RealisedPNL')
        req = builder.build()
        try:
            resp = self.api.get_futures_ledger(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_get_apikey_info_req(self):
        """
            get_apikey_info
            Get API Key Information
            /api/v1/user/api-key
        """

        try:
            resp = self.api.get_apikey_info()
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_get_account_info_req(self):
        """
            get_account_info
            Get Account Summary Info
            /api/v2/user-info
        """

        try:
            resp = self.api.get_account_info()
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_get_margin_hf_ledger_req(self):
        """
            get_margin_hf_ledger
            Get Account Ledgers - Margin_hf
            /api/v3/hf/margin/account/ledgers
        """

        builder = GetMarginHfLedgerReqBuilder()
        builder.set_currency("USDT")
        req = builder.build()
        try:
            resp = self.api.get_margin_hf_ledger(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_get_isolated_margin_account_req(self):
        """
            get_isolated_margin_account
            Get Account - Isolated Margin
            /api/v3/isolated/accounts
        """

        builder = GetIsolatedMarginAccountReqBuilder()
        (builder.set_symbol('BTC-USDT').
         set_quote_currency(GetIsolatedMarginAccountReq.QuoteCurrencyEnum.USDT).
         set_query_type(GetIsolatedMarginAccountReq.QueryTypeEnum.ISOLATED))
        req = builder.build()
        try:
            resp = self.api.get_isolated_margin_account(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_get_cross_margin_account_req(self):
        """
            get_cross_margin_account
            Get Account - Cross Margin
            /api/v3/margin/accounts
        """

        builder = GetCrossMarginAccountReqBuilder()
        (builder.set_quote_currency(GetCrossMarginAccountReq.QuoteCurrencyEnum.USDT).
         set_query_type(GetCrossMarginAccountReq.QueryTypeEnum.MARGIN))
        req = builder.build()
        try:
            resp = self.api.get_cross_margin_account(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e


if __name__ == '__main__':
    unittest.main()
