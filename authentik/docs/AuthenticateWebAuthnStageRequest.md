# AuthenticateWebAuthnStageRequest

AuthenticateWebAuthnStage Serializer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**flow_set** | [**List[FlowSetRequest]**](FlowSetRequest.md) |  | [optional] 
**configure_flow** | **str** | Flow used by an authenticated user to configure this Stage. If empty, user will not be able to configure this stage. | [optional] 
**friendly_name** | **str** |  | [optional] 
**user_verification** | [**UserVerificationEnum**](UserVerificationEnum.md) |  | [optional] 
**authenticator_attachment** | [**AuthenticatorAttachmentEnum**](AuthenticatorAttachmentEnum.md) |  | [optional] 
**resident_key_requirement** | [**ResidentKeyRequirementEnum**](ResidentKeyRequirementEnum.md) |  | [optional] 

## Example

```python
from authentik.models.authenticate_web_authn_stage_request import AuthenticateWebAuthnStageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticateWebAuthnStageRequest from a JSON string
authenticate_web_authn_stage_request_instance = AuthenticateWebAuthnStageRequest.from_json(json)
# print the JSON string representation of the object
print AuthenticateWebAuthnStageRequest.to_json()

# convert the object into a dict
authenticate_web_authn_stage_request_dict = authenticate_web_authn_stage_request_instance.to_dict()
# create an instance of AuthenticateWebAuthnStageRequest from a dict
authenticate_web_authn_stage_request_form_dict = authenticate_web_authn_stage_request.from_dict(authenticate_web_authn_stage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


