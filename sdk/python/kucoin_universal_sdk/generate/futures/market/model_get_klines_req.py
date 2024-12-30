# coding: utf-8

# Code generated by Kucoin Universal SDK Generator; DO NOT EDIT.

from __future__ import annotations
import pprint
import json

from enum import Enum
from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional


class GetKlinesReq(BaseModel):
    """
    GetKlinesReq

    Attributes:
        symbol (str): Symbol of the contract, Please refer to [Get Symbol endpoint: symbol, indexSymbol, premiumsSymbol1M, premiumsSymbol8H](https://www.kucoin.com/docs-new/api-3470220) 
        granularity (GranularityEnum): Type of candlestick patterns(minute)
        from_ (int): Start time (milisecond)
        to (int): End time (milisecond)
    """

    class GranularityEnum(Enum):
        """
        Attributes:
            T_1: 1min
            T_5: 5min
            T_15: 15min
            T_30: 30min
            T_60: 1hour
            T_120: 2hour
            T_240: 4hour
            T_480: 8hour
            T_720: 12hour
            T_1440: 1day
            T_10080: 1week
        """
        T_1 = 1
        T_5 = 5
        T_15 = 15
        T_30 = 30
        T_60 = 60
        T_120 = 120
        T_240 = 240
        T_480 = 480
        T_720 = 720
        T_1440 = 1440
        T_10080 = 10080

    symbol: Optional[str] = Field(
        default=None,
        description=
        "Symbol of the contract, Please refer to [Get Symbol endpoint: symbol, indexSymbol, premiumsSymbol1M, premiumsSymbol8H](https://www.kucoin.com/docs-new/api-3470220) "
    )
    granularity: Optional[GranularityEnum] = Field(
        default=None, description="Type of candlestick patterns(minute)")
    from_: Optional[int] = Field(default=None,
                                 description="Start time (milisecond)",
                                 alias="from")
    to: Optional[int] = Field(default=None,
                              description="End time (milisecond)")

    __properties: ClassVar[List[str]] = ["symbol", "granularity", "from", "to"]

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
    def from_json(cls, json_str: str) -> Optional[GetKlinesReq]:
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        _dict = self.model_dump(
            by_alias=True,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str,
                                          Any]]) -> Optional[GetKlinesReq]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "symbol": obj.get("symbol"),
            "granularity": obj.get("granularity"),
            "from": obj.get("from"),
            "to": obj.get("to")
        })
        return _obj


class GetKlinesReqBuilder:

    def __init__(self):
        self.obj = {}

    def set_symbol(self, value: str) -> GetKlinesReqBuilder:
        """
        Symbol of the contract, Please refer to [Get Symbol endpoint: symbol, indexSymbol, premiumsSymbol1M, premiumsSymbol8H](https://www.kucoin.com/docs-new/api-3470220) 
        """
        self.obj['symbol'] = value
        return self

    def set_granularity(
            self, value: GetKlinesReq.GranularityEnum) -> GetKlinesReqBuilder:
        """
        Type of candlestick patterns(minute)
        """
        self.obj['granularity'] = value
        return self

    def set_from_(self, value: int) -> GetKlinesReqBuilder:
        """
        Start time (milisecond)
        """
        self.obj['from'] = value
        return self

    def set_to(self, value: int) -> GetKlinesReqBuilder:
        """
        End time (milisecond)
        """
        self.obj['to'] = value
        return self

    def build(self) -> GetKlinesReq:
        return GetKlinesReq(**self.obj)
