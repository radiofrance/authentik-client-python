# coding: utf-8

# flake8: noqa
"""
    authentik

    Making authentication simple.

    The version of the OpenAPI document: 2023.6.1
    Contact: hello@goauthentik.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from authentik.models.access_denied_challenge import AccessDeniedChallenge
from authentik.models.app import App
from authentik.models.app_enum import AppEnum
from authentik.models.apple_challenge_response_request import AppleChallengeResponseRequest
from authentik.models.apple_login_challenge import AppleLoginChallenge
from authentik.models.application import Application
from authentik.models.application_request import ApplicationRequest
from authentik.models.auth_type_enum import AuthTypeEnum
from authentik.models.authenticate_web_authn_stage import AuthenticateWebAuthnStage
from authentik.models.authenticate_web_authn_stage_request import AuthenticateWebAuthnStageRequest
from authentik.models.authenticated_session import AuthenticatedSession
from authentik.models.authenticated_session_geo_ip import AuthenticatedSessionGeoIp
from authentik.models.authenticated_session_user_agent import AuthenticatedSessionUserAgent
from authentik.models.authenticated_session_user_agent_device import AuthenticatedSessionUserAgentDevice
from authentik.models.authenticated_session_user_agent_os import AuthenticatedSessionUserAgentOs
from authentik.models.authenticated_session_user_agent_user_agent import AuthenticatedSessionUserAgentUserAgent
from authentik.models.authentication_enum import AuthenticationEnum
from authentik.models.authenticator_attachment_enum import AuthenticatorAttachmentEnum
from authentik.models.authenticator_duo_challenge import AuthenticatorDuoChallenge
from authentik.models.authenticator_duo_challenge_response_request import AuthenticatorDuoChallengeResponseRequest
from authentik.models.authenticator_duo_stage import AuthenticatorDuoStage
from authentik.models.authenticator_duo_stage_device_import_response import AuthenticatorDuoStageDeviceImportResponse
from authentik.models.authenticator_duo_stage_manual_device_import_request import AuthenticatorDuoStageManualDeviceImportRequest
from authentik.models.authenticator_duo_stage_request import AuthenticatorDuoStageRequest
from authentik.models.authenticator_sms_challenge import AuthenticatorSMSChallenge
from authentik.models.authenticator_sms_challenge_response_request import AuthenticatorSMSChallengeResponseRequest
from authentik.models.authenticator_sms_stage import AuthenticatorSMSStage
from authentik.models.authenticator_sms_stage_request import AuthenticatorSMSStageRequest
from authentik.models.authenticator_static_challenge import AuthenticatorStaticChallenge
from authentik.models.authenticator_static_challenge_response_request import AuthenticatorStaticChallengeResponseRequest
from authentik.models.authenticator_static_stage import AuthenticatorStaticStage
from authentik.models.authenticator_static_stage_request import AuthenticatorStaticStageRequest
from authentik.models.authenticator_totp_challenge import AuthenticatorTOTPChallenge
from authentik.models.authenticator_totp_challenge_response_request import AuthenticatorTOTPChallengeResponseRequest
from authentik.models.authenticator_totp_stage import AuthenticatorTOTPStage
from authentik.models.authenticator_totp_stage_request import AuthenticatorTOTPStageRequest
from authentik.models.authenticator_validate_stage import AuthenticatorValidateStage
from authentik.models.authenticator_validate_stage_request import AuthenticatorValidateStageRequest
from authentik.models.authenticator_validation_challenge import AuthenticatorValidationChallenge
from authentik.models.authenticator_validation_challenge_response_request import AuthenticatorValidationChallengeResponseRequest
from authentik.models.authenticator_web_authn_challenge import AuthenticatorWebAuthnChallenge
from authentik.models.authenticator_web_authn_challenge_response_request import AuthenticatorWebAuthnChallengeResponseRequest
from authentik.models.auto_submit_challenge_response_request import AutoSubmitChallengeResponseRequest
from authentik.models.autosubmit_challenge import AutosubmitChallenge
from authentik.models.backends_enum import BackendsEnum
from authentik.models.binding_type_enum import BindingTypeEnum
from authentik.models.blueprint_file import BlueprintFile
from authentik.models.blueprint_instance import BlueprintInstance
from authentik.models.blueprint_instance_request import BlueprintInstanceRequest
from authentik.models.blueprint_instance_status_enum import BlueprintInstanceStatusEnum
from authentik.models.cache import Cache
from authentik.models.capabilities_enum import CapabilitiesEnum
from authentik.models.captcha_challenge import CaptchaChallenge
from authentik.models.captcha_challenge_response_request import CaptchaChallengeResponseRequest
from authentik.models.captcha_stage import CaptchaStage
from authentik.models.captcha_stage_request import CaptchaStageRequest
from authentik.models.certificate_data import CertificateData
from authentik.models.certificate_generation_request import CertificateGenerationRequest
from authentik.models.certificate_key_pair import CertificateKeyPair
from authentik.models.certificate_key_pair_request import CertificateKeyPairRequest
from authentik.models.challenge_choices import ChallengeChoices
from authentik.models.challenge_types import ChallengeTypes
from authentik.models.client_type_enum import ClientTypeEnum
from authentik.models.config import Config
from authentik.models.consent_challenge import ConsentChallenge
from authentik.models.consent_challenge_response_request import ConsentChallengeResponseRequest
from authentik.models.consent_stage import ConsentStage
from authentik.models.consent_stage_mode_enum import ConsentStageModeEnum
from authentik.models.consent_stage_request import ConsentStageRequest
from authentik.models.contextual_flow_info import ContextualFlowInfo
from authentik.models.coordinate import Coordinate
from authentik.models.current_tenant import CurrentTenant
from authentik.models.denied_action_enum import DeniedActionEnum
from authentik.models.deny_stage import DenyStage
from authentik.models.deny_stage_request import DenyStageRequest
from authentik.models.device import Device
from authentik.models.device_challenge import DeviceChallenge
from authentik.models.device_challenge_request import DeviceChallengeRequest
from authentik.models.device_classes_enum import DeviceClassesEnum
from authentik.models.digest_algorithm_enum import DigestAlgorithmEnum
from authentik.models.digits_enum import DigitsEnum
from authentik.models.docker_service_connection import DockerServiceConnection
from authentik.models.docker_service_connection_request import DockerServiceConnectionRequest
from authentik.models.dummy_challenge import DummyChallenge
from authentik.models.dummy_challenge_response_request import DummyChallengeResponseRequest
from authentik.models.dummy_policy import DummyPolicy
from authentik.models.dummy_policy_request import DummyPolicyRequest
from authentik.models.dummy_stage import DummyStage
from authentik.models.dummy_stage_request import DummyStageRequest
from authentik.models.duo_device import DuoDevice
from authentik.models.duo_device_enrollment_status import DuoDeviceEnrollmentStatus
from authentik.models.duo_device_request import DuoDeviceRequest
from authentik.models.duo_response_enum import DuoResponseEnum
from authentik.models.email_challenge import EmailChallenge
from authentik.models.email_challenge_response_request import EmailChallengeResponseRequest
from authentik.models.email_stage import EmailStage
from authentik.models.email_stage_request import EmailStageRequest
from authentik.models.error_detail import ErrorDetail
from authentik.models.error_reporting_config import ErrorReportingConfig
from authentik.models.event import Event
from authentik.models.event_actions import EventActions
from authentik.models.event_matcher_policy import EventMatcherPolicy
from authentik.models.event_matcher_policy_request import EventMatcherPolicyRequest
from authentik.models.event_request import EventRequest
from authentik.models.event_top_per_user import EventTopPerUser
from authentik.models.expiring_base_grant_model import ExpiringBaseGrantModel
from authentik.models.expression_policy import ExpressionPolicy
from authentik.models.expression_policy_request import ExpressionPolicyRequest
from authentik.models.file_path_request import FilePathRequest
from authentik.models.flow import Flow
from authentik.models.flow_challenge_response_request import FlowChallengeResponseRequest
from authentik.models.flow_designation_enum import FlowDesignationEnum
from authentik.models.flow_diagram import FlowDiagram
from authentik.models.flow_error_challenge import FlowErrorChallenge
from authentik.models.flow_import_result import FlowImportResult
from authentik.models.flow_inspection import FlowInspection
from authentik.models.flow_inspector_plan import FlowInspectorPlan
from authentik.models.flow_request import FlowRequest
from authentik.models.flow_set import FlowSet
from authentik.models.flow_set_request import FlowSetRequest
from authentik.models.flow_stage_binding import FlowStageBinding
from authentik.models.flow_stage_binding_request import FlowStageBindingRequest
from authentik.models.footer_link import FooterLink
from authentik.models.generic_error import GenericError
from authentik.models.group import Group
from authentik.models.group_member import GroupMember
from authentik.models.group_member_request import GroupMemberRequest
from authentik.models.group_request import GroupRequest
from authentik.models.identification_challenge import IdentificationChallenge
from authentik.models.identification_challenge_response_request import IdentificationChallengeResponseRequest
from authentik.models.identification_stage import IdentificationStage
from authentik.models.identification_stage_request import IdentificationStageRequest
from authentik.models.install_id import InstallID
from authentik.models.intent_enum import IntentEnum
from authentik.models.invalid_response_action_enum import InvalidResponseActionEnum
from authentik.models.invitation import Invitation
from authentik.models.invitation_request import InvitationRequest
from authentik.models.invitation_stage import InvitationStage
from authentik.models.invitation_stage_request import InvitationStageRequest
from authentik.models.issuer_mode_enum import IssuerModeEnum
from authentik.models.kubernetes_service_connection import KubernetesServiceConnection
from authentik.models.kubernetes_service_connection_request import KubernetesServiceConnectionRequest
from authentik.models.ldapapi_access_mode import LDAPAPIAccessMode
from authentik.models.ldap_debug import LDAPDebug
from authentik.models.ldap_outpost_config import LDAPOutpostConfig
from authentik.models.ldap_property_mapping import LDAPPropertyMapping
from authentik.models.ldap_property_mapping_request import LDAPPropertyMappingRequest
from authentik.models.ldap_provider import LDAPProvider
from authentik.models.ldap_provider_request import LDAPProviderRequest
from authentik.models.ldap_source import LDAPSource
from authentik.models.ldap_source_request import LDAPSourceRequest
from authentik.models.layout_enum import LayoutEnum
from authentik.models.license import License
from authentik.models.license_forecast import LicenseForecast
from authentik.models.license_request import LicenseRequest
from authentik.models.license_summary import LicenseSummary
from authentik.models.link import Link
from authentik.models.login_challenge_types import LoginChallengeTypes
from authentik.models.login_metrics import LoginMetrics
from authentik.models.login_source import LoginSource
from authentik.models.metadata import Metadata
from authentik.models.model_enum import ModelEnum
from authentik.models.name_id_policy_enum import NameIdPolicyEnum
from authentik.models.not_configured_action_enum import NotConfiguredActionEnum
from authentik.models.notification import Notification
from authentik.models.notification_request import NotificationRequest
from authentik.models.notification_rule import NotificationRule
from authentik.models.notification_rule_request import NotificationRuleRequest
from authentik.models.notification_transport import NotificationTransport
from authentik.models.notification_transport_mode_enum import NotificationTransportModeEnum
from authentik.models.notification_transport_request import NotificationTransportRequest
from authentik.models.notification_transport_test import NotificationTransportTest
from authentik.models.notification_webhook_mapping import NotificationWebhookMapping
from authentik.models.notification_webhook_mapping_request import NotificationWebhookMappingRequest
from authentik.models.o_auth2_provider import OAuth2Provider
from authentik.models.o_auth2_provider_request import OAuth2ProviderRequest
from authentik.models.o_auth2_provider_setup_urls import OAuth2ProviderSetupURLs
from authentik.models.o_auth_device_code_challenge import OAuthDeviceCodeChallenge
from authentik.models.o_auth_device_code_challenge_response_request import OAuthDeviceCodeChallengeResponseRequest
from authentik.models.o_auth_device_code_finish_challenge import OAuthDeviceCodeFinishChallenge
from authentik.models.o_auth_device_code_finish_challenge_response_request import OAuthDeviceCodeFinishChallengeResponseRequest
from authentik.models.o_auth_source import OAuthSource
from authentik.models.o_auth_source_request import OAuthSourceRequest
from authentik.models.open_id_connect_configuration import OpenIDConnectConfiguration
from authentik.models.outpost import Outpost
from authentik.models.outpost_default_config import OutpostDefaultConfig
from authentik.models.outpost_health import OutpostHealth
from authentik.models.outpost_request import OutpostRequest
from authentik.models.outpost_type_enum import OutpostTypeEnum
from authentik.models.paginated_application_list import PaginatedApplicationList
from authentik.models.paginated_authenticate_web_authn_stage_list import PaginatedAuthenticateWebAuthnStageList
from authentik.models.paginated_authenticated_session_list import PaginatedAuthenticatedSessionList
from authentik.models.paginated_authenticator_duo_stage_list import PaginatedAuthenticatorDuoStageList
from authentik.models.paginated_authenticator_sms_stage_list import PaginatedAuthenticatorSMSStageList
from authentik.models.paginated_authenticator_static_stage_list import PaginatedAuthenticatorStaticStageList
from authentik.models.paginated_authenticator_totp_stage_list import PaginatedAuthenticatorTOTPStageList
from authentik.models.paginated_authenticator_validate_stage_list import PaginatedAuthenticatorValidateStageList
from authentik.models.paginated_blueprint_instance_list import PaginatedBlueprintInstanceList
from authentik.models.paginated_captcha_stage_list import PaginatedCaptchaStageList
from authentik.models.paginated_certificate_key_pair_list import PaginatedCertificateKeyPairList
from authentik.models.paginated_consent_stage_list import PaginatedConsentStageList
from authentik.models.paginated_deny_stage_list import PaginatedDenyStageList
from authentik.models.paginated_docker_service_connection_list import PaginatedDockerServiceConnectionList
from authentik.models.paginated_dummy_policy_list import PaginatedDummyPolicyList
from authentik.models.paginated_dummy_stage_list import PaginatedDummyStageList
from authentik.models.paginated_duo_device_list import PaginatedDuoDeviceList
from authentik.models.paginated_email_stage_list import PaginatedEmailStageList
from authentik.models.paginated_event_list import PaginatedEventList
from authentik.models.paginated_event_matcher_policy_list import PaginatedEventMatcherPolicyList
from authentik.models.paginated_expiring_base_grant_model_list import PaginatedExpiringBaseGrantModelList
from authentik.models.paginated_expression_policy_list import PaginatedExpressionPolicyList
from authentik.models.paginated_flow_list import PaginatedFlowList
from authentik.models.paginated_flow_stage_binding_list import PaginatedFlowStageBindingList
from authentik.models.paginated_group_list import PaginatedGroupList
from authentik.models.paginated_identification_stage_list import PaginatedIdentificationStageList
from authentik.models.paginated_invitation_list import PaginatedInvitationList
from authentik.models.paginated_invitation_stage_list import PaginatedInvitationStageList
from authentik.models.paginated_kubernetes_service_connection_list import PaginatedKubernetesServiceConnectionList
from authentik.models.paginated_ldap_outpost_config_list import PaginatedLDAPOutpostConfigList
from authentik.models.paginated_ldap_property_mapping_list import PaginatedLDAPPropertyMappingList
from authentik.models.paginated_ldap_provider_list import PaginatedLDAPProviderList
from authentik.models.paginated_ldap_source_list import PaginatedLDAPSourceList
from authentik.models.paginated_license_list import PaginatedLicenseList
from authentik.models.paginated_notification_list import PaginatedNotificationList
from authentik.models.paginated_notification_rule_list import PaginatedNotificationRuleList
from authentik.models.paginated_notification_transport_list import PaginatedNotificationTransportList
from authentik.models.paginated_notification_webhook_mapping_list import PaginatedNotificationWebhookMappingList
from authentik.models.paginated_o_auth2_provider_list import PaginatedOAuth2ProviderList
from authentik.models.paginated_o_auth_source_list import PaginatedOAuthSourceList
from authentik.models.paginated_outpost_list import PaginatedOutpostList
from authentik.models.paginated_password_expiry_policy_list import PaginatedPasswordExpiryPolicyList
from authentik.models.paginated_password_policy_list import PaginatedPasswordPolicyList
from authentik.models.paginated_password_stage_list import PaginatedPasswordStageList
from authentik.models.paginated_plex_source_connection_list import PaginatedPlexSourceConnectionList
from authentik.models.paginated_plex_source_list import PaginatedPlexSourceList
from authentik.models.paginated_policy_binding_list import PaginatedPolicyBindingList
from authentik.models.paginated_policy_list import PaginatedPolicyList
from authentik.models.paginated_prompt_list import PaginatedPromptList
from authentik.models.paginated_prompt_stage_list import PaginatedPromptStageList
from authentik.models.paginated_property_mapping_list import PaginatedPropertyMappingList
from authentik.models.paginated_provider_list import PaginatedProviderList
from authentik.models.paginated_proxy_outpost_config_list import PaginatedProxyOutpostConfigList
from authentik.models.paginated_proxy_provider_list import PaginatedProxyProviderList
from authentik.models.paginated_radius_outpost_config_list import PaginatedRadiusOutpostConfigList
from authentik.models.paginated_radius_provider_list import PaginatedRadiusProviderList
from authentik.models.paginated_reputation_list import PaginatedReputationList
from authentik.models.paginated_reputation_policy_list import PaginatedReputationPolicyList
from authentik.models.paginated_saml_property_mapping_list import PaginatedSAMLPropertyMappingList
from authentik.models.paginated_saml_provider_list import PaginatedSAMLProviderList
from authentik.models.paginated_saml_source_list import PaginatedSAMLSourceList
from authentik.models.paginated_scim_mapping_list import PaginatedSCIMMappingList
from authentik.models.paginated_scim_provider_list import PaginatedSCIMProviderList
from authentik.models.paginated_sms_device_list import PaginatedSMSDeviceList
from authentik.models.paginated_scope_mapping_list import PaginatedScopeMappingList
from authentik.models.paginated_service_connection_list import PaginatedServiceConnectionList
from authentik.models.paginated_source_list import PaginatedSourceList
from authentik.models.paginated_stage_list import PaginatedStageList
from authentik.models.paginated_static_device_list import PaginatedStaticDeviceList
from authentik.models.paginated_totp_device_list import PaginatedTOTPDeviceList
from authentik.models.paginated_tenant_list import PaginatedTenantList
from authentik.models.paginated_token_list import PaginatedTokenList
from authentik.models.paginated_token_model_list import PaginatedTokenModelList
from authentik.models.paginated_user_consent_list import PaginatedUserConsentList
from authentik.models.paginated_user_delete_stage_list import PaginatedUserDeleteStageList
from authentik.models.paginated_user_list import PaginatedUserList
from authentik.models.paginated_user_login_stage_list import PaginatedUserLoginStageList
from authentik.models.paginated_user_logout_stage_list import PaginatedUserLogoutStageList
from authentik.models.paginated_user_o_auth_source_connection_list import PaginatedUserOAuthSourceConnectionList
from authentik.models.paginated_user_saml_source_connection_list import PaginatedUserSAMLSourceConnectionList
from authentik.models.paginated_user_source_connection_list import PaginatedUserSourceConnectionList
from authentik.models.paginated_user_write_stage_list import PaginatedUserWriteStageList
from authentik.models.paginated_web_authn_device_list import PaginatedWebAuthnDeviceList
from authentik.models.pagination import Pagination
from authentik.models.password_challenge import PasswordChallenge
from authentik.models.password_challenge_response_request import PasswordChallengeResponseRequest
from authentik.models.password_expiry_policy import PasswordExpiryPolicy
from authentik.models.password_expiry_policy_request import PasswordExpiryPolicyRequest
from authentik.models.password_policy import PasswordPolicy
from authentik.models.password_policy_request import PasswordPolicyRequest
from authentik.models.password_stage import PasswordStage
from authentik.models.password_stage_request import PasswordStageRequest
from authentik.models.patched_application_request import PatchedApplicationRequest
from authentik.models.patched_authenticate_web_authn_stage_request import PatchedAuthenticateWebAuthnStageRequest
from authentik.models.patched_authenticator_duo_stage_request import PatchedAuthenticatorDuoStageRequest
from authentik.models.patched_authenticator_sms_stage_request import PatchedAuthenticatorSMSStageRequest
from authentik.models.patched_authenticator_static_stage_request import PatchedAuthenticatorStaticStageRequest
from authentik.models.patched_authenticator_totp_stage_request import PatchedAuthenticatorTOTPStageRequest
from authentik.models.patched_authenticator_validate_stage_request import PatchedAuthenticatorValidateStageRequest
from authentik.models.patched_blueprint_instance_request import PatchedBlueprintInstanceRequest
from authentik.models.patched_captcha_stage_request import PatchedCaptchaStageRequest
from authentik.models.patched_certificate_key_pair_request import PatchedCertificateKeyPairRequest
from authentik.models.patched_consent_stage_request import PatchedConsentStageRequest
from authentik.models.patched_deny_stage_request import PatchedDenyStageRequest
from authentik.models.patched_docker_service_connection_request import PatchedDockerServiceConnectionRequest
from authentik.models.patched_dummy_policy_request import PatchedDummyPolicyRequest
from authentik.models.patched_dummy_stage_request import PatchedDummyStageRequest
from authentik.models.patched_duo_device_request import PatchedDuoDeviceRequest
from authentik.models.patched_email_stage_request import PatchedEmailStageRequest
from authentik.models.patched_event_matcher_policy_request import PatchedEventMatcherPolicyRequest
from authentik.models.patched_event_request import PatchedEventRequest
from authentik.models.patched_expression_policy_request import PatchedExpressionPolicyRequest
from authentik.models.patched_flow_request import PatchedFlowRequest
from authentik.models.patched_flow_stage_binding_request import PatchedFlowStageBindingRequest
from authentik.models.patched_group_request import PatchedGroupRequest
from authentik.models.patched_identification_stage_request import PatchedIdentificationStageRequest
from authentik.models.patched_invitation_request import PatchedInvitationRequest
from authentik.models.patched_invitation_stage_request import PatchedInvitationStageRequest
from authentik.models.patched_kubernetes_service_connection_request import PatchedKubernetesServiceConnectionRequest
from authentik.models.patched_ldap_property_mapping_request import PatchedLDAPPropertyMappingRequest
from authentik.models.patched_ldap_provider_request import PatchedLDAPProviderRequest
from authentik.models.patched_ldap_source_request import PatchedLDAPSourceRequest
from authentik.models.patched_license_request import PatchedLicenseRequest
from authentik.models.patched_notification_request import PatchedNotificationRequest
from authentik.models.patched_notification_rule_request import PatchedNotificationRuleRequest
from authentik.models.patched_notification_transport_request import PatchedNotificationTransportRequest
from authentik.models.patched_notification_webhook_mapping_request import PatchedNotificationWebhookMappingRequest
from authentik.models.patched_o_auth2_provider_request import PatchedOAuth2ProviderRequest
from authentik.models.patched_o_auth_source_request import PatchedOAuthSourceRequest
from authentik.models.patched_outpost_request import PatchedOutpostRequest
from authentik.models.patched_password_expiry_policy_request import PatchedPasswordExpiryPolicyRequest
from authentik.models.patched_password_policy_request import PatchedPasswordPolicyRequest
from authentik.models.patched_password_stage_request import PatchedPasswordStageRequest
from authentik.models.patched_plex_source_connection_request import PatchedPlexSourceConnectionRequest
from authentik.models.patched_plex_source_request import PatchedPlexSourceRequest
from authentik.models.patched_policy_binding_request import PatchedPolicyBindingRequest
from authentik.models.patched_prompt_request import PatchedPromptRequest
from authentik.models.patched_prompt_stage_request import PatchedPromptStageRequest
from authentik.models.patched_proxy_provider_request import PatchedProxyProviderRequest
from authentik.models.patched_radius_provider_request import PatchedRadiusProviderRequest
from authentik.models.patched_reputation_policy_request import PatchedReputationPolicyRequest
from authentik.models.patched_saml_property_mapping_request import PatchedSAMLPropertyMappingRequest
from authentik.models.patched_saml_provider_request import PatchedSAMLProviderRequest
from authentik.models.patched_saml_source_request import PatchedSAMLSourceRequest
from authentik.models.patched_scim_mapping_request import PatchedSCIMMappingRequest
from authentik.models.patched_scim_provider_request import PatchedSCIMProviderRequest
from authentik.models.patched_sms_device_request import PatchedSMSDeviceRequest
from authentik.models.patched_scope_mapping_request import PatchedScopeMappingRequest
from authentik.models.patched_static_device_request import PatchedStaticDeviceRequest
from authentik.models.patched_totp_device_request import PatchedTOTPDeviceRequest
from authentik.models.patched_tenant_request import PatchedTenantRequest
from authentik.models.patched_token_request import PatchedTokenRequest
from authentik.models.patched_user_delete_stage_request import PatchedUserDeleteStageRequest
from authentik.models.patched_user_login_stage_request import PatchedUserLoginStageRequest
from authentik.models.patched_user_logout_stage_request import PatchedUserLogoutStageRequest
from authentik.models.patched_user_o_auth_source_connection_request import PatchedUserOAuthSourceConnectionRequest
from authentik.models.patched_user_request import PatchedUserRequest
from authentik.models.patched_user_saml_source_connection_request import PatchedUserSAMLSourceConnectionRequest
from authentik.models.patched_user_write_stage_request import PatchedUserWriteStageRequest
from authentik.models.patched_web_authn_device_request import PatchedWebAuthnDeviceRequest
from authentik.models.permission import Permission
from authentik.models.plex_authentication_challenge import PlexAuthenticationChallenge
from authentik.models.plex_authentication_challenge_response_request import PlexAuthenticationChallengeResponseRequest
from authentik.models.plex_source import PlexSource
from authentik.models.plex_source_connection import PlexSourceConnection
from authentik.models.plex_source_connection_request import PlexSourceConnectionRequest
from authentik.models.plex_source_request import PlexSourceRequest
from authentik.models.plex_token_redeem_request import PlexTokenRedeemRequest
from authentik.models.policy import Policy
from authentik.models.policy_binding import PolicyBinding
from authentik.models.policy_binding_request import PolicyBindingRequest
from authentik.models.policy_engine_mode import PolicyEngineMode
from authentik.models.policy_request import PolicyRequest
from authentik.models.policy_test_request import PolicyTestRequest
from authentik.models.policy_test_result import PolicyTestResult
from authentik.models.prompt import Prompt
from authentik.models.prompt_challenge import PromptChallenge
from authentik.models.prompt_challenge_response_request import PromptChallengeResponseRequest
from authentik.models.prompt_request import PromptRequest
from authentik.models.prompt_stage import PromptStage
from authentik.models.prompt_stage_request import PromptStageRequest
from authentik.models.prompt_type_enum import PromptTypeEnum
from authentik.models.property_mapping import PropertyMapping
from authentik.models.property_mapping_preview import PropertyMappingPreview
from authentik.models.property_mapping_test_result import PropertyMappingTestResult
from authentik.models.provider import Provider
from authentik.models.provider_enum import ProviderEnum
from authentik.models.provider_request import ProviderRequest
from authentik.models.provider_type_enum import ProviderTypeEnum
from authentik.models.proxy_mode import ProxyMode
from authentik.models.proxy_outpost_config import ProxyOutpostConfig
from authentik.models.proxy_provider import ProxyProvider
from authentik.models.proxy_provider_request import ProxyProviderRequest
from authentik.models.radius_outpost_config import RadiusOutpostConfig
from authentik.models.radius_provider import RadiusProvider
from authentik.models.radius_provider_request import RadiusProviderRequest
from authentik.models.redirect_challenge import RedirectChallenge
from authentik.models.reputation import Reputation
from authentik.models.reputation_policy import ReputationPolicy
from authentik.models.reputation_policy_request import ReputationPolicyRequest
from authentik.models.resident_key_requirement_enum import ResidentKeyRequirementEnum
from authentik.models.saml_metadata import SAMLMetadata
from authentik.models.saml_property_mapping import SAMLPropertyMapping
from authentik.models.saml_property_mapping_request import SAMLPropertyMappingRequest
from authentik.models.saml_provider import SAMLProvider
from authentik.models.saml_provider_request import SAMLProviderRequest
from authentik.models.saml_source import SAMLSource
from authentik.models.saml_source_request import SAMLSourceRequest
from authentik.models.scim_mapping import SCIMMapping
from authentik.models.scim_mapping_request import SCIMMappingRequest
from authentik.models.scim_provider import SCIMProvider
from authentik.models.scim_provider_request import SCIMProviderRequest
from authentik.models.sms_device import SMSDevice
from authentik.models.sms_device_request import SMSDeviceRequest
from authentik.models.scope_mapping import ScopeMapping
from authentik.models.scope_mapping_request import ScopeMappingRequest
from authentik.models.selectable_stage import SelectableStage
from authentik.models.service_connection import ServiceConnection
from authentik.models.service_connection_request import ServiceConnectionRequest
from authentik.models.service_connection_state import ServiceConnectionState
from authentik.models.session_user import SessionUser
from authentik.models.severity_enum import SeverityEnum
from authentik.models.shell_challenge import ShellChallenge
from authentik.models.signature_algorithm_enum import SignatureAlgorithmEnum
from authentik.models.source import Source
from authentik.models.source_request import SourceRequest
from authentik.models.source_type import SourceType
from authentik.models.sp_binding_enum import SpBindingEnum
from authentik.models.stage import Stage
from authentik.models.stage_prompt import StagePrompt
from authentik.models.stage_request import StageRequest
from authentik.models.static_device import StaticDevice
from authentik.models.static_device_request import StaticDeviceRequest
from authentik.models.static_device_token import StaticDeviceToken
from authentik.models.static_device_token_request import StaticDeviceTokenRequest
from authentik.models.sub_mode_enum import SubModeEnum
from authentik.models.system import System
from authentik.models.system_runtime import SystemRuntime
from authentik.models.totp_device import TOTPDevice
from authentik.models.totp_device_request import TOTPDeviceRequest
from authentik.models.task import Task
from authentik.models.task_status_enum import TaskStatusEnum
from authentik.models.tenant import Tenant
from authentik.models.tenant_request import TenantRequest
from authentik.models.token import Token
from authentik.models.token_model import TokenModel
from authentik.models.token_request import TokenRequest
from authentik.models.token_set_key_request import TokenSetKeyRequest
from authentik.models.token_view import TokenView
from authentik.models.type_create import TypeCreate
from authentik.models.ui_theme_enum import UiThemeEnum
from authentik.models.used_by import UsedBy
from authentik.models.used_by_action_enum import UsedByActionEnum
from authentik.models.user import User
from authentik.models.user_account_request import UserAccountRequest
from authentik.models.user_consent import UserConsent
from authentik.models.user_creation_mode_enum import UserCreationModeEnum
from authentik.models.user_delete_stage import UserDeleteStage
from authentik.models.user_delete_stage_request import UserDeleteStageRequest
from authentik.models.user_fields_enum import UserFieldsEnum
from authentik.models.user_group import UserGroup
from authentik.models.user_group_request import UserGroupRequest
from authentik.models.user_login_challenge import UserLoginChallenge
from authentik.models.user_login_challenge_response_request import UserLoginChallengeResponseRequest
from authentik.models.user_login_stage import UserLoginStage
from authentik.models.user_login_stage_request import UserLoginStageRequest
from authentik.models.user_logout_stage import UserLogoutStage
from authentik.models.user_logout_stage_request import UserLogoutStageRequest
from authentik.models.user_matching_mode_enum import UserMatchingModeEnum
from authentik.models.user_metrics import UserMetrics
from authentik.models.user_o_auth_source_connection import UserOAuthSourceConnection
from authentik.models.user_o_auth_source_connection_request import UserOAuthSourceConnectionRequest
from authentik.models.user_password_set_request import UserPasswordSetRequest
from authentik.models.user_path import UserPath
from authentik.models.user_request import UserRequest
from authentik.models.user_saml_source_connection import UserSAMLSourceConnection
from authentik.models.user_saml_source_connection_request import UserSAMLSourceConnectionRequest
from authentik.models.user_self import UserSelf
from authentik.models.user_self_groups import UserSelfGroups
from authentik.models.user_service_account_request import UserServiceAccountRequest
from authentik.models.user_service_account_response import UserServiceAccountResponse
from authentik.models.user_setting import UserSetting
from authentik.models.user_source_connection import UserSourceConnection
from authentik.models.user_type_enum import UserTypeEnum
from authentik.models.user_verification_enum import UserVerificationEnum
from authentik.models.user_write_stage import UserWriteStage
from authentik.models.user_write_stage_request import UserWriteStageRequest
from authentik.models.validation_error import ValidationError
from authentik.models.version import Version
from authentik.models.web_authn_device import WebAuthnDevice
from authentik.models.web_authn_device_request import WebAuthnDeviceRequest
from authentik.models.workers import Workers