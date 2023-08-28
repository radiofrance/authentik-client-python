# WebAuthnDevice

Serializer for WebAuthn authenticator devices

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **int** |  | [readonly] 
**name** | **str** |  | 
**created_on** | **datetime** |  | [readonly] 

## Example

```python
from authentik.models.web_authn_device import WebAuthnDevice

# TODO update the JSON string below
json = "{}"
# create an instance of WebAuthnDevice from a JSON string
web_authn_device_instance = WebAuthnDevice.from_json(json)
# print the JSON string representation of the object
print WebAuthnDevice.to_json()

# convert the object into a dict
web_authn_device_dict = web_authn_device_instance.to_dict()
# create an instance of WebAuthnDevice from a dict
web_authn_device_form_dict = web_authn_device.from_dict(web_authn_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


