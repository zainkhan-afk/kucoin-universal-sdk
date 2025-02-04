# coding: utf-8

# Code generated by Kucoin Universal SDK Generator; DO NOT EDIT.

from __future__ import annotations
import pprint
import json

from enum import Enum
from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional


class GetOpenOrdersReq(BaseModel):
    """
    GetOpenOrdersReq

    Attributes:
        symbol (str): symbol
        trade_type (TradeTypeEnum): Order type: MARGIN_TRADE - cross margin trading order, MARGIN_ISOLATED_TRADE - isolated margin trading order
    """

    class TradeTypeEnum(Enum):
        """
        Attributes:
            MARGIN_TRADE: 
            MARGIN_ISOLATED_TRADE: 
        """
        MARGIN_TRADE = 'MARGIN_TRADE'
        MARGIN_ISOLATED_TRADE = 'MARGIN_ISOLATED_TRADE'

    symbol: Optional[str] = Field(default=None, description="symbol")
    trade_type: Optional[TradeTypeEnum] = Field(
        default=None,
        description=
        "Order type: MARGIN_TRADE - cross margin trading order, MARGIN_ISOLATED_TRADE - isolated margin trading order",
        alias="tradeType")

    __properties: ClassVar[List[str]] = ["symbol", "tradeType"]

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
    def from_json(cls, json_str: str) -> Optional[GetOpenOrdersReq]:
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        _dict = self.model_dump(
            by_alias=True,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str,
                                          Any]]) -> Optional[GetOpenOrdersReq]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "symbol": obj.get("symbol"),
            "tradeType": obj.get("tradeType")
        })
        return _obj


class GetOpenOrdersReqBuilder:

    def __init__(self):
        self.obj = {}

    def set_symbol(self, value: str) -> GetOpenOrdersReqBuilder:
        """
        symbol
        """
        self.obj['symbol'] = value
        return self

    def set_trade_type(
            self,
            value: GetOpenOrdersReq.TradeTypeEnum) -> GetOpenOrdersReqBuilder:
        """
        Order type: MARGIN_TRADE - cross margin trading order, MARGIN_ISOLATED_TRADE - isolated margin trading order
        """
        self.obj['tradeType'] = value
        return self

    def build(self) -> GetOpenOrdersReq:
        return GetOpenOrdersReq(**self.obj)
