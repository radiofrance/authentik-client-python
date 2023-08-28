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
from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr
from authentik.models.application import Application
from authentik.models.user import User

class UserConsent(BaseModel):
    """
    UserConsent Serializer
    """
    pk: StrictInt = Field(...)
    expires: Optional[datetime] = None
    user: User = Field(...)
    application: Application = Field(...)
    permissions: Optional[StrictStr] = ''
    __properties = ["pk", "expires", "user", "application", "permissions"]

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
    def from_json(cls, json_str: str) -> UserConsent:
        """Create an instance of UserConsent from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "pk",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        # override the default output from pydantic by calling `to_dict()` of application
        if self.application:
            _dict['application'] = self.application.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UserConsent:
        """Create an instance of UserConsent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UserConsent.parse_obj(obj)

        _obj = UserConsent.parse_obj({
            "pk": obj.get("pk"),
            "expires": obj.get("expires"),
            "user": User.from_dict(obj.get("user")) if obj.get("user") is not None else None,
            "application": Application.from_dict(obj.get("application")) if obj.get("application") is not None else None,
            "permissions": obj.get("permissions") if obj.get("permissions") is not None else ''
        })
        return _obj

