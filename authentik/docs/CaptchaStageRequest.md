# CaptchaStageRequest

CaptchaStage Serializer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**flow_set** | [**List[FlowSetRequest]**](FlowSetRequest.md) |  | [optional] 
**public_key** | **str** | Public key, acquired your captcha Provider. | 
**private_key** | **str** | Private key, acquired your captcha Provider. | 
**js_url** | **str** |  | [optional] 
**api_url** | **str** |  | [optional] 

## Example

```python
from authentik.models.captcha_stage_request import CaptchaStageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CaptchaStageRequest from a JSON string
captcha_stage_request_instance = CaptchaStageRequest.from_json(json)
# print the JSON string representation of the object
print CaptchaStageRequest.to_json()

# convert the object into a dict
captcha_stage_request_dict = captcha_stage_request_instance.to_dict()
# create an instance of CaptchaStageRequest from a dict
captcha_stage_request_form_dict = captcha_stage_request.from_dict(captcha_stage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


