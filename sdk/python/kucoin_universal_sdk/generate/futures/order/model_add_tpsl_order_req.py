# coding: utf-8

# Code generated by Kucoin Universal SDK Generator; DO NOT EDIT.

from __future__ import annotations
import pprint
import json

from enum import Enum
from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional


class AddTpslOrderReq(BaseModel):
    """
    AddTpslOrderReq

    Attributes:
        client_oid (str): Unique order id created by users to identify their orders, the maximum length cannot exceed 40, e.g. UUID, Only allows numbers, characters, underline(_), and separator(-)
        side (SideEnum): specify if the order is to 'buy' or 'sell'
        symbol (str): Symbol of the contract, Please refer to [Get Symbol endpoint: symbol](https://www.kucoin.com/docs-new/api-3470220) 
        leverage (int): Used to calculate the margin to be frozen for the order. If you are to close the position, this parameter is not required.
        type (TypeEnum): specify if the order is an 'limit' order or 'market' order
        remark (str): remark for the order, length cannot exceed 100 utf8 characters
        stop_price_type (StopPriceTypeEnum): Either 'TP', 'IP' or 'MP'
        reduce_only (bool): A mark to reduce the position size only. Set to false by default. Need to set the position size when reduceOnly is true. If set to true, only the orders reducing the position size will be executed. If the reduce-only order size exceeds the position size, the extra size will be canceled.
        close_order (bool): A mark to close the position. Set to false by default. If closeOrder is set to true, the system will close the position and the position size will become 0. Side, Size and Leverage fields can be left empty and the system will determine the side and size automatically.
        force_hold (bool): A mark to forcely hold the funds for an order, even though it's an order to reduce the position size. This helps the order stay on the order book and not get canceled when the position size changes. Set to false by default. The system will forcely freeze certain amount of funds for this order, including orders whose direction is opposite to the current positions. This feature is to ensure that the order won’t be canceled by the matching engine in such a circumstance that not enough funds are frozen for the order.
        stp (StpEnum): [Self Trade Prevention](https://www.kucoin.com/docs-new/doc-338146) is divided into these strategies: CN, CO, CB. Not supported DC at the moment.
        margin_mode (MarginModeEnum): Margin mode: ISOLATED, CROSS, default: ISOLATED
        price (str): Required for type is 'limit' order, indicating the operating price
        size (int): **Choose one of size, qty, valueQty**, Order size (Lot), must be a positive integer. The quantity unit of coin-swap contracts is size(lot), and other units are not supported.
        time_in_force (TimeInForceEnum): Optional for type is 'limit' order, [Time in force](https://www.kucoin.com/docs-new/doc-338146) is a special strategy used during trading, default is GTC
        post_only (bool): Optional for type is 'limit' order,  post only flag, invalid when timeInForce is IOC. When postOnly is true, not allowed choose hidden or iceberg. The post-only flag ensures that the trader always pays the maker fee and provides liquidity to the order book. If any part of the order is going to pay taker fee, the order will be fully rejected.
        hidden (bool): Optional for type is 'limit' order, orders not displaying in order book. When hidden chose, not allowed choose postOnly.
        iceberg (bool): Optional for type is 'limit' order, Only visible portion of the order is displayed in the order book. When iceberg chose, not allowed choose postOnly.
        visible_size (str): Optional for type is 'limit' order, The maximum visible size of an iceberg order. please place order in size (lots), The units of qty (base currency) and valueQty (value) are not supported.
        trigger_stop_up_price (str): Take profit price
        trigger_stop_down_price (str): Stop loss price
        qty (str): **Choose one of size, qty, valueQty**, Order size (Base currency) must be an integer multiple of the multiplier. The unit of the quantity of coin-swap is size(lot), which is not supported
        value_qty (str): **Choose one of size, qty, valueQty**, Order size (Value), USDS-Swap correspond to USDT or USDC. The unit of the quantity of coin-swap is size(lot), which is not supported
    """

    class SideEnum(Enum):
        """
        Attributes:
            BUY: 
            SELL: 
        """
        BUY = 'buy'
        SELL = 'sell'

    class TypeEnum(Enum):
        """
        Attributes:
            LIMIT: limit order
            MARKET: market order
        """
        LIMIT = 'limit'
        MARKET = 'market'

    class StopPriceTypeEnum(Enum):
        """
        Attributes:
            TRADE_PRICE: TP for trade price, The last trade price is the last price at which an order was filled. This price can be found in the latest match message.
            MARK_PRICE: MP for mark price, The mark price can be obtained through relevant OPEN API for index services
            INDEX_PRICE: IP for index price, The index price can be obtained through relevant OPEN API for index services
        """
        TRADE_PRICE = 'TP'
        MARK_PRICE = 'MP'
        INDEX_PRICE = 'IP'

    class StpEnum(Enum):
        """
        Attributes:
            CN: Cancel new, Cancel the new order
            CO: Cancel old, Cancel the old order
            CB: Cancel both, Cancel both sides
        """
        CN = 'CN'
        CO = 'CO'
        CB = 'CB'

    class MarginModeEnum(Enum):
        """
        Attributes:
            ISOLATED: 
            CROSS: 
        """
        ISOLATED = 'ISOLATED'
        CROSS = 'CROSS'

    class TimeInForceEnum(Enum):
        """
        Attributes:
            GOOD_TILL_CANCELED: order remains open on the order book until canceled. This is the default type if the field is left empty.
            IMMEDIATE_OR_CANCEL: being matched or not, the remaining size of the order will be instantly canceled instead of entering the order book.
        """
        GOOD_TILL_CANCELED = 'GTC'
        IMMEDIATE_OR_CANCEL = 'IOC'

    client_oid: Optional[str] = Field(
        default=None,
        description=
        "Unique order id created by users to identify their orders, the maximum length cannot exceed 40, e.g. UUID, Only allows numbers, characters, underline(_), and separator(-)",
        alias="clientOid")
    side: Optional[SideEnum] = Field(
        default=None, description="specify if the order is to 'buy' or 'sell'")
    symbol: Optional[str] = Field(
        default=None,
        description=
        "Symbol of the contract, Please refer to [Get Symbol endpoint: symbol](https://www.kucoin.com/docs-new/api-3470220) "
    )
    leverage: Optional[int] = Field(
        default=None,
        description=
        "Used to calculate the margin to be frozen for the order. If you are to close the position, this parameter is not required."
    )
    type: Optional[TypeEnum] = Field(
        default=TypeEnum.LIMIT,
        description="specify if the order is an 'limit' order or 'market' order"
    )
    remark: Optional[str] = Field(
        default=None,
        description=
        "remark for the order, length cannot exceed 100 utf8 characters")
    stop_price_type: Optional[StopPriceTypeEnum] = Field(
        default=None,
        description="Either 'TP', 'IP' or 'MP'",
        alias="stopPriceType")
    reduce_only: Optional[bool] = Field(
        default=False,
        description=
        "A mark to reduce the position size only. Set to false by default. Need to set the position size when reduceOnly is true. If set to true, only the orders reducing the position size will be executed. If the reduce-only order size exceeds the position size, the extra size will be canceled.",
        alias="reduceOnly")
    close_order: Optional[bool] = Field(
        default=False,
        description=
        "A mark to close the position. Set to false by default. If closeOrder is set to true, the system will close the position and the position size will become 0. Side, Size and Leverage fields can be left empty and the system will determine the side and size automatically.",
        alias="closeOrder")
    force_hold: Optional[bool] = Field(
        default=False,
        description=
        "A mark to forcely hold the funds for an order, even though it's an order to reduce the position size. This helps the order stay on the order book and not get canceled when the position size changes. Set to false by default. The system will forcely freeze certain amount of funds for this order, including orders whose direction is opposite to the current positions. This feature is to ensure that the order won’t be canceled by the matching engine in such a circumstance that not enough funds are frozen for the order.",
        alias="forceHold")
    stp: Optional[StpEnum] = Field(
        default=None,
        description=
        "[Self Trade Prevention](https://www.kucoin.com/docs-new/doc-338146) is divided into these strategies: CN, CO, CB. Not supported DC at the moment."
    )
    margin_mode: Optional[MarginModeEnum] = Field(
        default=MarginModeEnum.ISOLATED,
        description="Margin mode: ISOLATED, CROSS, default: ISOLATED",
        alias="marginMode")
    price: Optional[str] = Field(
        default=None,
        description=
        "Required for type is 'limit' order, indicating the operating price")
    size: Optional[int] = Field(
        default=None,
        description=
        "**Choose one of size, qty, valueQty**, Order size (Lot), must be a positive integer. The quantity unit of coin-swap contracts is size(lot), and other units are not supported."
    )
    time_in_force: Optional[TimeInForceEnum] = Field(
        default=TimeInForceEnum.GOOD_TILL_CANCELED,
        description=
        "Optional for type is 'limit' order, [Time in force](https://www.kucoin.com/docs-new/doc-338146) is a special strategy used during trading, default is GTC",
        alias="timeInForce")
    post_only: Optional[bool] = Field(
        default=False,
        description=
        "Optional for type is 'limit' order,  post only flag, invalid when timeInForce is IOC. When postOnly is true, not allowed choose hidden or iceberg. The post-only flag ensures that the trader always pays the maker fee and provides liquidity to the order book. If any part of the order is going to pay taker fee, the order will be fully rejected.",
        alias="postOnly")
    hidden: Optional[bool] = Field(
        default=False,
        description=
        "Optional for type is 'limit' order, orders not displaying in order book. When hidden chose, not allowed choose postOnly."
    )
    iceberg: Optional[bool] = Field(
        default=False,
        description=
        "Optional for type is 'limit' order, Only visible portion of the order is displayed in the order book. When iceberg chose, not allowed choose postOnly."
    )
    visible_size: Optional[str] = Field(
        default=None,
        description=
        "Optional for type is 'limit' order, The maximum visible size of an iceberg order. please place order in size (lots), The units of qty (base currency) and valueQty (value) are not supported.",
        alias="visibleSize")
    trigger_stop_up_price: Optional[str] = Field(
        default=None,
        description="Take profit price",
        alias="triggerStopUpPrice")
    trigger_stop_down_price: Optional[str] = Field(
        default=None,
        description="Stop loss price",
        alias="triggerStopDownPrice")
    qty: Optional[str] = Field(
        default=None,
        description=
        "**Choose one of size, qty, valueQty**, Order size (Base currency) must be an integer multiple of the multiplier. The unit of the quantity of coin-swap is size(lot), which is not supported"
    )
    value_qty: Optional[str] = Field(
        default=None,
        description=
        "**Choose one of size, qty, valueQty**, Order size (Value), USDS-Swap correspond to USDT or USDC. The unit of the quantity of coin-swap is size(lot), which is not supported",
        alias="valueQty")

    __properties: ClassVar[List[str]] = [
        "clientOid", "side", "symbol", "leverage", "type", "remark",
        "stopPriceType", "reduceOnly", "closeOrder", "forceHold", "stp",
        "marginMode", "price", "size", "timeInForce", "postOnly", "hidden",
        "iceberg", "visibleSize", "triggerStopUpPrice", "triggerStopDownPrice",
        "qty", "valueQty"
    ]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=False,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        return self.model_dump_json(by_alias=True, exclude_none=True)

    @classmethod
    def from_json(cls, json_str: str) -> Optional[AddTpslOrderReq]:
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        _dict = self.model_dump(
            by_alias=True,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str,
                                          Any]]) -> Optional[AddTpslOrderReq]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "clientOid":
            obj.get("clientOid"),
            "side":
            obj.get("side"),
            "symbol":
            obj.get("symbol"),
            "leverage":
            obj.get("leverage"),
            "type":
            obj.get("type")
            if obj.get("type") is not None else AddTpslOrderReq.TypeEnum.LIMIT,
            "remark":
            obj.get("remark"),
            "stopPriceType":
            obj.get("stopPriceType"),
            "reduceOnly":
            obj.get("reduceOnly")
            if obj.get("reduceOnly") is not None else False,
            "closeOrder":
            obj.get("closeOrder")
            if obj.get("closeOrder") is not None else False,
            "forceHold":
            obj.get("forceHold")
            if obj.get("forceHold") is not None else False,
            "stp":
            obj.get("stp"),
            "marginMode":
            obj.get("marginMode") if obj.get("marginMode") is not None else
            AddTpslOrderReq.MarginModeEnum.ISOLATED,
            "price":
            obj.get("price"),
            "size":
            obj.get("size"),
            "timeInForce":
            obj.get("timeInForce") if obj.get("timeInForce") is not None else
            AddTpslOrderReq.TimeInForceEnum.GOOD_TILL_CANCELED,
            "postOnly":
            obj.get("postOnly") if obj.get("postOnly") is not None else False,
            "hidden":
            obj.get("hidden") if obj.get("hidden") is not None else False,
            "iceberg":
            obj.get("iceberg") if obj.get("iceberg") is not None else False,
            "visibleSize":
            obj.get("visibleSize"),
            "triggerStopUpPrice":
            obj.get("triggerStopUpPrice"),
            "triggerStopDownPrice":
            obj.get("triggerStopDownPrice"),
            "qty":
            obj.get("qty"),
            "valueQty":
            obj.get("valueQty")
        })
        return _obj


class AddTpslOrderReqBuilder:

    def __init__(self):
        self.obj = {}

    def set_client_oid(self, value: str) -> AddTpslOrderReqBuilder:
        """
        Unique order id created by users to identify their orders, the maximum length cannot exceed 40, e.g. UUID, Only allows numbers, characters, underline(_), and separator(-)
        """
        self.obj['clientOid'] = value
        return self

    def set_side(self,
                 value: AddTpslOrderReq.SideEnum) -> AddTpslOrderReqBuilder:
        """
        specify if the order is to 'buy' or 'sell'
        """
        self.obj['side'] = value
        return self

    def set_symbol(self, value: str) -> AddTpslOrderReqBuilder:
        """
        Symbol of the contract, Please refer to [Get Symbol endpoint: symbol](https://www.kucoin.com/docs-new/api-3470220) 
        """
        self.obj['symbol'] = value
        return self

    def set_leverage(self, value: int) -> AddTpslOrderReqBuilder:
        """
        Used to calculate the margin to be frozen for the order. If you are to close the position, this parameter is not required.
        """
        self.obj['leverage'] = value
        return self

    def set_type(self,
                 value: AddTpslOrderReq.TypeEnum) -> AddTpslOrderReqBuilder:
        """
        specify if the order is an 'limit' order or 'market' order
        """
        self.obj['type'] = value
        return self

    def set_remark(self, value: str) -> AddTpslOrderReqBuilder:
        """
        remark for the order, length cannot exceed 100 utf8 characters
        """
        self.obj['remark'] = value
        return self

    def set_stop_price_type(
            self, value: AddTpslOrderReq.StopPriceTypeEnum
    ) -> AddTpslOrderReqBuilder:
        """
        Either 'TP', 'IP' or 'MP'
        """
        self.obj['stopPriceType'] = value
        return self

    def set_reduce_only(self, value: bool) -> AddTpslOrderReqBuilder:
        """
        A mark to reduce the position size only. Set to false by default. Need to set the position size when reduceOnly is true. If set to true, only the orders reducing the position size will be executed. If the reduce-only order size exceeds the position size, the extra size will be canceled.
        """
        self.obj['reduceOnly'] = value
        return self

    def set_close_order(self, value: bool) -> AddTpslOrderReqBuilder:
        """
        A mark to close the position. Set to false by default. If closeOrder is set to true, the system will close the position and the position size will become 0. Side, Size and Leverage fields can be left empty and the system will determine the side and size automatically.
        """
        self.obj['closeOrder'] = value
        return self

    def set_force_hold(self, value: bool) -> AddTpslOrderReqBuilder:
        """
        A mark to forcely hold the funds for an order, even though it's an order to reduce the position size. This helps the order stay on the order book and not get canceled when the position size changes. Set to false by default. The system will forcely freeze certain amount of funds for this order, including orders whose direction is opposite to the current positions. This feature is to ensure that the order won’t be canceled by the matching engine in such a circumstance that not enough funds are frozen for the order.
        """
        self.obj['forceHold'] = value
        return self

    def set_stp(self,
                value: AddTpslOrderReq.StpEnum) -> AddTpslOrderReqBuilder:
        """
        [Self Trade Prevention](https://www.kucoin.com/docs-new/doc-338146) is divided into these strategies: CN, CO, CB. Not supported DC at the moment.
        """
        self.obj['stp'] = value
        return self

    def set_margin_mode(
            self,
            value: AddTpslOrderReq.MarginModeEnum) -> AddTpslOrderReqBuilder:
        """
        Margin mode: ISOLATED, CROSS, default: ISOLATED
        """
        self.obj['marginMode'] = value
        return self

    def set_price(self, value: str) -> AddTpslOrderReqBuilder:
        """
        Required for type is 'limit' order, indicating the operating price
        """
        self.obj['price'] = value
        return self

    def set_size(self, value: int) -> AddTpslOrderReqBuilder:
        """
        **Choose one of size, qty, valueQty**, Order size (Lot), must be a positive integer. The quantity unit of coin-swap contracts is size(lot), and other units are not supported.
        """
        self.obj['size'] = value
        return self

    def set_time_in_force(
            self,
            value: AddTpslOrderReq.TimeInForceEnum) -> AddTpslOrderReqBuilder:
        """
        Optional for type is 'limit' order, [Time in force](https://www.kucoin.com/docs-new/doc-338146) is a special strategy used during trading, default is GTC
        """
        self.obj['timeInForce'] = value
        return self

    def set_post_only(self, value: bool) -> AddTpslOrderReqBuilder:
        """
        Optional for type is 'limit' order,  post only flag, invalid when timeInForce is IOC. When postOnly is true, not allowed choose hidden or iceberg. The post-only flag ensures that the trader always pays the maker fee and provides liquidity to the order book. If any part of the order is going to pay taker fee, the order will be fully rejected.
        """
        self.obj['postOnly'] = value
        return self

    def set_hidden(self, value: bool) -> AddTpslOrderReqBuilder:
        """
        Optional for type is 'limit' order, orders not displaying in order book. When hidden chose, not allowed choose postOnly.
        """
        self.obj['hidden'] = value
        return self

    def set_iceberg(self, value: bool) -> AddTpslOrderReqBuilder:
        """
        Optional for type is 'limit' order, Only visible portion of the order is displayed in the order book. When iceberg chose, not allowed choose postOnly.
        """
        self.obj['iceberg'] = value
        return self

    def set_visible_size(self, value: str) -> AddTpslOrderReqBuilder:
        """
        Optional for type is 'limit' order, The maximum visible size of an iceberg order. please place order in size (lots), The units of qty (base currency) and valueQty (value) are not supported.
        """
        self.obj['visibleSize'] = value
        return self

    def set_trigger_stop_up_price(self, value: str) -> AddTpslOrderReqBuilder:
        """
        Take profit price
        """
        self.obj['triggerStopUpPrice'] = value
        return self

    def set_trigger_stop_down_price(self,
                                    value: str) -> AddTpslOrderReqBuilder:
        """
        Stop loss price
        """
        self.obj['triggerStopDownPrice'] = value
        return self

    def set_qty(self, value: str) -> AddTpslOrderReqBuilder:
        """
        **Choose one of size, qty, valueQty**, Order size (Base currency) must be an integer multiple of the multiplier. The unit of the quantity of coin-swap is size(lot), which is not supported
        """
        self.obj['qty'] = value
        return self

    def set_value_qty(self, value: str) -> AddTpslOrderReqBuilder:
        """
        **Choose one of size, qty, valueQty**, Order size (Value), USDS-Swap correspond to USDT or USDC. The unit of the quantity of coin-swap is size(lot), which is not supported
        """
        self.obj['valueQty'] = value
        return self

    def build(self) -> AddTpslOrderReq:
        return AddTpslOrderReq(**self.obj)
