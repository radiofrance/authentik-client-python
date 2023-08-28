# Flow

Flow Serializer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **str** |  | [readonly] 
**policybindingmodel_ptr_id** | **str** |  | [readonly] 
**name** | **str** |  | 
**slug** | **str** | Visible in the URL. | 
**title** | **str** | Shown as the Title in Flow pages. | 
**designation** | [**FlowDesignationEnum**](FlowDesignationEnum.md) |  | 
**background** | **str** | Get the URL to the background image. If the name is /static or starts with http it is returned as-is | [readonly] 
**stages** | **List[str]** |  | [readonly] 
**policies** | **List[str]** |  | [readonly] 
**cache_count** | **int** | Get count of cached flows | [readonly] 
**policy_engine_mode** | [**PolicyEngineMode**](PolicyEngineMode.md) |  | [optional] 
**compatibility_mode** | **bool** | Enable compatibility mode, increases compatibility with password managers on mobile devices. | [optional] 
**export_url** | **str** | Get export URL for flow | [readonly] 
**layout** | [**LayoutEnum**](LayoutEnum.md) |  | [optional] 
**denied_action** | [**DeniedActionEnum**](DeniedActionEnum.md) |  | [optional] 
**authentication** | [**AuthenticationEnum**](AuthenticationEnum.md) |  | [optional] 

## Example

```python
from authentik.models.flow import Flow

# TODO update the JSON string below
json = "{}"
# create an instance of Flow from a JSON string
flow_instance = Flow.from_json(json)
# print the JSON string representation of the object
print Flow.to_json()

# convert the object into a dict
flow_dict = flow_instance.to_dict()
# create an instance of Flow from a dict
flow_form_dict = flow.from_dict(flow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


