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





class ProviderTypeEnum(str, Enum):
    """
    * `apple` - Apple * `azuread` - Azure AD * `discord` - Discord * `facebook` - Facebook * `github` - GitHub * `google` - Google * `mailcow` - Mailcow * `openidconnect` - OpenID Connect * `okta` - Okta * `patreon` - Patreon * `reddit` - Reddit * `twitch` - Twitch * `twitter` - Twitter
    """

    """
    allowed enum values
    """
    APPLE = 'apple'
    AZUREAD = 'azuread'
    DISCORD = 'discord'
    FACEBOOK = 'facebook'
    GITHUB = 'github'
    GOOGLE = 'google'
    MAILCOW = 'mailcow'
    OPENIDCONNECT = 'openidconnect'
    OKTA = 'okta'
    PATREON = 'patreon'
    REDDIT = 'reddit'
    TWITCH = 'twitch'
    TWITTER = 'twitter'

    @classmethod
    def from_json(cls, json_str: str) -> ProviderTypeEnum:
        """Create an instance of ProviderTypeEnum from a JSON string"""
        return ProviderTypeEnum(json.loads(json_str))


