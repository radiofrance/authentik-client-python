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


from typing import Optional
from pydantic import BaseModel, constr

class PatchedWebAuthnDeviceRequest(BaseModel):
    """
    Serializer for WebAuthn authenticator devices
    """
    name: Optional[constr(strict=True, max_length=200, min_length=1)] = None
    __properties = ["name"]

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
    def from_json(cls, json_str: str) -> PatchedWebAuthnDeviceRequest:
        """Create an instance of PatchedWebAuthnDeviceRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PatchedWebAuthnDeviceRequest:
        """Create an instance of PatchedWebAuthnDeviceRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PatchedWebAuthnDeviceRequest.parse_obj(obj)

        _obj = PatchedWebAuthnDeviceRequest.parse_obj({
            "name": obj.get("name")
        })
        return _obj


