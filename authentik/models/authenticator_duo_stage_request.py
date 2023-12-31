# coding: utf-8

"""
    authentik

    Making authentication simple.

    The version of the OpenAPI document: 2023.6.1
    Contact: hello@goauthentik.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist, constr
from authentik.models.flow_set_request import FlowSetRequest

class AuthenticatorDuoStageRequest(BaseModel):
    """
    AuthenticatorDuoStage Serializer
    """
    name: constr(strict=True, min_length=1) = Field(...)
    flow_set: Optional[conlist(FlowSetRequest)] = None
    configure_flow: Optional[StrictStr] = Field(None, description="Flow used by an authenticated user to configure this Stage. If empty, user will not be able to configure this stage.")
    friendly_name: Optional[constr(strict=True, min_length=1)] = None
    client_id: constr(strict=True, min_length=1) = Field(...)
    client_secret: constr(strict=True, min_length=1) = Field(...)
    api_hostname: constr(strict=True, min_length=1) = Field(...)
    admin_integration_key: Optional[StrictStr] = None
    admin_secret_key: Optional[StrictStr] = None
    __properties = ["name", "flow_set", "configure_flow", "friendly_name", "client_id", "client_secret", "api_hostname", "admin_integration_key", "admin_secret_key"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> AuthenticatorDuoStageRequest:
        """Create an instance of AuthenticatorDuoStageRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in flow_set (list)
        _items = []
        if self.flow_set:
            for _item in self.flow_set:
                if _item:
                    _items.append(_item.to_dict())
            _dict['flow_set'] = _items
        # set to None if configure_flow (nullable) is None
        # and __fields_set__ contains the field
        if self.configure_flow is None and "configure_flow" in self.__fields_set__:
            _dict['configure_flow'] = None

        # set to None if friendly_name (nullable) is None
        # and __fields_set__ contains the field
        if self.friendly_name is None and "friendly_name" in self.__fields_set__:
            _dict['friendly_name'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AuthenticatorDuoStageRequest:
        """Create an instance of AuthenticatorDuoStageRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AuthenticatorDuoStageRequest.parse_obj(obj)

        _obj = AuthenticatorDuoStageRequest.parse_obj({
            "name": obj.get("name"),
            "flow_set": [FlowSetRequest.from_dict(_item) for _item in obj.get("flow_set")] if obj.get("flow_set") is not None else None,
            "configure_flow": obj.get("configure_flow"),
            "friendly_name": obj.get("friendly_name"),
            "client_id": obj.get("client_id"),
            "client_secret": obj.get("client_secret"),
            "api_hostname": obj.get("api_hostname"),
            "admin_integration_key": obj.get("admin_integration_key"),
            "admin_secret_key": obj.get("admin_secret_key")
        })
        return _obj


