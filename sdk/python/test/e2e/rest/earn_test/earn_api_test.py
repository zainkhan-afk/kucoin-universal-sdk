import os
import unittest

from kucoin_universal_sdk.api.client import DefaultClient
from kucoin_universal_sdk.extension.interceptor.logging import LoggingInterceptor
from kucoin_universal_sdk.generate.earn.earn.model_get_account_holding_req import GetAccountHoldingReqBuilder, \
    GetAccountHoldingReq
from kucoin_universal_sdk.generate.earn.earn.model_get_eth_staking_products_req import GetEthStakingProductsReqBuilder
from kucoin_universal_sdk.generate.earn.earn.model_get_kcs_staking_products_req import GetKcsStakingProductsReqBuilder
from kucoin_universal_sdk.generate.earn.earn.model_get_promotion_products_req import GetPromotionProductsReqBuilder
from kucoin_universal_sdk.generate.earn.earn.model_get_redeem_preview_req import GetRedeemPreviewReqBuilder, \
    GetRedeemPreviewReq
from kucoin_universal_sdk.generate.earn.earn.model_get_savings_products_req import GetSavingsProductsReqBuilder
from kucoin_universal_sdk.generate.earn.earn.model_get_staking_products_req import GetStakingProductsReqBuilder
from kucoin_universal_sdk.generate.earn.earn.model_purchase_req import PurchaseReqBuilder, PurchaseReq
from kucoin_universal_sdk.generate.earn.earn.model_redeem_req import RedeemReqBuilder, RedeemReq
from kucoin_universal_sdk.model.client_option import ClientOptionBuilder
from kucoin_universal_sdk.model.constants import GLOBAL_API_ENDPOINT, GLOBAL_BROKER_API_ENDPOINT, \
    GLOBAL_FUTURES_API_ENDPOINT
from kucoin_universal_sdk.model.transport_option import TransportOptionBuilder


class EarnApiTest(unittest.TestCase):
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
        self.api = kucoin_rest_api.get_earn_service().get_earn_api()

    def test_get_eth_staking_products_req(self):
        """
            get_eth_staking_products
            Get ETH Staking Products
            /api/v1/earn/eth-staking/products
        """

        builder = GetEthStakingProductsReqBuilder()
        builder.set_currency("ETH")
        req = builder.build()
        try:
            resp = self.api.get_eth_staking_products(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_get_account_holding_req(self):
        """
            get_account_holding
            Get Account Holding
            /api/v1/earn/hold-assets
        """

        builder = GetAccountHoldingReqBuilder()
        builder.set_currency("USDT").set_product_category(
            GetAccountHoldingReq.ProductCategoryEnum.DEMAND).set_product_id("2152")
        req = builder.build()
        try:
            resp = self.api.get_account_holding(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_get_kcs_staking_products_req(self):
        """
            get_kcs_staking_products
            Get KCS Staking Products
            /api/v1/earn/kcs-staking/products
        """

        builder = GetKcsStakingProductsReqBuilder()
        builder.set_currency("KCS")
        req = builder.build()
        try:
            resp = self.api.get_kcs_staking_products(req)
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
            /api/v1/earn/orders
        """

        builder = RedeemReqBuilder()
        builder.set_order_id("2849600").set_amount("10.0").set_from_account_type(
            RedeemReq.FromAccountTypeEnum.MAIN).set_confirm_punish_redeem("1")
        req = builder.build()
        try:
            resp = self.api.redeem(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_purchase_req(self):
        """
            purchase
            purchase
            /api/v1/earn/orders
        """

        builder = PurchaseReqBuilder()
        builder.set_product_id("2152").set_amount("10.0").set_account_type(PurchaseReq.AccountTypeEnum.MAIN)
        req = builder.build()
        try:
            resp = self.api.purchase(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_get_promotion_products_req(self):
        """
            get_promotion_products
            Get Promotion Products
            /api/v1/earn/promotion/products
        """

        builder = GetPromotionProductsReqBuilder()
        builder.set_currency("USDT")
        req = builder.build()
        try:
            resp = self.api.get_promotion_products(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_get_redeem_preview_req(self):
        """
            get_redeem_preview
            Get Redeem Preview
            /api/v1/earn/redeem-preview
        """

        builder = GetRedeemPreviewReqBuilder()
        builder.set_order_id("2849600").set_from_account_type(GetRedeemPreviewReq.FromAccountTypeEnum.MAIN)
        req = builder.build()
        try:
            resp = self.api.get_redeem_preview(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_get_savings_products_req(self):
        """
            get_savings_products
            Get Savings Products
            /api/v1/earn/saving/products
        """

        builder = GetSavingsProductsReqBuilder()
        builder.set_currency("USDT")
        req = builder.build()
        try:
            resp = self.api.get_savings_products(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_get_staking_products_req(self):
        """
            get_staking_products
            Get Staking Products
            /api/v1/earn/staking/products
        """

        builder = GetStakingProductsReqBuilder()
        builder.set_currency("ATOM")
        req = builder.build()
        try:
            resp = self.api.get_staking_products(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e
