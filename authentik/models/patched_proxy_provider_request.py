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
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist, constr
from authentik.models.proxy_mode import ProxyMode

class PatchedProxyProviderRequest(BaseModel):
    """
    ProxyProvider Serializer
    """
    name: Optional[constr(strict=True, min_length=1)] = None
    authentication_flow: Optional[StrictStr] = Field(None, description="Flow used for authentication when the associated application is accessed by an un-authenticated user.")
    authorization_flow: Optional[StrictStr] = Field(None, description="Flow used when authorizing this provider.")
    property_mappings: Optional[conlist(StrictStr)] = None
    internal_host: Optional[StrictStr] = None
    external_host: Optional[constr(strict=True, min_length=1)] = None
    internal_host_ssl_validation: Optional[StrictBool] = Field(None, description="Validate SSL Certificates of upstream servers")
    certificate: Optional[StrictStr] = None
    skip_path_regex: Optional[StrictStr] = Field(None, description="Regular expressions for which authentication is not required. Each new line is interpreted as a new Regular Expression.")
    basic_auth_enabled: Optional[StrictBool] = Field(None, description="Set a custom HTTP-Basic Authentication header based on values from authentik.")
    basic_auth_password_attribute: Optional[StrictStr] = Field(None, description="User/Group Attribute used for the password part of the HTTP-Basic Header.")
    basic_auth_user_attribute: Optional[StrictStr] = Field(None, description="User/Group Attribute used for the user part of the HTTP-Basic Header. If not set, the user's Email address is used.")
    mode: Optional[ProxyMode] = None
    intercept_header_auth: Optional[StrictBool] = Field(None, description="When enabled, this provider will intercept the authorization header and authenticate requests based on its value.")
    cookie_domain: Optional[StrictStr] = None
    jwks_sources: Optional[conlist(StrictStr)] = None
    access_token_validity: Optional[constr(strict=True, min_length=1)] = Field(None, description="Tokens not valid on or after current time + this value (Format: hours=1;minutes=2;seconds=3).")
    refresh_token_validity: Optional[constr(strict=True, min_length=1)] = Field(None, description="Tokens not valid on or after current time + this value (Format: hours=1;minutes=2;seconds=3).")
    __properties = ["name", "authentication_flow", "authorization_flow", "property_mappings", "internal_host", "external_host", "internal_host_ssl_validation", "certificate", "skip_path_regex", "basic_auth_enabled", "basic_auth_password_attribute", "basic_auth_user_attribute", "mode", "intercept_header_auth", "cookie_domain", "jwks_sources", "access_token_validity", "refresh_token_validity"]

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
    def from_json(cls, json_str: str) -> PatchedProxyProviderRequest:
        """Create an instance of PatchedProxyProviderRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if authentication_flow (nullable) is None
        # and __fields_set__ contains the field
        if self.authentication_flow is None and "authentication_flow" in self.__fields_set__:
            _dict['authentication_flow'] = None

        # set to None if certificate (nullable) is None
        # and __fields_set__ contains the field
        if self.certificate is None and "certificate" in self.__fields_set__:
            _dict['certificate'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PatchedProxyProviderRequest:
        """Create an instance of PatchedProxyProviderRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PatchedProxyProviderRequest.parse_obj(obj)

        _obj = PatchedProxyProviderRequest.parse_obj({
            "name": obj.get("name"),
            "authentication_flow": obj.get("authentication_flow"),
            "authorization_flow": obj.get("authorization_flow"),
            "property_mappings": obj.get("property_mappings"),
            "internal_host": obj.get("internal_host"),
            "external_host": obj.get("external_host"),
            "internal_host_ssl_validation": obj.get("internal_host_ssl_validation"),
            "certificate": obj.get("certificate"),
            "skip_path_regex": obj.get("skip_path_regex"),
            "basic_auth_enabled": obj.get("basic_auth_enabled"),
            "basic_auth_password_attribute": obj.get("basic_auth_password_attribute"),
            "basic_auth_user_attribute": obj.get("basic_auth_user_attribute"),
            "mode": obj.get("mode"),
            "intercept_header_auth": obj.get("intercept_header_auth"),
            "cookie_domain": obj.get("cookie_domain"),
            "jwks_sources": obj.get("jwks_sources"),
            "access_token_validity": obj.get("access_token_validity"),
            "refresh_token_validity": obj.get("refresh_token_validity")
        })
        return _obj

