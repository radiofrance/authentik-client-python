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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr
from authentik.models.authenticated_session_geo_ip import AuthenticatedSessionGeoIp
from authentik.models.authenticated_session_user_agent import AuthenticatedSessionUserAgent

class AuthenticatedSession(BaseModel):
    """
    AuthenticatedSession Serializer
    """
    uuid: Optional[StrictStr] = None
    current: StrictBool = Field(..., description="Check if session is currently active session")
    user_agent: AuthenticatedSessionUserAgent = Field(...)
    geo_ip: Optional[AuthenticatedSessionGeoIp] = Field(...)
    user: StrictInt = Field(...)
    last_ip: StrictStr = Field(...)
    last_user_agent: Optional[StrictStr] = None
    last_used: datetime = Field(...)
    expires: Optional[datetime] = None
    __properties = ["uuid", "current", "user_agent", "geo_ip", "user", "last_ip", "last_user_agent", "last_used", "expires"]

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
    def from_json(cls, json_str: str) -> AuthenticatedSession:
        """Create an instance of AuthenticatedSession from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "current",
                            "last_used",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of user_agent
        if self.user_agent:
            _dict['user_agent'] = self.user_agent.to_dict()
        # override the default output from pydantic by calling `to_dict()` of geo_ip
        if self.geo_ip:
            _dict['geo_ip'] = self.geo_ip.to_dict()
        # set to None if geo_ip (nullable) is None
        # and __fields_set__ contains the field
        if self.geo_ip is None and "geo_ip" in self.__fields_set__:
            _dict['geo_ip'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AuthenticatedSession:
        """Create an instance of AuthenticatedSession from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AuthenticatedSession.parse_obj(obj)

        _obj = AuthenticatedSession.parse_obj({
            "uuid": obj.get("uuid"),
            "current": obj.get("current"),
            "user_agent": AuthenticatedSessionUserAgent.from_dict(obj.get("user_agent")) if obj.get("user_agent") is not None else None,
            "geo_ip": AuthenticatedSessionGeoIp.from_dict(obj.get("geo_ip")) if obj.get("geo_ip") is not None else None,
            "user": obj.get("user"),
            "last_ip": obj.get("last_ip"),
            "last_user_agent": obj.get("last_user_agent"),
            "last_used": obj.get("last_used"),
            "expires": obj.get("expires")
        })
        return _obj

