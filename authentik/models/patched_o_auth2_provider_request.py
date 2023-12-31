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
from authentik.models.client_type_enum import ClientTypeEnum
from authentik.models.issuer_mode_enum import IssuerModeEnum
from authentik.models.sub_mode_enum import SubModeEnum

class PatchedOAuth2ProviderRequest(BaseModel):
    """
    OAuth2Provider Serializer
    """
    name: Optional[constr(strict=True, min_length=1)] = None
    authentication_flow: Optional[StrictStr] = Field(None, description="Flow used for authentication when the associated application is accessed by an un-authenticated user.")
    authorization_flow: Optional[StrictStr] = Field(None, description="Flow used when authorizing this provider.")
    property_mappings: Optional[conlist(StrictStr)] = None
    client_type: Optional[ClientTypeEnum] = None
    client_id: Optional[constr(strict=True, max_length=255, min_length=1)] = None
    client_secret: Optional[constr(strict=True, max_length=255)] = None
    access_code_validity: Optional[constr(strict=True, min_length=1)] = Field(None, description="Access codes not valid on or after current time + this value (Format: hours=1;minutes=2;seconds=3).")
    access_token_validity: Optional[constr(strict=True, min_length=1)] = Field(None, description="Tokens not valid on or after current time + this value (Format: hours=1;minutes=2;seconds=3).")
    refresh_token_validity: Optional[constr(strict=True, min_length=1)] = Field(None, description="Tokens not valid on or after current time + this value (Format: hours=1;minutes=2;seconds=3).")
    include_claims_in_id_token: Optional[StrictBool] = Field(None, description="Include User claims from scopes in the id_token, for applications that don't access the userinfo endpoint.")
    signing_key: Optional[StrictStr] = Field(None, description="Key used to sign the tokens. Only required when JWT Algorithm is set to RS256.")
    redirect_uris: Optional[StrictStr] = Field(None, description="Enter each URI on a new line.")
    sub_mode: Optional[SubModeEnum] = None
    issuer_mode: Optional[IssuerModeEnum] = None
    jwks_sources: Optional[conlist(StrictStr)] = None
    __properties = ["name", "authentication_flow", "authorization_flow", "property_mappings", "client_type", "client_id", "client_secret", "access_code_validity", "access_token_validity", "refresh_token_validity", "include_claims_in_id_token", "signing_key", "redirect_uris", "sub_mode", "issuer_mode", "jwks_sources"]

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
    def from_json(cls, json_str: str) -> PatchedOAuth2ProviderRequest:
        """Create an instance of PatchedOAuth2ProviderRequest from a JSON string"""
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

        # set to None if signing_key (nullable) is None
        # and __fields_set__ contains the field
        if self.signing_key is None and "signing_key" in self.__fields_set__:
            _dict['signing_key'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PatchedOAuth2ProviderRequest:
        """Create an instance of PatchedOAuth2ProviderRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PatchedOAuth2ProviderRequest.parse_obj(obj)

        _obj = PatchedOAuth2ProviderRequest.parse_obj({
            "name": obj.get("name"),
            "authentication_flow": obj.get("authentication_flow"),
            "authorization_flow": obj.get("authorization_flow"),
            "property_mappings": obj.get("property_mappings"),
            "client_type": obj.get("client_type"),
            "client_id": obj.get("client_id"),
            "client_secret": obj.get("client_secret"),
            "access_code_validity": obj.get("access_code_validity"),
            "access_token_validity": obj.get("access_token_validity"),
            "refresh_token_validity": obj.get("refresh_token_validity"),
            "include_claims_in_id_token": obj.get("include_claims_in_id_token"),
            "signing_key": obj.get("signing_key"),
            "redirect_uris": obj.get("redirect_uris"),
            "sub_mode": obj.get("sub_mode"),
            "issuer_mode": obj.get("issuer_mode"),
            "jwks_sources": obj.get("jwks_sources")
        })
        return _obj


