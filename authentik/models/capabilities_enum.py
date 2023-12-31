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





class CapabilitiesEnum(str, Enum):
    """
    * `can_save_media` - Can Save Media * `can_geo_ip` - Can Geo Ip * `can_impersonate` - Can Impersonate * `can_debug` - Can Debug * `is_enterprise` - Is Enterprise
    """

    """
    allowed enum values
    """
    CAN_SAVE_MEDIA = 'can_save_media'
    CAN_GEO_IP = 'can_geo_ip'
    CAN_IMPERSONATE = 'can_impersonate'
    CAN_DEBUG = 'can_debug'
    IS_ENTERPRISE = 'is_enterprise'

    @classmethod
    def from_json(cls, json_str: str) -> CapabilitiesEnum:
        """Create an instance of CapabilitiesEnum from a JSON string"""
        return CapabilitiesEnum(json.loads(json_str))


