import os
import unittest

from kucoin_universal_sdk.api.client import DefaultClient
from kucoin_universal_sdk.extension.interceptor.logging import LoggingInterceptor
from kucoin_universal_sdk.generate.margin.market.model_get_cross_margin_symbols_req import \
    GetCrossMarginSymbolsReqBuilder
from kucoin_universal_sdk.generate.margin.market.model_get_etf_info_req import GetEtfInfoReqBuilder
from kucoin_universal_sdk.generate.margin.market.model_get_mark_price_detail_req import GetMarkPriceDetailReqBuilder
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
        self.api = kucoin_rest_api.get_margin_service().get_market_api()

    def test_get_isolated_margin_symbols_req(self):
        """
            get_isolated_margin_symbols
            Get Symbols - Isolated Margin
            /api/v1/isolated/symbols
        """

        try:
            resp = self.api.get_isolated_margin_symbols()
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_get_margin_config_req(self):
        """
            get_margin_config
            Get Margin Config
            /api/v1/margin/config
        """

        try:
            resp = self.api.get_margin_config()
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_get_mark_price_detail_req(self):
        """
            get_mark_price_detail
            Get Mark Price Detail
            /api/v1/mark-price/{symbol}/current
        """

        builder = GetMarkPriceDetailReqBuilder()
        builder.set_symbol("USDT-BTC")
        req = builder.build()
        try:
            resp = self.api.get_mark_price_detail(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_get_etf_info_req(self):
        """
            get_etf_info
            Get ETF Info
            /api/v3/etf/info
        """

        builder = GetEtfInfoReqBuilder()
        builder.set_currency("BTCUP")
        req = builder.build()
        try:
            resp = self.api.get_etf_info(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_get_cross_margin_symbols_req(self):
        """
            get_cross_margin_symbols
            Get Symbols - Cross Margin
            /api/v3/margin/symbols
        """

        builder = GetCrossMarginSymbolsReqBuilder()
        builder.set_symbol("BTC-USDT")
        req = builder.build()
        try:
            resp = self.api.get_cross_margin_symbols(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_get_mark_price_list_req(self):
        """
            get_mark_price_list
            Get Mark Price List
            /api/v3/mark-price/all-symbols
        """

        try:
            resp = self.api.get_mark_price_list()
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e
