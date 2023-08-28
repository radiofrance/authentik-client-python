# PaginatedAuthenticateWebAuthnStageList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[AuthenticateWebAuthnStage]**](AuthenticateWebAuthnStage.md) |  | 

## Example

```python
from authentik.models.paginated_authenticate_web_authn_stage_list import PaginatedAuthenticateWebAuthnStageList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedAuthenticateWebAuthnStageList from a JSON string
paginated_authenticate_web_authn_stage_list_instance = PaginatedAuthenticateWebAuthnStageList.from_json(json)
# print the JSON string representation of the object
print PaginatedAuthenticateWebAuthnStageList.to_json()

# convert the object into a dict
paginated_authenticate_web_authn_stage_list_dict = paginated_authenticate_web_authn_stage_list_instance.to_dict()
# create an instance of PaginatedAuthenticateWebAuthnStageList from a dict
paginated_authenticate_web_authn_stage_list_form_dict = paginated_authenticate_web_authn_stage_list.from_dict(paginated_authenticate_web_authn_stage_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


