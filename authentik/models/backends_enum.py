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





class BackendsEnum(str, Enum):
    """
    * `authentik.core.auth.InbuiltBackend` - User database + standard password * `authentik.core.auth.TokenBackend` - User database + app passwords * `authentik.sources.ldap.auth.LDAPBackend` - User database + LDAP password
    """

    """
    allowed enum values
    """
    AUTHENTIK_DOT_CORE_DOT_AUTH_DOT_INBUILT_BACKEND = 'authentik.core.auth.InbuiltBackend'
    AUTHENTIK_DOT_CORE_DOT_AUTH_DOT_TOKEN_BACKEND = 'authentik.core.auth.TokenBackend'
    AUTHENTIK_DOT_SOURCES_DOT_LDAP_DOT_AUTH_DOT_LDAP_BACKEND = 'authentik.sources.ldap.auth.LDAPBackend'

    @classmethod
    def from_json(cls, json_str: str) -> BackendsEnum:
        """Create an instance of BackendsEnum from a JSON string"""
        return BackendsEnum(json.loads(json_str))

