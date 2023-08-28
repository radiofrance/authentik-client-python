# FlowRequest

Flow Serializer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**slug** | **str** | Visible in the URL. | 
**title** | **str** | Shown as the Title in Flow pages. | 
**designation** | [**FlowDesignationEnum**](FlowDesignationEnum.md) |  | 
**policy_engine_mode** | [**PolicyEngineMode**](PolicyEngineMode.md) |  | [optional] 
**compatibility_mode** | **bool** | Enable compatibility mode, increases compatibility with password managers on mobile devices. | [optional] 
**layout** | [**LayoutEnum**](LayoutEnum.md) |  | [optional] 
**denied_action** | [**DeniedActionEnum**](DeniedActionEnum.md) |  | [optional] 
**authentication** | [**AuthenticationEnum**](AuthenticationEnum.md) |  | [optional] 

## Example

```python
from authentik.models.flow_request import FlowRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FlowRequest from a JSON string
flow_request_instance = FlowRequest.from_json(json)
# print the JSON string representation of the object
print FlowRequest.to_json()

# convert the object into a dict
flow_request_dict = flow_request_instance.to_dict()
# create an instance of FlowRequest from a dict
flow_request_form_dict = flow_request.from_dict(flow_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


