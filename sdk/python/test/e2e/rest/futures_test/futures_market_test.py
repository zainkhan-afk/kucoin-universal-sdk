import os
import unittest

from kucoin_universal_sdk.api.client import DefaultClient
from kucoin_universal_sdk.extension.interceptor.logging import LoggingInterceptor
from kucoin_universal_sdk.generate.futures.market.model_get_full_order_book_req import GetFullOrderBookReqBuilder
from kucoin_universal_sdk.generate.futures.market.model_get_interest_rate_index_req import \
    GetInterestRateIndexReqBuilder
from kucoin_universal_sdk.generate.futures.market.model_get_klines_req import GetKlinesReqBuilder, GetKlinesReq
from kucoin_universal_sdk.generate.futures.market.model_get_mark_price_req import GetMarkPriceReqBuilder
from kucoin_universal_sdk.generate.futures.market.model_get_part_order_book_req import GetPartOrderBookReqBuilder
from kucoin_universal_sdk.generate.futures.market.model_get_premium_index_req import GetPremiumIndexReqBuilder
from kucoin_universal_sdk.generate.futures.market.model_get_spot_index_price_req import GetSpotIndexPriceReqBuilder
from kucoin_universal_sdk.generate.futures.market.model_get_symbol_req import GetSymbolReqBuilder
from kucoin_universal_sdk.generate.futures.market.model_get_ticker_req import GetTickerReqBuilder
from kucoin_universal_sdk.generate.futures.market.model_get_trade_history_req import GetTradeHistoryReqBuilder
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
        self.api = kucoin_rest_api.get_futures_service().get_market_api()

    def test_get_all_tickers_req(self):
        """
            get_all_tickers
            Get All Tickers
            /api/v1/allTickers
        """

        try:
            resp = self.api.get_all_tickers()
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_get_private_token_req(self):
        """
            get_private_token
            Get Private Token - Futures
            /api/v1/bullet-private
        """

        try:
            resp = self.api.get_private_token()
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_get_public_token_req(self):
        """
            get_public_token
            Get Public Token - Futures
            /api/v1/bullet-public
        """

        try:
            resp = self.api.get_public_token()
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_get_all_symbols_req(self):
        """
            get_all_symbols
            Get All Symbols
            /api/v1/contracts/active
        """

        try:
            resp = self.api.get_all_symbols()
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_get_symbol_req(self):
        """
            get_symbol
            Get Symbol
            /api/v1/contracts/{symbol}
        """

        builder = GetSymbolReqBuilder()
        builder.set_symbol("XBTUSDTM")
        req = builder.build()
        try:
            resp = self.api.get_symbol(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_get_spot_index_price_req(self):
        """
            get_spot_index_price
            Get Spot Index Price
            /api/v1/index/query
        """

        builder = GetSpotIndexPriceReqBuilder()
        builder.set_symbol(".KXBTUSDT").set_start_at(1732464000000).set_end_at(1732521600000).set_max_count(10)
        req = builder.build()
        try:
            resp = self.api.get_spot_index_price(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_get_interest_rate_index_req(self):
        """
            get_interest_rate_index
            Get Interest Rate Index
            /api/v1/interest/query
        """

        builder = GetInterestRateIndexReqBuilder()
        builder.set_symbol(".XBTINT").set_start_at(1732464000000).set_end_at(1732521600000).set_max_count(100)
        req = builder.build()
        try:
            resp = self.api.get_interest_rate_index(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_get_klines_req(self):
        """
            get_klines
            Get Klines
            /api/v1/kline/query
        """

        builder = GetKlinesReqBuilder()
        builder.set_symbol("XBTUSDTM").set_granularity(GetKlinesReq.GranularityEnum.T_1).set_from_(
            1732464000000).set_to(1732521600000)
        req = builder.build()
        try:
            resp = self.api.get_klines(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_get_part_order_book_req(self):
        """
            get_part_order_book
            Get Part OrderBook
            /api/v1/level2/depth{size}
        """

        builder = GetPartOrderBookReqBuilder()
        builder.set_symbol("XBTUSDTM").set_size("100")
        req = builder.build()
        try:
            resp = self.api.get_part_order_book(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_get_full_order_book_req(self):
        """
            get_full_order_book
            Get Full OrderBook
            /api/v1/level2/snapshot
        """

        builder = GetFullOrderBookReqBuilder()
        builder.set_symbol("XBTUSDTM")
        req = builder.build()
        try:
            resp = self.api.get_full_order_book(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_get_mark_price_req(self):
        """
            get_mark_price
            Get Mark Price
            /api/v1/mark-price/{symbol}/current
        """

        builder = GetMarkPriceReqBuilder()
        builder.set_symbol("XBTUSDTM")
        req = builder.build()
        try:
            resp = self.api.get_mark_price(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_get_premium_index_req(self):
        """
            get_premium_index
            Get Premium Index
            /api/v1/premium/query
        """

        builder = GetPremiumIndexReqBuilder()
        builder.set_symbol(".XBTUSDTMPI").set_start_at(1732464000000).set_end_at(1732521600000)
        req = builder.build()
        try:
            resp = self.api.get_premium_index(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_get_service_status_req(self):
        """
            get_service_status
            Get Service Status
            /api/v1/status
        """

        try:
            resp = self.api.get_service_status()
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_get_ticker_req(self):
        """
            get_ticker
            Get Ticker
            /api/v1/ticker
        """

        builder = GetTickerReqBuilder()
        builder.set_symbol("XBTUSDTM")
        req = builder.build()
        try:
            resp = self.api.get_ticker(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_get_server_time_req(self):
        """
            get_server_time
            Get Server Time
            /api/v1/timestamp
        """

        try:
            resp = self.api.get_server_time()
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
            /api/v1/trade/history
        """

        builder = GetTradeHistoryReqBuilder()
        builder.set_symbol("XBTUSDTM")
        req = builder.build()
        try:
            resp = self.api.get_trade_history(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_get24hr_stats_req(self):
        """
            get24hr_stats
            Get 24hr Stats
            /api/v1/trade-statistics
        """

        try:
            resp = self.api.get24hr_stats()
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e
