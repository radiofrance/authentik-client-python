# CurrentTenant

Partial tenant information for styling

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**matched_domain** | **str** |  | 
**branding_title** | **str** |  | 
**branding_logo** | **str** |  | 
**branding_favicon** | **str** |  | 
**ui_footer_links** | [**List[FooterLink]**](FooterLink.md) |  | [readonly] [default to []]
**ui_theme** | [**UiThemeEnum**](UiThemeEnum.md) |  | [readonly] 
**flow_authentication** | **str** |  | [optional] 
**flow_invalidation** | **str** |  | [optional] 
**flow_recovery** | **str** |  | [optional] 
**flow_unenrollment** | **str** |  | [optional] 
**flow_user_settings** | **str** |  | [optional] 
**flow_device_code** | **str** |  | [optional] 
**default_locale** | **str** |  | [readonly] 

## Example

```python
from authentik.models.current_tenant import CurrentTenant

# TODO update the JSON string below
json = "{}"
# create an instance of CurrentTenant from a JSON string
current_tenant_instance = CurrentTenant.from_json(json)
# print the JSON string representation of the object
print CurrentTenant.to_json()

# convert the object into a dict
current_tenant_dict = current_tenant_instance.to_dict()
# create an instance of CurrentTenant from a dict
current_tenant_form_dict = current_tenant.from_dict(current_tenant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


