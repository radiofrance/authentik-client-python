# PatchedFlowRequest

Flow Serializer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**slug** | **str** | Visible in the URL. | [optional] 
**title** | **str** | Shown as the Title in Flow pages. | [optional] 
**designation** | [**FlowDesignationEnum**](FlowDesignationEnum.md) |  | [optional] 
**policy_engine_mode** | [**PolicyEngineMode**](PolicyEngineMode.md) |  | [optional] 
**compatibility_mode** | **bool** | Enable compatibility mode, increases compatibility with password managers on mobile devices. | [optional] 
**layout** | [**LayoutEnum**](LayoutEnum.md) |  | [optional] 
**denied_action** | [**DeniedActionEnum**](DeniedActionEnum.md) |  | [optional] 
**authentication** | [**AuthenticationEnum**](AuthenticationEnum.md) |  | [optional] 

## Example

```python
from authentik.models.patched_flow_request import PatchedFlowRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedFlowRequest from a JSON string
patched_flow_request_instance = PatchedFlowRequest.from_json(json)
# print the JSON string representation of the object
print PatchedFlowRequest.to_json()

# convert the object into a dict
patched_flow_request_dict = patched_flow_request_instance.to_dict()
# create an instance of PatchedFlowRequest from a dict
patched_flow_request_form_dict = patched_flow_request.from_dict(patched_flow_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


