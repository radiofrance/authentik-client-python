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



from pydantic import BaseModel, Field, StrictStr

class OAuth2ProviderSetupURLs(BaseModel):
    """
    OAuth2 Provider Metadata serializer
    """
    issuer: StrictStr = Field(...)
    authorize: StrictStr = Field(...)
    token: StrictStr = Field(...)
    user_info: StrictStr = Field(...)
    provider_info: StrictStr = Field(...)
    logout: StrictStr = Field(...)
    jwks: StrictStr = Field(...)
    __properties = ["issuer", "authorize", "token", "user_info", "provider_info", "logout", "jwks"]

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
    def from_json(cls, json_str: str) -> OAuth2ProviderSetupURLs:
        """Create an instance of OAuth2ProviderSetupURLs from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "issuer",
                            "authorize",
                            "token",
                            "user_info",
                            "provider_info",
                            "logout",
                            "jwks",
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OAuth2ProviderSetupURLs:
        """Create an instance of OAuth2ProviderSetupURLs from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OAuth2ProviderSetupURLs.parse_obj(obj)

        _obj = OAuth2ProviderSetupURLs.parse_obj({
            "issuer": obj.get("issuer"),
            "authorize": obj.get("authorize"),
            "token": obj.get("token"),
            "user_info": obj.get("user_info"),
            "provider_info": obj.get("provider_info"),
            "logout": obj.get("logout"),
            "jwks": obj.get("jwks")
        })
        return _obj


