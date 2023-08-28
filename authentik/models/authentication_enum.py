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





class AuthenticationEnum(str, Enum):
    """
    * `none` - None * `require_authenticated` - Require Authenticated * `require_unauthenticated` - Require Unauthenticated * `require_superuser` - Require Superuser
    """

    """
    allowed enum values
    """
    NONE = 'none'
    REQUIRE_AUTHENTICATED = 'require_authenticated'
    REQUIRE_UNAUTHENTICATED = 'require_unauthenticated'
    REQUIRE_SUPERUSER = 'require_superuser'

    @classmethod
    def from_json(cls, json_str: str) -> AuthenticationEnum:
        """Create an instance of AuthenticationEnum from a JSON string"""
        return AuthenticationEnum(json.loads(json_str))

