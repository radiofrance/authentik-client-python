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


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr

class KubernetesServiceConnection(BaseModel):
    """
    KubernetesServiceConnection Serializer
    """
    pk: StrictStr = Field(...)
    name: StrictStr = Field(...)
    local: Optional[StrictBool] = Field(None, description="If enabled, use the local connection. Required Docker socket/Kubernetes Integration")
    component: StrictStr = Field(...)
    verbose_name: StrictStr = Field(..., description="Return object's verbose_name")
    verbose_name_plural: StrictStr = Field(..., description="Return object's plural verbose_name")
    meta_model_name: StrictStr = Field(..., description="Return internal model name")
    kubeconfig: Optional[Dict[str, Any]] = Field(None, description="Paste your kubeconfig here. authentik will automatically use the currently selected context.")
    verify_ssl: Optional[StrictBool] = Field(None, description="Verify SSL Certificates of the Kubernetes API endpoint")
    __properties = ["pk", "name", "local", "component", "verbose_name", "verbose_name_plural", "meta_model_name", "kubeconfig", "verify_ssl"]

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
    def from_json(cls, json_str: str) -> KubernetesServiceConnection:
        """Create an instance of KubernetesServiceConnection from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> KubernetesServiceConnection:
        """Create an instance of KubernetesServiceConnection from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return KubernetesServiceConnection.parse_obj(obj)

        _obj = KubernetesServiceConnection.parse_obj({
            "pk": obj.get("pk"),
            "name": obj.get("name"),
            "local": obj.get("local"),
            "component": obj.get("component"),
            "verbose_name": obj.get("verbose_name"),
            "verbose_name_plural": obj.get("verbose_name_plural"),
            "meta_model_name": obj.get("meta_model_name"),
            "kubeconfig": obj.get("kubeconfig"),
            "verify_ssl": obj.get("verify_ssl")
        })
        return _obj


