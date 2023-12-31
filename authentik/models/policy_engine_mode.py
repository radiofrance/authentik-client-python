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





class PolicyEngineMode(str, Enum):
    """
    * `all` - all, all policies must pass * `any` - any, any policy must pass
    """

    """
    allowed enum values
    """
    ALL = 'all'
    ANY = 'any'

    @classmethod
    def from_json(cls, json_str: str) -> PolicyEngineMode:
        """Create an instance of PolicyEngineMode from a JSON string"""
        return PolicyEngineMode(json.loads(json_str))


