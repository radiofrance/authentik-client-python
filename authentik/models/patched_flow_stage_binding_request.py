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
from pydantic import BaseModel, Field, StrictBool, StrictStr, conint
from authentik.models.invalid_response_action_enum import InvalidResponseActionEnum
from authentik.models.policy_engine_mode import PolicyEngineMode

class PatchedFlowStageBindingRequest(BaseModel):
    """
    FlowStageBinding Serializer
    """
    target: Optional[StrictStr] = None
    stage: Optional[StrictStr] = None
    evaluate_on_plan: Optional[StrictBool] = Field(None, description="Evaluate policies during the Flow planning process.")
    re_evaluate_policies: Optional[StrictBool] = Field(None, description="Evaluate policies when the Stage is present to the user.")
    order: Optional[conint(strict=True, le=2147483647, ge=-2147483648)] = None
    policy_engine_mode: Optional[PolicyEngineMode] = None
    invalid_response_action: Optional[InvalidResponseActionEnum] = None
    __properties = ["target", "stage", "evaluate_on_plan", "re_evaluate_policies", "order", "policy_engine_mode", "invalid_response_action"]

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
    def from_json(cls, json_str: str) -> PatchedFlowStageBindingRequest:
        """Create an instance of PatchedFlowStageBindingRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PatchedFlowStageBindingRequest:
        """Create an instance of PatchedFlowStageBindingRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PatchedFlowStageBindingRequest.parse_obj(obj)

        _obj = PatchedFlowStageBindingRequest.parse_obj({
            "target": obj.get("target"),
            "stage": obj.get("stage"),
            "evaluate_on_plan": obj.get("evaluate_on_plan"),
            "re_evaluate_policies": obj.get("re_evaluate_policies"),
            "order": obj.get("order"),
            "policy_engine_mode": obj.get("policy_engine_mode"),
            "invalid_response_action": obj.get("invalid_response_action")
        })
        return _obj


