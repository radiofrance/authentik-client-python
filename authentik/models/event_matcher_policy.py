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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr
from authentik.models.app_enum import AppEnum
from authentik.models.event_actions import EventActions
from authentik.models.model_enum import ModelEnum

class EventMatcherPolicy(BaseModel):
    """
    Event Matcher Policy Serializer
    """
    pk: StrictStr = Field(...)
    name: StrictStr = Field(...)
    execution_logging: Optional[StrictBool] = Field(None, description="When this option is enabled, all executions of this policy will be logged. By default, only execution errors are logged.")
    component: StrictStr = Field(..., description="Get object component so that we know how to edit the object")
    verbose_name: StrictStr = Field(..., description="Return object's verbose_name")
    verbose_name_plural: StrictStr = Field(..., description="Return object's plural verbose_name")
    meta_model_name: StrictStr = Field(..., description="Return internal model name")
    bound_to: StrictInt = Field(..., description="Return objects policy is bound to")
    action: Optional[EventActions] = None
    client_ip: Optional[StrictStr] = Field(None, description="Matches Event's Client IP (strict matching, for network matching use an Expression Policy)")
    app: Optional[AppEnum] = None
    model: Optional[ModelEnum] = None
    __properties = ["pk", "name", "execution_logging", "component", "verbose_name", "verbose_name_plural", "meta_model_name", "bound_to", "action", "client_ip", "app", "model"]

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
    def from_json(cls, json_str: str) -> EventMatcherPolicy:
        """Create an instance of EventMatcherPolicy from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "pk",
                            "component",
                            "verbose_name",
                            "verbose_name_plural",
                            "meta_model_name",
                            "bound_to",
                          },
                          exclude_none=True)
        # set to None if action (nullable) is None
        # and __fields_set__ contains the field
        if self.action is None and "action" in self.__fields_set__:
            _dict['action'] = None

        # set to None if client_ip (nullable) is None
        # and __fields_set__ contains the field
        if self.client_ip is None and "client_ip" in self.__fields_set__:
            _dict['client_ip'] = None

        # set to None if app (nullable) is None
        # and __fields_set__ contains the field
        if self.app is None and "app" in self.__fields_set__:
            _dict['app'] = None

        # set to None if model (nullable) is None
        # and __fields_set__ contains the field
        if self.model is None and "model" in self.__fields_set__:
            _dict['model'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EventMatcherPolicy:
        """Create an instance of EventMatcherPolicy from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EventMatcherPolicy.parse_obj(obj)

        _obj = EventMatcherPolicy.parse_obj({
            "pk": obj.get("pk"),
            "name": obj.get("name"),
            "execution_logging": obj.get("execution_logging"),
            "component": obj.get("component"),
            "verbose_name": obj.get("verbose_name"),
            "verbose_name_plural": obj.get("verbose_name_plural"),
            "meta_model_name": obj.get("meta_model_name"),
            "bound_to": obj.get("bound_to"),
            "action": obj.get("action"),
            "client_ip": obj.get("client_ip"),
            "app": obj.get("app"),
            "model": obj.get("model")
        })
        return _obj


