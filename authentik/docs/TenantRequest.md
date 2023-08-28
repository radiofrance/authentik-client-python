# TenantRequest

Tenant Serializer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | Domain that activates this tenant. Can be a superset, i.e. &#x60;a.b&#x60; for &#x60;aa.b&#x60; and &#x60;ba.b&#x60; | 
**default** | **bool** |  | [optional] 
**branding_title** | **str** |  | [optional] 
**branding_logo** | **str** |  | [optional] 
**branding_favicon** | **str** |  | [optional] 
**flow_authentication** | **str** |  | [optional] 
**flow_invalidation** | **str** |  | [optional] 
**flow_recovery** | **str** |  | [optional] 
**flow_unenrollment** | **str** |  | [optional] 
**flow_user_settings** | **str** |  | [optional] 
**flow_device_code** | **str** |  | [optional] 
**event_retention** | **str** | Events will be deleted after this duration.(Format: weeks&#x3D;3;days&#x3D;2;hours&#x3D;3,seconds&#x3D;2). | [optional] 
**web_certificate** | **str** | Web Certificate used by the authentik Core webserver. | [optional] 
**attributes** | **Dict[str, object]** |  | [optional] 

## Example

```python
from authentik.models.tenant_request import TenantRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TenantRequest from a JSON string
tenant_request_instance = TenantRequest.from_json(json)
# print the JSON string representation of the object
print TenantRequest.to_json()

# convert the object into a dict
tenant_request_dict = tenant_request_instance.to_dict()
# create an instance of TenantRequest from a dict
tenant_request_form_dict = tenant_request.from_dict(tenant_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


