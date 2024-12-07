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


class AffiliateApiTest(unittest.TestCase):
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
        self.api = kucoin_rest_api.get_affiliate_service().get_affiliate_api()

    # TODO no permission
    def test_get_account_req(self):
        """
            get_account
            Get Account
            /api/v2/affiliate/inviter/statistics
        """

        try:
            resp = self.api.get_account()
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e