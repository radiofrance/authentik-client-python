# SystemRuntime

Get versions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**python_version** | **str** |  | 
**gunicorn_version** | **str** |  | 
**environment** | **str** |  | 
**architecture** | **str** |  | 
**platform** | **str** |  | 
**uname** | **str** |  | 

## Example

```python
from authentik.models.system_runtime import SystemRuntime

# TODO update the JSON string below
json = "{}"
# create an instance of SystemRuntime from a JSON string
system_runtime_instance = SystemRuntime.from_json(json)
# print the JSON string representation of the object
print SystemRuntime.to_json()

# convert the object into a dict
system_runtime_dict = system_runtime_instance.to_dict()
# create an instance of SystemRuntime from a dict
system_runtime_form_dict = system_runtime.from_dict(system_runtime_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


