# System

Get system information.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**http_headers** | **Dict[str, str]** | Get HTTP Request headers | [readonly] 
**http_host** | **str** | Get HTTP host | [readonly] 
**http_is_secure** | **bool** | Get HTTP Secure flag | [readonly] 
**runtime** | [**SystemRuntime**](SystemRuntime.md) |  | 
**tenant** | **str** | Currently active tenant | [readonly] 
**server_time** | **datetime** | Current server time | [readonly] 
**embedded_outpost_host** | **str** | Get the FQDN configured on the embedded outpost | [readonly] 

## Example

```python
from authentik.models.system import System

# TODO update the JSON string below
json = "{}"
# create an instance of System from a JSON string
system_instance = System.from_json(json)
# print the JSON string representation of the object
print System.to_json()

# convert the object into a dict
system_dict = system_instance.to_dict()
# create an instance of System from a dict
system_form_dict = system.from_dict(system_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


