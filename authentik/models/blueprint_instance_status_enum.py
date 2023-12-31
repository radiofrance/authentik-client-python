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





class BlueprintInstanceStatusEnum(str, Enum):
    """
    * `successful` - Successful * `warning` - Warning * `error` - Error * `orphaned` - Orphaned * `unknown` - Unknown
    """

    """
    allowed enum values
    """
    SUCCESSFUL = 'successful'
    WARNING = 'warning'
    ERROR = 'error'
    ORPHANED = 'orphaned'
    UNKNOWN = 'unknown'

    @classmethod
    def from_json(cls, json_str: str) -> BlueprintInstanceStatusEnum:
        """Create an instance of BlueprintInstanceStatusEnum from a JSON string"""
        return BlueprintInstanceStatusEnum(json.loads(json_str))


