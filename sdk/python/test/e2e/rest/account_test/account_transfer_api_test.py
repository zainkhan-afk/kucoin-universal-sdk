import os
import unittest
import uuid

from kucoin_universal_sdk.api.client import DefaultClient
from kucoin_universal_sdk.extension.interceptor.logging import LoggingInterceptor
from kucoin_universal_sdk.generate.account.transfer.model_flex_transfer_req import FlexTransferReqBuilder, \
    FlexTransferReq
from kucoin_universal_sdk.generate.account.transfer.model_futures_account_transfer_in_req import \
    FuturesAccountTransferInReqBuilder, FuturesAccountTransferInReq
from kucoin_universal_sdk.generate.account.transfer.model_futures_account_transfer_out_req import \
    FuturesAccountTransferOutReqBuilder, FuturesAccountTransferOutReq
from kucoin_universal_sdk.generate.account.transfer.model_get_futures_account_transfer_out_ledger_req import \
    GetFuturesAccountTransferOutLedgerReqBuilder
from kucoin_universal_sdk.generate.account.transfer.model_get_transfer_quotas_req import GetTransferQuotasReqBuilder, \
    GetTransferQuotasReq
from kucoin_universal_sdk.generate.account.transfer.model_inner_transfer_req import InnerTransferReqBuilder, \
    InnerTransferReq
from kucoin_universal_sdk.generate.account.transfer.model_sub_account_transfer_req import SubAccountTransferReqBuilder, \
    SubAccountTransferReq
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
        self.api = kucoin_rest_api.get_account_service().get_transfer_api()

    def test_get_transfer_quotas_req(self):
        """
            get_transfer_quotas
            Get Transfer Quotas
            /api/v1/accounts/transferable
        """

        builder = GetTransferQuotasReqBuilder()
        builder.set_currency("USDT").set_type(GetTransferQuotasReq.TypeEnum.MAIN)
        req = builder.build()
        try:
            resp = self.api.get_transfer_quotas(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_futures_account_transfer_in_req(self):
        """
            futures_account_transfer_in
            Futures Account Transfer In
            /api/v1/transfer-in
        """

        builder = FuturesAccountTransferInReqBuilder()
        builder.set_currency("USDT").set_amount(1.0).set_pay_account_type(
            FuturesAccountTransferInReq.PayAccountTypeEnum.MAIN)
        req = builder.build()
        try:
            resp = self.api.futures_account_transfer_in(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_get_futures_account_transfer_out_ledger_req(self):
        """
            get_futures_account_transfer_out_ledger
            Get Futures Account Transfer Out Ledger
            /api/v1/transfer-list
        """

        builder = GetFuturesAccountTransferOutLedgerReqBuilder()
        builder.set_currency("USDT").set_start_at(1669478400000).set_end_at(1669564800000)
        req = builder.build()
        try:
            resp = self.api.get_futures_account_transfer_out_ledger(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_inner_transfer_req(self):
        """
            inner_transfer
            Inner Transfer
            /api/v2/accounts/inner-transfer
        """

        builder = InnerTransferReqBuilder()
        builder.set_client_oid(uuid.uuid4().__str__()).set_currency("USDT").set_amount("10").set_to(
            InnerTransferReq.ToEnum.TRADE).set_from_(InnerTransferReq.FromEnum.MAIN)
        req = builder.build()
        try:
            resp = self.api.inner_transfer(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_sub_account_transfer_req(self):
        """
            sub_account_transfer
            SubAccount Transfer
            /api/v2/accounts/sub-transfer
        """

        builder = SubAccountTransferReqBuilder()
        builder.set_client_oid(uuid.uuid4().__str__()).set_currency("USDT").set_amount("10.0").set_direction(
            SubAccountTransferReq.DirectionEnum.OUT).set_account_type(
            SubAccountTransferReq.AccountTypeEnum.MAIN).set_sub_account_type(
            SubAccountTransferReq.SubAccountTypeEnum.MAIN).set_sub_user_id("6744227ce235b300012232d6")
        req = builder.build()
        try:
            resp = self.api.sub_account_transfer(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_flex_transfer_req(self):
        """
            flex_transfer
            Flex Transfer
            /api/v3/accounts/universal-transfer
        """

        builder = FlexTransferReqBuilder()
        builder.set_client_oid(uuid.uuid4().__str__()).set_currency("USDT").set_amount(
            "1").set_from_user_id("6744227ce235b300012232d6").set_from_account_type(
            FlexTransferReq.FromAccountTypeEnum.MAIN).set_type(
            FlexTransferReq.TypeEnum.INTERNAL).set_to_user_id("6744227ce235b300012232d6").set_to_account_type(
            FlexTransferReq.ToAccountTypeEnum.TRADE)
        req = builder.build()
        try:
            resp = self.api.flex_transfer(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e

    def test_futures_account_transfer_out_req(self):
        """
            futures_account_transfer_out
            Futures Account Transfer Out
            /api/v3/transfer-out
        """
        builder = FuturesAccountTransferOutReqBuilder()
        builder.set_currency("USDT").set_amount(1).set_rec_account_type(
            FuturesAccountTransferOutReq.RecAccountTypeEnum.MAIN)
        req = builder.build()
        try:
            resp = self.api.futures_account_transfer_out(req)
            print("code: ", resp.common_response.code)
            print("msg: ", resp.common_response.message)
            print("data: ", resp.to_json())
        except Exception as e:
            print("error: ", e)
            raise e
