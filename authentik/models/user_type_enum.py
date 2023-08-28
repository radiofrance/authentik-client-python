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





class UserTypeEnum(str, Enum):
    """
    * `internal` - Internal * `external` - External * `service_account` - Service Account * `internal_service_account` - Internal Service Account
    """

    """
    allowed enum values
    """
    INTERNAL = 'internal'
    EXTERNAL = 'external'
    SERVICE_ACCOUNT = 'service_account'
    INTERNAL_SERVICE_ACCOUNT = 'internal_service_account'

    @classmethod
    def from_json(cls, json_str: str) -> UserTypeEnum:
        """Create an instance of UserTypeEnum from a JSON string"""
        return UserTypeEnum(json.loads(json_str))

