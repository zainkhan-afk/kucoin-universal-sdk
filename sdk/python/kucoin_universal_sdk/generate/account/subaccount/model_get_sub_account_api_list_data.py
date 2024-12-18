# coding: utf-8

# Code generated by Kucoin Universal SDK Generator; DO NOT EDIT.

from __future__ import annotations
import pprint
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional


class GetSubAccountApiListData(BaseModel):
    """
    GetSubAccountApiListData

    Attributes:
        sub_name (str): Sub Name
        remark (str): Remarks
        api_key (str): API Key
        api_version (int): API Version
        permission (str): [Permissions](doc://link/pages/338144)
        ip_whitelist (str): IP whitelist
        created_at (int): Apikey create time
        uid (int): Sub-account UID
        is_master (bool): Whether it is the master account.
    """

    sub_name: Optional[str] = Field(default=None,
                                    description="Sub Name",
                                    alias="subName")
    remark: Optional[str] = Field(default=None, description="Remarks")
    api_key: Optional[str] = Field(default=None,
                                   description="API Key",
                                   alias="apiKey")
    api_version: Optional[int] = Field(default=None,
                                       description="API Version",
                                       alias="apiVersion")
    permission: Optional[str] = Field(
        default=None, description="[Permissions](doc://link/pages/338144)")
    ip_whitelist: Optional[str] = Field(default=None,
                                        description="IP whitelist",
                                        alias="ipWhitelist")
    created_at: Optional[int] = Field(default=None,
                                      description="Apikey create time",
                                      alias="createdAt")
    uid: Optional[int] = Field(default=None, description="Sub-account UID")
    is_master: Optional[bool] = Field(
        default=None,
        description="Whether it is the master account.",
        alias="isMaster")

    __properties: ClassVar[List[str]] = [
        "subName", "remark", "apiKey", "apiVersion", "permission",
        "ipWhitelist", "createdAt", "uid", "isMaster"
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
    def from_json(cls, json_str: str) -> Optional[GetSubAccountApiListData]:
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        _dict = self.model_dump(
            by_alias=True,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(
            cls,
            obj: Optional[Dict[str,
                               Any]]) -> Optional[GetSubAccountApiListData]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "subName": obj.get("subName"),
            "remark": obj.get("remark"),
            "apiKey": obj.get("apiKey"),
            "apiVersion": obj.get("apiVersion"),
            "permission": obj.get("permission"),
            "ipWhitelist": obj.get("ipWhitelist"),
            "createdAt": obj.get("createdAt"),
            "uid": obj.get("uid"),
            "isMaster": obj.get("isMaster")
        })
        return _obj
