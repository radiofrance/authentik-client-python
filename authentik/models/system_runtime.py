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

class SystemRuntime(BaseModel):
    """
    Get versions
    """
    python_version: StrictStr = Field(...)
    gunicorn_version: StrictStr = Field(...)
    environment: StrictStr = Field(...)
    architecture: StrictStr = Field(...)
    platform: StrictStr = Field(...)
    uname: StrictStr = Field(...)
    __properties = ["python_version", "gunicorn_version", "environment", "architecture", "platform", "uname"]

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
    def from_json(cls, json_str: str) -> SystemRuntime:
        """Create an instance of SystemRuntime from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SystemRuntime:
        """Create an instance of SystemRuntime from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SystemRuntime.parse_obj(obj)

        _obj = SystemRuntime.parse_obj({
            "python_version": obj.get("python_version"),
            "gunicorn_version": obj.get("gunicorn_version"),
            "environment": obj.get("environment"),
            "architecture": obj.get("architecture"),
            "platform": obj.get("platform"),
            "uname": obj.get("uname")
        })
        return _obj


