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
from pydantic import BaseModel, Field, StrictBool, StrictStr, constr
from authentik.models.notification_transport_mode_enum import NotificationTransportModeEnum

class NotificationTransportRequest(BaseModel):
    """
    NotificationTransport Serializer
    """
    name: constr(strict=True, min_length=1) = Field(...)
    mode: Optional[NotificationTransportModeEnum] = None
    webhook_url: Optional[StrictStr] = None
    webhook_mapping: Optional[StrictStr] = None
    send_once: Optional[StrictBool] = Field(None, description="Only send notification once, for example when sending a webhook into a chat channel.")
    __properties = ["name", "mode", "webhook_url", "webhook_mapping", "send_once"]

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
    def from_json(cls, json_str: str) -> NotificationTransportRequest:
        """Create an instance of NotificationTransportRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if webhook_mapping (nullable) is None
        # and __fields_set__ contains the field
        if self.webhook_mapping is None and "webhook_mapping" in self.__fields_set__:
            _dict['webhook_mapping'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> NotificationTransportRequest:
        """Create an instance of NotificationTransportRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return NotificationTransportRequest.parse_obj(obj)

        _obj = NotificationTransportRequest.parse_obj({
            "name": obj.get("name"),
            "mode": obj.get("mode"),
            "webhook_url": obj.get("webhook_url"),
            "webhook_mapping": obj.get("webhook_mapping"),
            "send_once": obj.get("send_once")
        })
        return _obj

