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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist
from authentik.models.prompt_type_enum import PromptTypeEnum

class StagePrompt(BaseModel):
    """
    Serializer for a single Prompt field
    """
    field_key: StrictStr = Field(...)
    label: StrictStr = Field(...)
    type: PromptTypeEnum = Field(...)
    required: StrictBool = Field(...)
    placeholder: StrictStr = Field(...)
    initial_value: StrictStr = Field(...)
    order: StrictInt = Field(...)
    sub_text: StrictStr = Field(...)
    choices: Optional[conlist(StrictStr)] = Field(...)
    __properties = ["field_key", "label", "type", "required", "placeholder", "initial_value", "order", "sub_text", "choices"]

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
    def from_json(cls, json_str: str) -> StagePrompt:
        """Create an instance of StagePrompt from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if choices (nullable) is None
        # and __fields_set__ contains the field
        if self.choices is None and "choices" in self.__fields_set__:
            _dict['choices'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> StagePrompt:
        """Create an instance of StagePrompt from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return StagePrompt.parse_obj(obj)

        _obj = StagePrompt.parse_obj({
            "field_key": obj.get("field_key"),
            "label": obj.get("label"),
            "type": obj.get("type"),
            "required": obj.get("required"),
            "placeholder": obj.get("placeholder"),
            "initial_value": obj.get("initial_value"),
            "order": obj.get("order"),
            "sub_text": obj.get("sub_text"),
            "choices": obj.get("choices")
        })
        return _obj


