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

from datetime import datetime
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist, constr
from authentik.models.user_type_enum import UserTypeEnum

class PatchedUserRequest(BaseModel):
    """
    User Serializer
    """
    username: Optional[constr(strict=True, max_length=150, min_length=1)] = None
    name: Optional[StrictStr] = Field(None, description="User's display name.")
    is_active: Optional[StrictBool] = Field(None, description="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.")
    last_login: Optional[datetime] = None
    groups: Optional[conlist(StrictStr)] = None
    email: Optional[constr(strict=True, max_length=254)] = None
    attributes: Optional[Dict[str, Any]] = None
    path: Optional[constr(strict=True, min_length=1)] = None
    type: Optional[UserTypeEnum] = None
    __properties = ["username", "name", "is_active", "last_login", "groups", "email", "attributes", "path", "type"]

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
    def from_json(cls, json_str: str) -> PatchedUserRequest:
        """Create an instance of PatchedUserRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if last_login (nullable) is None
        # and __fields_set__ contains the field
        if self.last_login is None and "last_login" in self.__fields_set__:
            _dict['last_login'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PatchedUserRequest:
        """Create an instance of PatchedUserRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PatchedUserRequest.parse_obj(obj)

        _obj = PatchedUserRequest.parse_obj({
            "username": obj.get("username"),
            "name": obj.get("name"),
            "is_active": obj.get("is_active"),
            "last_login": obj.get("last_login"),
            "groups": obj.get("groups"),
            "email": obj.get("email"),
            "attributes": obj.get("attributes"),
            "path": obj.get("path"),
            "type": obj.get("type")
        })
        return _obj


