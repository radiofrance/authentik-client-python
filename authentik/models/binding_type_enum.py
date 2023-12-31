# coding: utf-8

"""
    authentik

    Making authentication simple.

    The version of the OpenAPI document: 2023.6.1
    Contact: hello@goauthentik.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class BindingTypeEnum(str, Enum):
    """
    * `REDIRECT` - Redirect Binding * `POST` - POST Binding * `POST_AUTO` - POST Binding with auto-confirmation
    """

    """
    allowed enum values
    """
    REDIRECT = 'REDIRECT'
    POST = 'POST'
    POST_AUTO = 'POST_AUTO'

    @classmethod
    def from_json(cls, json_str: str) -> BindingTypeEnum:
        """Create an instance of BindingTypeEnum from a JSON string"""
        return BindingTypeEnum(json.loads(json_str))


