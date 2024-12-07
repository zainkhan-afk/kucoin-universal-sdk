import os
import unittest

from kucoin_universal_sdk.api.client import DefaultClient
from kucoin_universal_sdk.extension.interceptor.logging import LoggingInterceptor
from kucoin_universal_sdk.generate.spot.market.model_get24hr_stats_req import Get24hrStatsReqBuilder
from kucoin_universal_sdk.generate.spot.market.model_get_all_symbols_req import GetAllSymbolsReqBuilder
from kucoin_universal_sdk.generate.spot.market.model_get_announcements_req import GetAnnouncementsReqBuilder, \
    GetAnnouncementsReq
from kucoin_universal_sdk.generate.spot.market.model_get_currency_req import GetCurrencyReqBuilder
from kucoin_universal_sdk.generate.spot.market.model_get_fiat_price_req import GetFiatPriceReqBuilder
from kucoin_universal_sdk.generate.spot.market.model_get_full_order_book_req import GetFullOrderBookReqBuilder
from kucoin_universal_sdk.generate.spot.market.model_get_klines_req import GetKlinesReqBuilder, GetKlinesReq
from kucoin_universal_sdk.generate.spot.market.model_get_part_order_book_req import GetPartOrderBookReqBuilder
from kucoin_universal_sdk.generate.spot.market.model_get_symbol_req import GetSymbolReqBuilder
from kucoin_universal_sdk.generate.spot.market.model_get_ticker_req import GetTickerReqBuilder
from kucoin_universal_sdk.generate.spot.market.model_get_trade_history_req import GetTradeHistoryReqBuilder
from kucoin_universal_sdk.model.client_option import ClientOptionBuilder
from kucoin_universal_sdk.model.constants import GLOBAL_API_ENDPOINT, GLOBAL_BROKER_API_ENDPOINT, \
    GLOBAL_FUTURES_API_ENDPOINT
from kucoin_universal_sdk.model.transport_option import TransportOptionBuilder


class VipLendingApiTest(unittest.TestCase):
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
        self.api = kucoin_rest_api.get_vip_lending_service().get_vip_lending_api()

    # TODO no permission
    def test_get_accounts_req(self):
        """
            get_accounts
            Get Accounts
            /api/v1/otc-loan/accounts
        """

        try:
            resp = self.api.get_accounts()
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    # TODO no permission
    def test_get_account_detail_req(self):
        """
            get_account_detail
            Get Account Detail
            /api/v1/otc-loan/loan
        """

        try:
            resp = self.api.get_account_detail()
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

