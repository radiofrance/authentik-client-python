# PatchedEventMatcherPolicyRequest

Event Matcher Policy Serializer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**execution_logging** | **bool** | When this option is enabled, all executions of this policy will be logged. By default, only execution errors are logged. | [optional] 
**action** | [**EventActions**](EventActions.md) |  | [optional] 
**client_ip** | **str** | Matches Event&#39;s Client IP (strict matching, for network matching use an Expression Policy) | [optional] 
**app** | [**AppEnum**](AppEnum.md) |  | [optional] 
**model** | [**ModelEnum**](ModelEnum.md) |  | [optional] 

## Example

```python
from authentik.models.patched_event_matcher_policy_request import PatchedEventMatcherPolicyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedEventMatcherPolicyRequest from a JSON string
patched_event_matcher_policy_request_instance = PatchedEventMatcherPolicyRequest.from_json(json)
# print the JSON string representation of the object
print PatchedEventMatcherPolicyRequest.to_json()

# convert the object into a dict
patched_event_matcher_policy_request_dict = patched_event_matcher_policy_request_instance.to_dict()
# create an instance of PatchedEventMatcherPolicyRequest from a dict
patched_event_matcher_policy_request_form_dict = patched_event_matcher_policy_request.from_dict(patched_event_matcher_policy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


