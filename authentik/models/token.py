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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, constr, validator
from authentik.models.intent_enum import IntentEnum
from authentik.models.user import User

class Token(BaseModel):
    """
    Token Serializer
    """
    pk: StrictStr = Field(...)
    managed: Optional[StrictStr] = Field(None, description="Objects that are managed by authentik. These objects are created and updated automatically. This flag only indicates that an object can be overwritten by migrations. You can still modify the objects via the API, but expect changes to be overwritten in a later update.")
    identifier: constr(strict=True, max_length=255) = Field(...)
    intent: Optional[IntentEnum] = None
    user: Optional[StrictInt] = None
    user_obj: User = Field(...)
    description: Optional[StrictStr] = None
    expires: Optional[datetime] = None
    expiring: Optional[StrictBool] = None
    __properties = ["pk", "managed", "identifier", "intent", "user", "user_obj", "description", "expires", "expiring"]

    @validator('identifier')
    def identifier_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[-a-zA-Z0-9_]+$", value):
            raise ValueError(r"must validate the regular expression /^[-a-zA-Z0-9_]+$/")
        return value

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
    def from_json(cls, json_str: str) -> Token:
        """Create an instance of Token from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "pk",
                            "user_obj",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of user_obj
        if self.user_obj:
            _dict['user_obj'] = self.user_obj.to_dict()
        # set to None if managed (nullable) is None
        # and __fields_set__ contains the field
        if self.managed is None and "managed" in self.__fields_set__:
            _dict['managed'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Token:
        """Create an instance of Token from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Token.parse_obj(obj)

        _obj = Token.parse_obj({
            "pk": obj.get("pk"),
            "managed": obj.get("managed"),
            "identifier": obj.get("identifier"),
            "intent": obj.get("intent"),
            "user": obj.get("user"),
            "user_obj": User.from_dict(obj.get("user_obj")) if obj.get("user_obj") is not None else None,
            "description": obj.get("description"),
            "expires": obj.get("expires"),
            "expiring": obj.get("expiring")
        })
        return _obj


