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
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist
from authentik.models.flow_set import FlowSet

class UserLoginStage(BaseModel):
    """
    UserLoginStage Serializer
    """
    pk: StrictStr = Field(...)
    name: StrictStr = Field(...)
    component: StrictStr = Field(..., description="Get object type so that we know how to edit the object")
    verbose_name: StrictStr = Field(..., description="Return object's verbose_name")
    verbose_name_plural: StrictStr = Field(..., description="Return object's plural verbose_name")
    meta_model_name: StrictStr = Field(..., description="Return internal model name")
    flow_set: Optional[conlist(FlowSet)] = None
    session_duration: Optional[StrictStr] = Field(None, description="Determines how long a session lasts. Default of 0 means that the sessions lasts until the browser is closed. (Format: hours=-1;minutes=-2;seconds=-3)")
    terminate_other_sessions: Optional[StrictBool] = Field(None, description="Terminate all other sessions of the user logging in.")
    remember_me_offset: Optional[StrictStr] = Field(None, description="Offset the session will be extended by when the user picks the remember me option. Default of 0 means that the remember me option will not be shown. (Format: hours=-1;minutes=-2;seconds=-3)")
    __properties = ["pk", "name", "component", "verbose_name", "verbose_name_plural", "meta_model_name", "flow_set", "session_duration", "terminate_other_sessions", "remember_me_offset"]

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
    def from_json(cls, json_str: str) -> UserLoginStage:
        """Create an instance of UserLoginStage from a JSON string"""
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
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in flow_set (list)
        _items = []
        if self.flow_set:
            for _item in self.flow_set:
                if _item:
                    _items.append(_item.to_dict())
            _dict['flow_set'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UserLoginStage:
        """Create an instance of UserLoginStage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UserLoginStage.parse_obj(obj)

        _obj = UserLoginStage.parse_obj({
            "pk": obj.get("pk"),
            "name": obj.get("name"),
            "component": obj.get("component"),
            "verbose_name": obj.get("verbose_name"),
            "verbose_name_plural": obj.get("verbose_name_plural"),
            "meta_model_name": obj.get("meta_model_name"),
            "flow_set": [FlowSet.from_dict(_item) for _item in obj.get("flow_set")] if obj.get("flow_set") is not None else None,
            "session_duration": obj.get("session_duration"),
            "terminate_other_sessions": obj.get("terminate_other_sessions"),
            "remember_me_offset": obj.get("remember_me_offset")
        })
        return _obj

