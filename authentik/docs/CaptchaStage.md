# CaptchaStage

CaptchaStage Serializer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **str** |  | [readonly] 
**name** | **str** |  | 
**component** | **str** | Get object type so that we know how to edit the object | [readonly] 
**verbose_name** | **str** | Return object&#39;s verbose_name | [readonly] 
**verbose_name_plural** | **str** | Return object&#39;s plural verbose_name | [readonly] 
**meta_model_name** | **str** | Return internal model name | [readonly] 
**flow_set** | [**List[FlowSet]**](FlowSet.md) |  | [optional] 
**public_key** | **str** | Public key, acquired your captcha Provider. | 
**js_url** | **str** |  | [optional] 
**api_url** | **str** |  | [optional] 

## Example

```python
from authentik.models.captcha_stage import CaptchaStage

# TODO update the JSON string below
json = "{}"
# create an instance of CaptchaStage from a JSON string
captcha_stage_instance = CaptchaStage.from_json(json)
# print the JSON string representation of the object
print CaptchaStage.to_json()

# convert the object into a dict
captcha_stage_dict = captcha_stage_instance.to_dict()
# create an instance of CaptchaStage from a dict
captcha_stage_form_dict = captcha_stage.from_dict(captcha_stage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


