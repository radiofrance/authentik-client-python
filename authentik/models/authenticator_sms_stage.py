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
from authentik.models.auth_type_enum import AuthTypeEnum
from authentik.models.flow_set import FlowSet
from authentik.models.provider_enum import ProviderEnum

class AuthenticatorSMSStage(BaseModel):
    """
    AuthenticatorSMSStage Serializer
    """
    pk: StrictStr = Field(...)
    name: StrictStr = Field(...)
    component: StrictStr = Field(..., description="Get object type so that we know how to edit the object")
    verbose_name: StrictStr = Field(..., description="Return object's verbose_name")
    verbose_name_plural: StrictStr = Field(..., description="Return object's plural verbose_name")
    meta_model_name: StrictStr = Field(..., description="Return internal model name")
    flow_set: Optional[conlist(FlowSet)] = None
    configure_flow: Optional[StrictStr] = Field(None, description="Flow used by an authenticated user to configure this Stage. If empty, user will not be able to configure this stage.")
    friendly_name: Optional[StrictStr] = None
    provider: ProviderEnum = Field(...)
    from_number: StrictStr = Field(...)
    account_sid: StrictStr = Field(...)
    auth: StrictStr = Field(...)
    auth_password: Optional[StrictStr] = None
    auth_type: Optional[AuthTypeEnum] = None
    verify_only: Optional[StrictBool] = Field(None, description="When enabled, the Phone number is only used during enrollment to verify the users authenticity. Only a hash of the phone number is saved to ensure it is not re-used in the future.")
    mapping: Optional[StrictStr] = Field(None, description="Optionally modify the payload being sent to custom providers.")
    __properties = ["pk", "name", "component", "verbose_name", "verbose_name_plural", "meta_model_name", "flow_set", "configure_flow", "friendly_name", "provider", "from_number", "account_sid", "auth", "auth_password", "auth_type", "verify_only", "mapping"]

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
    def from_json(cls, json_str: str) -> AuthenticatorSMSStage:
        """Create an instance of AuthenticatorSMSStage from a JSON string"""
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
        # set to None if configure_flow (nullable) is None
        # and __fields_set__ contains the field
        if self.configure_flow is None and "configure_flow" in self.__fields_set__:
            _dict['configure_flow'] = None

        # set to None if friendly_name (nullable) is None
        # and __fields_set__ contains the field
        if self.friendly_name is None and "friendly_name" in self.__fields_set__:
            _dict['friendly_name'] = None

        # set to None if mapping (nullable) is None
        # and __fields_set__ contains the field
        if self.mapping is None and "mapping" in self.__fields_set__:
            _dict['mapping'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AuthenticatorSMSStage:
        """Create an instance of AuthenticatorSMSStage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AuthenticatorSMSStage.parse_obj(obj)

        _obj = AuthenticatorSMSStage.parse_obj({
            "pk": obj.get("pk"),
            "name": obj.get("name"),
            "component": obj.get("component"),
            "verbose_name": obj.get("verbose_name"),
            "verbose_name_plural": obj.get("verbose_name_plural"),
            "meta_model_name": obj.get("meta_model_name"),
            "flow_set": [FlowSet.from_dict(_item) for _item in obj.get("flow_set")] if obj.get("flow_set") is not None else None,
            "configure_flow": obj.get("configure_flow"),
            "friendly_name": obj.get("friendly_name"),
            "provider": obj.get("provider"),
            "from_number": obj.get("from_number"),
            "account_sid": obj.get("account_sid"),
            "auth": obj.get("auth"),
            "auth_password": obj.get("auth_password"),
            "auth_type": obj.get("auth_type"),
            "verify_only": obj.get("verify_only"),
            "mapping": obj.get("mapping")
        })
        return _obj


