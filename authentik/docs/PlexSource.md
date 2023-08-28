# PlexSource

Plex Source Serializer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **str** |  | [readonly] 
**name** | **str** | Source&#39;s display Name. | 
**slug** | **str** | Internal source name, used in URLs. | 
**enabled** | **bool** |  | [optional] 
**authentication_flow** | **str** | Flow to use when authenticating existing users. | [optional] 
**enrollment_flow** | **str** | Flow to use when enrolling new users. | [optional] 
**component** | **str** | Get object component so that we know how to edit the object | [readonly] 
**verbose_name** | **str** | Return object&#39;s verbose_name | [readonly] 
**verbose_name_plural** | **str** | Return object&#39;s plural verbose_name | [readonly] 
**meta_model_name** | **str** | Return internal model name | [readonly] 
**policy_engine_mode** | [**PolicyEngineMode**](PolicyEngineMode.md) |  | [optional] 
**user_matching_mode** | [**UserMatchingModeEnum**](UserMatchingModeEnum.md) |  | [optional] 
**managed** | **str** | Objects that are managed by authentik. These objects are created and updated automatically. This flag only indicates that an object can be overwritten by migrations. You can still modify the objects via the API, but expect changes to be overwritten in a later update. | [readonly] 
**user_path_template** | **str** |  | [optional] 
**icon** | **str** | Get the URL to the Icon. If the name is /static or starts with http it is returned as-is | [readonly] 
**client_id** | **str** | Client identifier used to talk to Plex. | [optional] 
**allowed_servers** | **List[str]** | Which servers a user has to be a member of to be granted access. Empty list allows every server. | [optional] 
**allow_friends** | **bool** | Allow friends to authenticate, even if you don&#39;t share a server. | [optional] 
**plex_token** | **str** | Plex token used to check friends | 

## Example

```python
from authentik.models.plex_source import PlexSource

# TODO update the JSON string below
json = "{}"
# create an instance of PlexSource from a JSON string
plex_source_instance = PlexSource.from_json(json)
# print the JSON string representation of the object
print PlexSource.to_json()

# convert the object into a dict
plex_source_dict = plex_source_instance.to_dict()
# create an instance of PlexSource from a dict
plex_source_form_dict = plex_source.from_dict(plex_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


