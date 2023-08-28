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
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist, constr, validator
from authentik.models.policy_engine_mode import PolicyEngineMode
from authentik.models.user_matching_mode_enum import UserMatchingModeEnum

class PatchedPlexSourceRequest(BaseModel):
    """
    Plex Source Serializer
    """
    name: Optional[constr(strict=True, min_length=1)] = Field(None, description="Source's display Name.")
    slug: Optional[constr(strict=True, max_length=50, min_length=1)] = Field(None, description="Internal source name, used in URLs.")
    enabled: Optional[StrictBool] = None
    authentication_flow: Optional[StrictStr] = Field(None, description="Flow to use when authenticating existing users.")
    enrollment_flow: Optional[StrictStr] = Field(None, description="Flow to use when enrolling new users.")
    policy_engine_mode: Optional[PolicyEngineMode] = None
    user_matching_mode: Optional[UserMatchingModeEnum] = None
    user_path_template: Optional[constr(strict=True, min_length=1)] = None
    client_id: Optional[constr(strict=True, min_length=1)] = Field(None, description="Client identifier used to talk to Plex.")
    allowed_servers: Optional[conlist(constr(strict=True, min_length=1))] = Field(None, description="Which servers a user has to be a member of to be granted access. Empty list allows every server.")
    allow_friends: Optional[StrictBool] = Field(None, description="Allow friends to authenticate, even if you don't share a server.")
    plex_token: Optional[constr(strict=True, min_length=1)] = Field(None, description="Plex token used to check friends")
    __properties = ["name", "slug", "enabled", "authentication_flow", "enrollment_flow", "policy_engine_mode", "user_matching_mode", "user_path_template", "client_id", "allowed_servers", "allow_friends", "plex_token"]

    @validator('slug')
    def slug_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

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
    def from_json(cls, json_str: str) -> PatchedPlexSourceRequest:
        """Create an instance of PatchedPlexSourceRequest from a JSON string"""
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

        # set to None if enrollment_flow (nullable) is None
        # and __fields_set__ contains the field
        if self.enrollment_flow is None and "enrollment_flow" in self.__fields_set__:
            _dict['enrollment_flow'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PatchedPlexSourceRequest:
        """Create an instance of PatchedPlexSourceRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PatchedPlexSourceRequest.parse_obj(obj)

        _obj = PatchedPlexSourceRequest.parse_obj({
            "name": obj.get("name"),
            "slug": obj.get("slug"),
            "enabled": obj.get("enabled"),
            "authentication_flow": obj.get("authentication_flow"),
            "enrollment_flow": obj.get("enrollment_flow"),
            "policy_engine_mode": obj.get("policy_engine_mode"),
            "user_matching_mode": obj.get("user_matching_mode"),
            "user_path_template": obj.get("user_path_template"),
            "client_id": obj.get("client_id"),
            "allowed_servers": obj.get("allowed_servers"),
            "allow_friends": obj.get("allow_friends"),
            "plex_token": obj.get("plex_token")
        })
        return _obj

