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
from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, constr
from authentik.models.event_actions import EventActions

class EventRequest(BaseModel):
    """
    Event Serializer
    """
    user: Optional[Dict[str, Any]] = None
    action: EventActions = Field(...)
    app: constr(strict=True, min_length=1) = Field(...)
    context: Optional[Dict[str, Any]] = None
    client_ip: Optional[constr(strict=True, min_length=1)] = None
    expires: Optional[datetime] = None
    tenant: Optional[Dict[str, Any]] = None
    __properties = ["user", "action", "app", "context", "client_ip", "expires", "tenant"]

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
    def from_json(cls, json_str: str) -> EventRequest:
        """Create an instance of EventRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if client_ip (nullable) is None
        # and __fields_set__ contains the field
        if self.client_ip is None and "client_ip" in self.__fields_set__:
            _dict['client_ip'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EventRequest:
        """Create an instance of EventRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EventRequest.parse_obj(obj)

        _obj = EventRequest.parse_obj({
            "user": obj.get("user"),
            "action": obj.get("action"),
            "app": obj.get("app"),
            "context": obj.get("context"),
            "client_ip": obj.get("client_ip"),
            "expires": obj.get("expires"),
            "tenant": obj.get("tenant")
        })
        return _obj

