# authentik.SourcesApi

All URIs are relative to *http://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sources_all_destroy**](SourcesApi.md#sources_all_destroy) | **DELETE** /sources/all/{slug}/ | 
[**sources_all_list**](SourcesApi.md#sources_all_list) | **GET** /sources/all/ | 
[**sources_all_retrieve**](SourcesApi.md#sources_all_retrieve) | **GET** /sources/all/{slug}/ | 
[**sources_all_set_icon_create**](SourcesApi.md#sources_all_set_icon_create) | **POST** /sources/all/{slug}/set_icon/ | 
[**sources_all_set_icon_url_create**](SourcesApi.md#sources_all_set_icon_url_create) | **POST** /sources/all/{slug}/set_icon_url/ | 
[**sources_all_types_list**](SourcesApi.md#sources_all_types_list) | **GET** /sources/all/types/ | 
[**sources_all_used_by_list**](SourcesApi.md#sources_all_used_by_list) | **GET** /sources/all/{slug}/used_by/ | 
[**sources_all_user_settings_list**](SourcesApi.md#sources_all_user_settings_list) | **GET** /sources/all/user_settings/ | 
[**sources_ldap_create**](SourcesApi.md#sources_ldap_create) | **POST** /sources/ldap/ | 
[**sources_ldap_debug_retrieve**](SourcesApi.md#sources_ldap_debug_retrieve) | **GET** /sources/ldap/{slug}/debug/ | 
[**sources_ldap_destroy**](SourcesApi.md#sources_ldap_destroy) | **DELETE** /sources/ldap/{slug}/ | 
[**sources_ldap_list**](SourcesApi.md#sources_ldap_list) | **GET** /sources/ldap/ | 
[**sources_ldap_partial_update**](SourcesApi.md#sources_ldap_partial_update) | **PATCH** /sources/ldap/{slug}/ | 
[**sources_ldap_retrieve**](SourcesApi.md#sources_ldap_retrieve) | **GET** /sources/ldap/{slug}/ | 
[**sources_ldap_sync_status_list**](SourcesApi.md#sources_ldap_sync_status_list) | **GET** /sources/ldap/{slug}/sync_status/ | 
[**sources_ldap_update**](SourcesApi.md#sources_ldap_update) | **PUT** /sources/ldap/{slug}/ | 
[**sources_ldap_used_by_list**](SourcesApi.md#sources_ldap_used_by_list) | **GET** /sources/ldap/{slug}/used_by/ | 
[**sources_oauth_create**](SourcesApi.md#sources_oauth_create) | **POST** /sources/oauth/ | 
[**sources_oauth_destroy**](SourcesApi.md#sources_oauth_destroy) | **DELETE** /sources/oauth/{slug}/ | 
[**sources_oauth_list**](SourcesApi.md#sources_oauth_list) | **GET** /sources/oauth/ | 
[**sources_oauth_partial_update**](SourcesApi.md#sources_oauth_partial_update) | **PATCH** /sources/oauth/{slug}/ | 
[**sources_oauth_retrieve**](SourcesApi.md#sources_oauth_retrieve) | **GET** /sources/oauth/{slug}/ | 
[**sources_oauth_source_types_list**](SourcesApi.md#sources_oauth_source_types_list) | **GET** /sources/oauth/source_types/ | 
[**sources_oauth_update**](SourcesApi.md#sources_oauth_update) | **PUT** /sources/oauth/{slug}/ | 
[**sources_oauth_used_by_list**](SourcesApi.md#sources_oauth_used_by_list) | **GET** /sources/oauth/{slug}/used_by/ | 
[**sources_plex_create**](SourcesApi.md#sources_plex_create) | **POST** /sources/plex/ | 
[**sources_plex_destroy**](SourcesApi.md#sources_plex_destroy) | **DELETE** /sources/plex/{slug}/ | 
[**sources_plex_list**](SourcesApi.md#sources_plex_list) | **GET** /sources/plex/ | 
[**sources_plex_partial_update**](SourcesApi.md#sources_plex_partial_update) | **PATCH** /sources/plex/{slug}/ | 
[**sources_plex_redeem_token_authenticated_create**](SourcesApi.md#sources_plex_redeem_token_authenticated_create) | **POST** /sources/plex/redeem_token_authenticated/ | 
[**sources_plex_redeem_token_create**](SourcesApi.md#sources_plex_redeem_token_create) | **POST** /sources/plex/redeem_token/ | 
[**sources_plex_retrieve**](SourcesApi.md#sources_plex_retrieve) | **GET** /sources/plex/{slug}/ | 
[**sources_plex_update**](SourcesApi.md#sources_plex_update) | **PUT** /sources/plex/{slug}/ | 
[**sources_plex_used_by_list**](SourcesApi.md#sources_plex_used_by_list) | **GET** /sources/plex/{slug}/used_by/ | 
[**sources_saml_create**](SourcesApi.md#sources_saml_create) | **POST** /sources/saml/ | 
[**sources_saml_destroy**](SourcesApi.md#sources_saml_destroy) | **DELETE** /sources/saml/{slug}/ | 
[**sources_saml_list**](SourcesApi.md#sources_saml_list) | **GET** /sources/saml/ | 
[**sources_saml_metadata_retrieve**](SourcesApi.md#sources_saml_metadata_retrieve) | **GET** /sources/saml/{slug}/metadata/ | 
[**sources_saml_partial_update**](SourcesApi.md#sources_saml_partial_update) | **PATCH** /sources/saml/{slug}/ | 
[**sources_saml_retrieve**](SourcesApi.md#sources_saml_retrieve) | **GET** /sources/saml/{slug}/ | 
[**sources_saml_update**](SourcesApi.md#sources_saml_update) | **PUT** /sources/saml/{slug}/ | 
[**sources_saml_used_by_list**](SourcesApi.md#sources_saml_used_by_list) | **GET** /sources/saml/{slug}/used_by/ | 
[**sources_user_connections_all_destroy**](SourcesApi.md#sources_user_connections_all_destroy) | **DELETE** /sources/user_connections/all/{id}/ | 
[**sources_user_connections_all_list**](SourcesApi.md#sources_user_connections_all_list) | **GET** /sources/user_connections/all/ | 
[**sources_user_connections_all_partial_update**](SourcesApi.md#sources_user_connections_all_partial_update) | **PATCH** /sources/user_connections/all/{id}/ | 
[**sources_user_connections_all_retrieve**](SourcesApi.md#sources_user_connections_all_retrieve) | **GET** /sources/user_connections/all/{id}/ | 
[**sources_user_connections_all_update**](SourcesApi.md#sources_user_connections_all_update) | **PUT** /sources/user_connections/all/{id}/ | 
[**sources_user_connections_all_used_by_list**](SourcesApi.md#sources_user_connections_all_used_by_list) | **GET** /sources/user_connections/all/{id}/used_by/ | 
[**sources_user_connections_oauth_create**](SourcesApi.md#sources_user_connections_oauth_create) | **POST** /sources/user_connections/oauth/ | 
[**sources_user_connections_oauth_destroy**](SourcesApi.md#sources_user_connections_oauth_destroy) | **DELETE** /sources/user_connections/oauth/{id}/ | 
[**sources_user_connections_oauth_list**](SourcesApi.md#sources_user_connections_oauth_list) | **GET** /sources/user_connections/oauth/ | 
[**sources_user_connections_oauth_partial_update**](SourcesApi.md#sources_user_connections_oauth_partial_update) | **PATCH** /sources/user_connections/oauth/{id}/ | 
[**sources_user_connections_oauth_retrieve**](SourcesApi.md#sources_user_connections_oauth_retrieve) | **GET** /sources/user_connections/oauth/{id}/ | 
[**sources_user_connections_oauth_update**](SourcesApi.md#sources_user_connections_oauth_update) | **PUT** /sources/user_connections/oauth/{id}/ | 
[**sources_user_connections_oauth_used_by_list**](SourcesApi.md#sources_user_connections_oauth_used_by_list) | **GET** /sources/user_connections/oauth/{id}/used_by/ | 
[**sources_user_connections_plex_create**](SourcesApi.md#sources_user_connections_plex_create) | **POST** /sources/user_connections/plex/ | 
[**sources_user_connections_plex_destroy**](SourcesApi.md#sources_user_connections_plex_destroy) | **DELETE** /sources/user_connections/plex/{id}/ | 
[**sources_user_connections_plex_list**](SourcesApi.md#sources_user_connections_plex_list) | **GET** /sources/user_connections/plex/ | 
[**sources_user_connections_plex_partial_update**](SourcesApi.md#sources_user_connections_plex_partial_update) | **PATCH** /sources/user_connections/plex/{id}/ | 
[**sources_user_connections_plex_retrieve**](SourcesApi.md#sources_user_connections_plex_retrieve) | **GET** /sources/user_connections/plex/{id}/ | 
[**sources_user_connections_plex_update**](SourcesApi.md#sources_user_connections_plex_update) | **PUT** /sources/user_connections/plex/{id}/ | 
[**sources_user_connections_plex_used_by_list**](SourcesApi.md#sources_user_connections_plex_used_by_list) | **GET** /sources/user_connections/plex/{id}/used_by/ | 
[**sources_user_connections_saml_create**](SourcesApi.md#sources_user_connections_saml_create) | **POST** /sources/user_connections/saml/ | 
[**sources_user_connections_saml_destroy**](SourcesApi.md#sources_user_connections_saml_destroy) | **DELETE** /sources/user_connections/saml/{id}/ | 
[**sources_user_connections_saml_list**](SourcesApi.md#sources_user_connections_saml_list) | **GET** /sources/user_connections/saml/ | 
[**sources_user_connections_saml_partial_update**](SourcesApi.md#sources_user_connections_saml_partial_update) | **PATCH** /sources/user_connections/saml/{id}/ | 
[**sources_user_connections_saml_retrieve**](SourcesApi.md#sources_user_connections_saml_retrieve) | **GET** /sources/user_connections/saml/{id}/ | 
[**sources_user_connections_saml_update**](SourcesApi.md#sources_user_connections_saml_update) | **PUT** /sources/user_connections/saml/{id}/ | 
[**sources_user_connections_saml_used_by_list**](SourcesApi.md#sources_user_connections_saml_used_by_list) | **GET** /sources/user_connections/saml/{id}/used_by/ | 


# **sources_all_destroy**
> sources_all_destroy(slug)



Source Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    slug = 'slug_example' # str | 

    try:
        api_instance.sources_all_destroy(slug)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_all_destroy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_all_list**
> PaginatedSourceList sources_all_list(managed=managed, name=name, ordering=ordering, page=page, page_size=page_size, search=search, slug=slug)



Source Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.paginated_source_list import PaginatedSourceList
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    managed = 'managed_example' # str |  (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)
    slug = 'slug_example' # str |  (optional)

    try:
        api_response = api_instance.sources_all_list(managed=managed, name=name, ordering=ordering, page=page, page_size=page_size, search=search, slug=slug)
        print("The response of SourcesApi->sources_all_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_all_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **managed** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **slug** | **str**|  | [optional] 

### Return type

[**PaginatedSourceList**](PaginatedSourceList.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_all_retrieve**
> Source sources_all_retrieve(slug)



Source Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.source import Source
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    slug = 'slug_example' # str | 

    try:
        api_response = api_instance.sources_all_retrieve(slug)
        print("The response of SourcesApi->sources_all_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_all_retrieve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

### Return type

[**Source**](Source.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_all_set_icon_create**
> sources_all_set_icon_create(slug, file=file, clear=clear)



Set source icon

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    slug = 'slug_example' # str | 
    file = None # bytearray |  (optional)
    clear = False # bool |  (optional) (default to False)

    try:
        api_instance.sources_all_set_icon_create(slug, file=file, clear=clear)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_all_set_icon_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **file** | **bytearray**|  | [optional] 
 **clear** | **bool**|  | [optional] [default to False]

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_all_set_icon_url_create**
> sources_all_set_icon_url_create(slug, file_path_request)



Set source icon (as URL)

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.file_path_request import FilePathRequest
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    slug = 'slug_example' # str | 
    file_path_request = authentik.FilePathRequest() # FilePathRequest | 

    try:
        api_instance.sources_all_set_icon_url_create(slug, file_path_request)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_all_set_icon_url_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **file_path_request** | [**FilePathRequest**](FilePathRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_all_types_list**
> List[TypeCreate] sources_all_types_list()



Get all creatable source types

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.type_create import TypeCreate
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)

    try:
        api_response = api_instance.sources_all_types_list()
        print("The response of SourcesApi->sources_all_types_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_all_types_list: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[TypeCreate]**](TypeCreate.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_all_used_by_list**
> List[UsedBy] sources_all_used_by_list(slug)



Get a list of all objects that use this object

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.used_by import UsedBy
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    slug = 'slug_example' # str | 

    try:
        api_response = api_instance.sources_all_used_by_list(slug)
        print("The response of SourcesApi->sources_all_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_all_used_by_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

### Return type

[**List[UsedBy]**](UsedBy.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_all_user_settings_list**
> List[UserSetting] sources_all_user_settings_list()



Get all sources the user can configure

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.user_setting import UserSetting
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)

    try:
        api_response = api_instance.sources_all_user_settings_list()
        print("The response of SourcesApi->sources_all_user_settings_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_all_user_settings_list: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[UserSetting]**](UserSetting.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_ldap_create**
> LDAPSource sources_ldap_create(ldap_source_request)



LDAP Source Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.ldap_source import LDAPSource
from authentik.models.ldap_source_request import LDAPSourceRequest
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    ldap_source_request = authentik.LDAPSourceRequest() # LDAPSourceRequest | 

    try:
        api_response = api_instance.sources_ldap_create(ldap_source_request)
        print("The response of SourcesApi->sources_ldap_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_ldap_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ldap_source_request** | [**LDAPSourceRequest**](LDAPSourceRequest.md)|  | 

### Return type

[**LDAPSource**](LDAPSource.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_ldap_debug_retrieve**
> LDAPDebug sources_ldap_debug_retrieve(slug)



Get raw LDAP data to debug

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.ldap_debug import LDAPDebug
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    slug = 'slug_example' # str | 

    try:
        api_response = api_instance.sources_ldap_debug_retrieve(slug)
        print("The response of SourcesApi->sources_ldap_debug_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_ldap_debug_retrieve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

### Return type

[**LDAPDebug**](LDAPDebug.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_ldap_destroy**
> sources_ldap_destroy(slug)



LDAP Source Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    slug = 'slug_example' # str | 

    try:
        api_instance.sources_ldap_destroy(slug)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_ldap_destroy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_ldap_list**
> PaginatedLDAPSourceList sources_ldap_list(additional_group_dn=additional_group_dn, additional_user_dn=additional_user_dn, base_dn=base_dn, bind_cn=bind_cn, client_certificate=client_certificate, enabled=enabled, group_membership_field=group_membership_field, group_object_filter=group_object_filter, name=name, object_uniqueness_field=object_uniqueness_field, ordering=ordering, page=page, page_size=page_size, peer_certificate=peer_certificate, property_mappings=property_mappings, property_mappings_group=property_mappings_group, search=search, server_uri=server_uri, slug=slug, sni=sni, start_tls=start_tls, sync_groups=sync_groups, sync_parent_group=sync_parent_group, sync_users=sync_users, sync_users_password=sync_users_password, user_object_filter=user_object_filter)



LDAP Source Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.paginated_ldap_source_list import PaginatedLDAPSourceList
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    additional_group_dn = 'additional_group_dn_example' # str |  (optional)
    additional_user_dn = 'additional_user_dn_example' # str |  (optional)
    base_dn = 'base_dn_example' # str |  (optional)
    bind_cn = 'bind_cn_example' # str |  (optional)
    client_certificate = 'client_certificate_example' # str |  (optional)
    enabled = True # bool |  (optional)
    group_membership_field = 'group_membership_field_example' # str |  (optional)
    group_object_filter = 'group_object_filter_example' # str |  (optional)
    name = 'name_example' # str |  (optional)
    object_uniqueness_field = 'object_uniqueness_field_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    peer_certificate = 'peer_certificate_example' # str |  (optional)
    property_mappings = ['property_mappings_example'] # List[str] |  (optional)
    property_mappings_group = ['property_mappings_group_example'] # List[str] |  (optional)
    search = 'search_example' # str | A search term. (optional)
    server_uri = 'server_uri_example' # str |  (optional)
    slug = 'slug_example' # str |  (optional)
    sni = True # bool |  (optional)
    start_tls = True # bool |  (optional)
    sync_groups = True # bool |  (optional)
    sync_parent_group = 'sync_parent_group_example' # str |  (optional)
    sync_users = True # bool |  (optional)
    sync_users_password = True # bool |  (optional)
    user_object_filter = 'user_object_filter_example' # str |  (optional)

    try:
        api_response = api_instance.sources_ldap_list(additional_group_dn=additional_group_dn, additional_user_dn=additional_user_dn, base_dn=base_dn, bind_cn=bind_cn, client_certificate=client_certificate, enabled=enabled, group_membership_field=group_membership_field, group_object_filter=group_object_filter, name=name, object_uniqueness_field=object_uniqueness_field, ordering=ordering, page=page, page_size=page_size, peer_certificate=peer_certificate, property_mappings=property_mappings, property_mappings_group=property_mappings_group, search=search, server_uri=server_uri, slug=slug, sni=sni, start_tls=start_tls, sync_groups=sync_groups, sync_parent_group=sync_parent_group, sync_users=sync_users, sync_users_password=sync_users_password, user_object_filter=user_object_filter)
        print("The response of SourcesApi->sources_ldap_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_ldap_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **additional_group_dn** | **str**|  | [optional] 
 **additional_user_dn** | **str**|  | [optional] 
 **base_dn** | **str**|  | [optional] 
 **bind_cn** | **str**|  | [optional] 
 **client_certificate** | **str**|  | [optional] 
 **enabled** | **bool**|  | [optional] 
 **group_membership_field** | **str**|  | [optional] 
 **group_object_filter** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **object_uniqueness_field** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **peer_certificate** | **str**|  | [optional] 
 **property_mappings** | [**List[str]**](str.md)|  | [optional] 
 **property_mappings_group** | [**List[str]**](str.md)|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **server_uri** | **str**|  | [optional] 
 **slug** | **str**|  | [optional] 
 **sni** | **bool**|  | [optional] 
 **start_tls** | **bool**|  | [optional] 
 **sync_groups** | **bool**|  | [optional] 
 **sync_parent_group** | **str**|  | [optional] 
 **sync_users** | **bool**|  | [optional] 
 **sync_users_password** | **bool**|  | [optional] 
 **user_object_filter** | **str**|  | [optional] 

### Return type

[**PaginatedLDAPSourceList**](PaginatedLDAPSourceList.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_ldap_partial_update**
> LDAPSource sources_ldap_partial_update(slug, patched_ldap_source_request=patched_ldap_source_request)



LDAP Source Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.ldap_source import LDAPSource
from authentik.models.patched_ldap_source_request import PatchedLDAPSourceRequest
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    slug = 'slug_example' # str | 
    patched_ldap_source_request = authentik.PatchedLDAPSourceRequest() # PatchedLDAPSourceRequest |  (optional)

    try:
        api_response = api_instance.sources_ldap_partial_update(slug, patched_ldap_source_request=patched_ldap_source_request)
        print("The response of SourcesApi->sources_ldap_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_ldap_partial_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **patched_ldap_source_request** | [**PatchedLDAPSourceRequest**](PatchedLDAPSourceRequest.md)|  | [optional] 

### Return type

[**LDAPSource**](LDAPSource.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_ldap_retrieve**
> LDAPSource sources_ldap_retrieve(slug)



LDAP Source Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.ldap_source import LDAPSource
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    slug = 'slug_example' # str | 

    try:
        api_response = api_instance.sources_ldap_retrieve(slug)
        print("The response of SourcesApi->sources_ldap_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_ldap_retrieve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

### Return type

[**LDAPSource**](LDAPSource.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_ldap_sync_status_list**
> List[Task] sources_ldap_sync_status_list(slug)



Get source's sync status

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.task import Task
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    slug = 'slug_example' # str | 

    try:
        api_response = api_instance.sources_ldap_sync_status_list(slug)
        print("The response of SourcesApi->sources_ldap_sync_status_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_ldap_sync_status_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

### Return type

[**List[Task]**](Task.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_ldap_update**
> LDAPSource sources_ldap_update(slug, ldap_source_request)



LDAP Source Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.ldap_source import LDAPSource
from authentik.models.ldap_source_request import LDAPSourceRequest
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    slug = 'slug_example' # str | 
    ldap_source_request = authentik.LDAPSourceRequest() # LDAPSourceRequest | 

    try:
        api_response = api_instance.sources_ldap_update(slug, ldap_source_request)
        print("The response of SourcesApi->sources_ldap_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_ldap_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **ldap_source_request** | [**LDAPSourceRequest**](LDAPSourceRequest.md)|  | 

### Return type

[**LDAPSource**](LDAPSource.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_ldap_used_by_list**
> List[UsedBy] sources_ldap_used_by_list(slug)



Get a list of all objects that use this object

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.used_by import UsedBy
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    slug = 'slug_example' # str | 

    try:
        api_response = api_instance.sources_ldap_used_by_list(slug)
        print("The response of SourcesApi->sources_ldap_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_ldap_used_by_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

### Return type

[**List[UsedBy]**](UsedBy.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_oauth_create**
> OAuthSource sources_oauth_create(o_auth_source_request)



Source Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.o_auth_source import OAuthSource
from authentik.models.o_auth_source_request import OAuthSourceRequest
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    o_auth_source_request = authentik.OAuthSourceRequest() # OAuthSourceRequest | 

    try:
        api_response = api_instance.sources_oauth_create(o_auth_source_request)
        print("The response of SourcesApi->sources_oauth_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_oauth_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **o_auth_source_request** | [**OAuthSourceRequest**](OAuthSourceRequest.md)|  | 

### Return type

[**OAuthSource**](OAuthSource.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_oauth_destroy**
> sources_oauth_destroy(slug)



Source Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    slug = 'slug_example' # str | 

    try:
        api_instance.sources_oauth_destroy(slug)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_oauth_destroy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_oauth_list**
> PaginatedOAuthSourceList sources_oauth_list(access_token_url=access_token_url, additional_scopes=additional_scopes, authentication_flow=authentication_flow, authorization_url=authorization_url, consumer_key=consumer_key, enabled=enabled, enrollment_flow=enrollment_flow, has_jwks=has_jwks, name=name, ordering=ordering, page=page, page_size=page_size, policy_engine_mode=policy_engine_mode, profile_url=profile_url, provider_type=provider_type, request_token_url=request_token_url, search=search, slug=slug, user_matching_mode=user_matching_mode)



Source Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.paginated_o_auth_source_list import PaginatedOAuthSourceList
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    access_token_url = 'access_token_url_example' # str |  (optional)
    additional_scopes = 'additional_scopes_example' # str |  (optional)
    authentication_flow = 'authentication_flow_example' # str |  (optional)
    authorization_url = 'authorization_url_example' # str |  (optional)
    consumer_key = 'consumer_key_example' # str |  (optional)
    enabled = True # bool |  (optional)
    enrollment_flow = 'enrollment_flow_example' # str |  (optional)
    has_jwks = True # bool | Only return sources with JWKS data (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    policy_engine_mode = 'policy_engine_mode_example' # str | * `all` - all, all policies must pass * `any` - any, any policy must pass (optional)
    profile_url = 'profile_url_example' # str |  (optional)
    provider_type = 'provider_type_example' # str |  (optional)
    request_token_url = 'request_token_url_example' # str |  (optional)
    search = 'search_example' # str | A search term. (optional)
    slug = 'slug_example' # str |  (optional)
    user_matching_mode = 'user_matching_mode_example' # str | How the source determines if an existing user should be authenticated or a new user enrolled.  * `identifier` - Use the source-specific identifier * `email_link` - Link to a user with identical email address. Can have security implications when a source doesn't validate email addresses. * `email_deny` - Use the user's email address, but deny enrollment when the email address already exists. * `username_link` - Link to a user with identical username. Can have security implications when a username is used with another source. * `username_deny` - Use the user's username, but deny enrollment when the username already exists. (optional)

    try:
        api_response = api_instance.sources_oauth_list(access_token_url=access_token_url, additional_scopes=additional_scopes, authentication_flow=authentication_flow, authorization_url=authorization_url, consumer_key=consumer_key, enabled=enabled, enrollment_flow=enrollment_flow, has_jwks=has_jwks, name=name, ordering=ordering, page=page, page_size=page_size, policy_engine_mode=policy_engine_mode, profile_url=profile_url, provider_type=provider_type, request_token_url=request_token_url, search=search, slug=slug, user_matching_mode=user_matching_mode)
        print("The response of SourcesApi->sources_oauth_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_oauth_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token_url** | **str**|  | [optional] 
 **additional_scopes** | **str**|  | [optional] 
 **authentication_flow** | **str**|  | [optional] 
 **authorization_url** | **str**|  | [optional] 
 **consumer_key** | **str**|  | [optional] 
 **enabled** | **bool**|  | [optional] 
 **enrollment_flow** | **str**|  | [optional] 
 **has_jwks** | **bool**| Only return sources with JWKS data | [optional] 
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **policy_engine_mode** | **str**| * &#x60;all&#x60; - all, all policies must pass * &#x60;any&#x60; - any, any policy must pass | [optional] 
 **profile_url** | **str**|  | [optional] 
 **provider_type** | **str**|  | [optional] 
 **request_token_url** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **slug** | **str**|  | [optional] 
 **user_matching_mode** | **str**| How the source determines if an existing user should be authenticated or a new user enrolled.  * &#x60;identifier&#x60; - Use the source-specific identifier * &#x60;email_link&#x60; - Link to a user with identical email address. Can have security implications when a source doesn&#39;t validate email addresses. * &#x60;email_deny&#x60; - Use the user&#39;s email address, but deny enrollment when the email address already exists. * &#x60;username_link&#x60; - Link to a user with identical username. Can have security implications when a username is used with another source. * &#x60;username_deny&#x60; - Use the user&#39;s username, but deny enrollment when the username already exists. | [optional] 

### Return type

[**PaginatedOAuthSourceList**](PaginatedOAuthSourceList.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_oauth_partial_update**
> OAuthSource sources_oauth_partial_update(slug, patched_o_auth_source_request=patched_o_auth_source_request)



Source Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.o_auth_source import OAuthSource
from authentik.models.patched_o_auth_source_request import PatchedOAuthSourceRequest
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    slug = 'slug_example' # str | 
    patched_o_auth_source_request = authentik.PatchedOAuthSourceRequest() # PatchedOAuthSourceRequest |  (optional)

    try:
        api_response = api_instance.sources_oauth_partial_update(slug, patched_o_auth_source_request=patched_o_auth_source_request)
        print("The response of SourcesApi->sources_oauth_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_oauth_partial_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **patched_o_auth_source_request** | [**PatchedOAuthSourceRequest**](PatchedOAuthSourceRequest.md)|  | [optional] 

### Return type

[**OAuthSource**](OAuthSource.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_oauth_retrieve**
> OAuthSource sources_oauth_retrieve(slug)



Source Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.o_auth_source import OAuthSource
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    slug = 'slug_example' # str | 

    try:
        api_response = api_instance.sources_oauth_retrieve(slug)
        print("The response of SourcesApi->sources_oauth_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_oauth_retrieve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

### Return type

[**OAuthSource**](OAuthSource.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_oauth_source_types_list**
> List[SourceType] sources_oauth_source_types_list(name=name)



Get all creatable source types. If ?name is set, only returns the type for <name>. If <name> isn't found, returns the default type.

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.source_type import SourceType
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    name = 'name_example' # str |  (optional)

    try:
        api_response = api_instance.sources_oauth_source_types_list(name=name)
        print("The response of SourcesApi->sources_oauth_source_types_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_oauth_source_types_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 

### Return type

[**List[SourceType]**](SourceType.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_oauth_update**
> OAuthSource sources_oauth_update(slug, o_auth_source_request)



Source Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.o_auth_source import OAuthSource
from authentik.models.o_auth_source_request import OAuthSourceRequest
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    slug = 'slug_example' # str | 
    o_auth_source_request = authentik.OAuthSourceRequest() # OAuthSourceRequest | 

    try:
        api_response = api_instance.sources_oauth_update(slug, o_auth_source_request)
        print("The response of SourcesApi->sources_oauth_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_oauth_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **o_auth_source_request** | [**OAuthSourceRequest**](OAuthSourceRequest.md)|  | 

### Return type

[**OAuthSource**](OAuthSource.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_oauth_used_by_list**
> List[UsedBy] sources_oauth_used_by_list(slug)



Get a list of all objects that use this object

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.used_by import UsedBy
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    slug = 'slug_example' # str | 

    try:
        api_response = api_instance.sources_oauth_used_by_list(slug)
        print("The response of SourcesApi->sources_oauth_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_oauth_used_by_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

### Return type

[**List[UsedBy]**](UsedBy.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_plex_create**
> PlexSource sources_plex_create(plex_source_request)



Plex source Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.plex_source import PlexSource
from authentik.models.plex_source_request import PlexSourceRequest
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    plex_source_request = authentik.PlexSourceRequest() # PlexSourceRequest | 

    try:
        api_response = api_instance.sources_plex_create(plex_source_request)
        print("The response of SourcesApi->sources_plex_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_plex_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plex_source_request** | [**PlexSourceRequest**](PlexSourceRequest.md)|  | 

### Return type

[**PlexSource**](PlexSource.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_plex_destroy**
> sources_plex_destroy(slug)



Plex source Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    slug = 'slug_example' # str | 

    try:
        api_instance.sources_plex_destroy(slug)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_plex_destroy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_plex_list**
> PaginatedPlexSourceList sources_plex_list(allow_friends=allow_friends, authentication_flow=authentication_flow, client_id=client_id, enabled=enabled, enrollment_flow=enrollment_flow, name=name, ordering=ordering, page=page, page_size=page_size, policy_engine_mode=policy_engine_mode, search=search, slug=slug, user_matching_mode=user_matching_mode)



Plex source Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.paginated_plex_source_list import PaginatedPlexSourceList
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    allow_friends = True # bool |  (optional)
    authentication_flow = 'authentication_flow_example' # str |  (optional)
    client_id = 'client_id_example' # str |  (optional)
    enabled = True # bool |  (optional)
    enrollment_flow = 'enrollment_flow_example' # str |  (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    policy_engine_mode = 'policy_engine_mode_example' # str | * `all` - all, all policies must pass * `any` - any, any policy must pass (optional)
    search = 'search_example' # str | A search term. (optional)
    slug = 'slug_example' # str |  (optional)
    user_matching_mode = 'user_matching_mode_example' # str | How the source determines if an existing user should be authenticated or a new user enrolled.  * `identifier` - Use the source-specific identifier * `email_link` - Link to a user with identical email address. Can have security implications when a source doesn't validate email addresses. * `email_deny` - Use the user's email address, but deny enrollment when the email address already exists. * `username_link` - Link to a user with identical username. Can have security implications when a username is used with another source. * `username_deny` - Use the user's username, but deny enrollment when the username already exists. (optional)

    try:
        api_response = api_instance.sources_plex_list(allow_friends=allow_friends, authentication_flow=authentication_flow, client_id=client_id, enabled=enabled, enrollment_flow=enrollment_flow, name=name, ordering=ordering, page=page, page_size=page_size, policy_engine_mode=policy_engine_mode, search=search, slug=slug, user_matching_mode=user_matching_mode)
        print("The response of SourcesApi->sources_plex_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_plex_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **allow_friends** | **bool**|  | [optional] 
 **authentication_flow** | **str**|  | [optional] 
 **client_id** | **str**|  | [optional] 
 **enabled** | **bool**|  | [optional] 
 **enrollment_flow** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **policy_engine_mode** | **str**| * &#x60;all&#x60; - all, all policies must pass * &#x60;any&#x60; - any, any policy must pass | [optional] 
 **search** | **str**| A search term. | [optional] 
 **slug** | **str**|  | [optional] 
 **user_matching_mode** | **str**| How the source determines if an existing user should be authenticated or a new user enrolled.  * &#x60;identifier&#x60; - Use the source-specific identifier * &#x60;email_link&#x60; - Link to a user with identical email address. Can have security implications when a source doesn&#39;t validate email addresses. * &#x60;email_deny&#x60; - Use the user&#39;s email address, but deny enrollment when the email address already exists. * &#x60;username_link&#x60; - Link to a user with identical username. Can have security implications when a username is used with another source. * &#x60;username_deny&#x60; - Use the user&#39;s username, but deny enrollment when the username already exists. | [optional] 

### Return type

[**PaginatedPlexSourceList**](PaginatedPlexSourceList.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_plex_partial_update**
> PlexSource sources_plex_partial_update(slug, patched_plex_source_request=patched_plex_source_request)



Plex source Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.patched_plex_source_request import PatchedPlexSourceRequest
from authentik.models.plex_source import PlexSource
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    slug = 'slug_example' # str | 
    patched_plex_source_request = authentik.PatchedPlexSourceRequest() # PatchedPlexSourceRequest |  (optional)

    try:
        api_response = api_instance.sources_plex_partial_update(slug, patched_plex_source_request=patched_plex_source_request)
        print("The response of SourcesApi->sources_plex_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_plex_partial_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **patched_plex_source_request** | [**PatchedPlexSourceRequest**](PatchedPlexSourceRequest.md)|  | [optional] 

### Return type

[**PlexSource**](PlexSource.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_plex_redeem_token_authenticated_create**
> sources_plex_redeem_token_authenticated_create(plex_token_redeem_request, slug=slug)



Redeem a plex token for an authenticated user, creating a connection

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.plex_token_redeem_request import PlexTokenRedeemRequest
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    plex_token_redeem_request = authentik.PlexTokenRedeemRequest() # PlexTokenRedeemRequest | 
    slug = 'slug_example' # str |  (optional)

    try:
        api_instance.sources_plex_redeem_token_authenticated_create(plex_token_redeem_request, slug=slug)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_plex_redeem_token_authenticated_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plex_token_redeem_request** | [**PlexTokenRedeemRequest**](PlexTokenRedeemRequest.md)|  | 
 **slug** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** | Token not found |  -  |
**403** | Access denied |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_plex_redeem_token_create**
> RedirectChallenge sources_plex_redeem_token_create(plex_token_redeem_request, slug=slug)



Redeem a plex token, check it's access to resources against what's allowed for the source, and redirect to an authentication/enrollment flow.

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.plex_token_redeem_request import PlexTokenRedeemRequest
from authentik.models.redirect_challenge import RedirectChallenge
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    plex_token_redeem_request = authentik.PlexTokenRedeemRequest() # PlexTokenRedeemRequest | 
    slug = 'slug_example' # str |  (optional)

    try:
        api_response = api_instance.sources_plex_redeem_token_create(plex_token_redeem_request, slug=slug)
        print("The response of SourcesApi->sources_plex_redeem_token_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_plex_redeem_token_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plex_token_redeem_request** | [**PlexTokenRedeemRequest**](PlexTokenRedeemRequest.md)|  | 
 **slug** | **str**|  | [optional] 

### Return type

[**RedirectChallenge**](RedirectChallenge.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Token not found |  -  |
**403** | Access denied |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_plex_retrieve**
> PlexSource sources_plex_retrieve(slug)



Plex source Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.plex_source import PlexSource
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    slug = 'slug_example' # str | 

    try:
        api_response = api_instance.sources_plex_retrieve(slug)
        print("The response of SourcesApi->sources_plex_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_plex_retrieve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

### Return type

[**PlexSource**](PlexSource.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_plex_update**
> PlexSource sources_plex_update(slug, plex_source_request)



Plex source Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.plex_source import PlexSource
from authentik.models.plex_source_request import PlexSourceRequest
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    slug = 'slug_example' # str | 
    plex_source_request = authentik.PlexSourceRequest() # PlexSourceRequest | 

    try:
        api_response = api_instance.sources_plex_update(slug, plex_source_request)
        print("The response of SourcesApi->sources_plex_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_plex_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **plex_source_request** | [**PlexSourceRequest**](PlexSourceRequest.md)|  | 

### Return type

[**PlexSource**](PlexSource.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_plex_used_by_list**
> List[UsedBy] sources_plex_used_by_list(slug)



Get a list of all objects that use this object

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.used_by import UsedBy
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    slug = 'slug_example' # str | 

    try:
        api_response = api_instance.sources_plex_used_by_list(slug)
        print("The response of SourcesApi->sources_plex_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_plex_used_by_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

### Return type

[**List[UsedBy]**](UsedBy.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_saml_create**
> SAMLSource sources_saml_create(saml_source_request)



SAMLSource Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.saml_source import SAMLSource
from authentik.models.saml_source_request import SAMLSourceRequest
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    saml_source_request = authentik.SAMLSourceRequest() # SAMLSourceRequest | 

    try:
        api_response = api_instance.sources_saml_create(saml_source_request)
        print("The response of SourcesApi->sources_saml_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_saml_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **saml_source_request** | [**SAMLSourceRequest**](SAMLSourceRequest.md)|  | 

### Return type

[**SAMLSource**](SAMLSource.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_saml_destroy**
> sources_saml_destroy(slug)



SAMLSource Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    slug = 'slug_example' # str | 

    try:
        api_instance.sources_saml_destroy(slug)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_saml_destroy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_saml_list**
> PaginatedSAMLSourceList sources_saml_list(allow_idp_initiated=allow_idp_initiated, authentication_flow=authentication_flow, binding_type=binding_type, digest_algorithm=digest_algorithm, enabled=enabled, enrollment_flow=enrollment_flow, issuer=issuer, managed=managed, name=name, name_id_policy=name_id_policy, ordering=ordering, page=page, page_size=page_size, policy_engine_mode=policy_engine_mode, pre_authentication_flow=pre_authentication_flow, search=search, signature_algorithm=signature_algorithm, signing_kp=signing_kp, slo_url=slo_url, slug=slug, sso_url=sso_url, temporary_user_delete_after=temporary_user_delete_after, user_matching_mode=user_matching_mode, verification_kp=verification_kp)



SAMLSource Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.paginated_saml_source_list import PaginatedSAMLSourceList
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    allow_idp_initiated = True # bool |  (optional)
    authentication_flow = 'authentication_flow_example' # str |  (optional)
    binding_type = 'binding_type_example' # str | * `REDIRECT` - Redirect Binding * `POST` - POST Binding * `POST_AUTO` - POST Binding with auto-confirmation (optional)
    digest_algorithm = 'digest_algorithm_example' # str | * `http://www.w3.org/2000/09/xmldsig#sha1` - SHA1 * `http://www.w3.org/2001/04/xmlenc#sha256` - SHA256 * `http://www.w3.org/2001/04/xmldsig-more#sha384` - SHA384 * `http://www.w3.org/2001/04/xmlenc#sha512` - SHA512 (optional)
    enabled = True # bool |  (optional)
    enrollment_flow = 'enrollment_flow_example' # str |  (optional)
    issuer = 'issuer_example' # str |  (optional)
    managed = 'managed_example' # str |  (optional)
    name = 'name_example' # str |  (optional)
    name_id_policy = 'name_id_policy_example' # str | NameID Policy sent to the IdP. Can be unset, in which case no Policy is sent.  * `urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress` - Email * `urn:oasis:names:tc:SAML:2.0:nameid-format:persistent` - Persistent * `urn:oasis:names:tc:SAML:2.0:nameid-format:X509SubjectName` - X509 * `urn:oasis:names:tc:SAML:2.0:nameid-format:WindowsDomainQualifiedName` - Windows * `urn:oasis:names:tc:SAML:2.0:nameid-format:transient` - Transient (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    policy_engine_mode = 'policy_engine_mode_example' # str | * `all` - all, all policies must pass * `any` - any, any policy must pass (optional)
    pre_authentication_flow = 'pre_authentication_flow_example' # str |  (optional)
    search = 'search_example' # str | A search term. (optional)
    signature_algorithm = 'signature_algorithm_example' # str | * `http://www.w3.org/2000/09/xmldsig#rsa-sha1` - RSA-SHA1 * `http://www.w3.org/2001/04/xmldsig-more#rsa-sha256` - RSA-SHA256 * `http://www.w3.org/2001/04/xmldsig-more#rsa-sha384` - RSA-SHA384 * `http://www.w3.org/2001/04/xmldsig-more#rsa-sha512` - RSA-SHA512 * `http://www.w3.org/2000/09/xmldsig#dsa-sha1` - DSA-SHA1 (optional)
    signing_kp = 'signing_kp_example' # str |  (optional)
    slo_url = 'slo_url_example' # str |  (optional)
    slug = 'slug_example' # str |  (optional)
    sso_url = 'sso_url_example' # str |  (optional)
    temporary_user_delete_after = 'temporary_user_delete_after_example' # str |  (optional)
    user_matching_mode = 'user_matching_mode_example' # str | How the source determines if an existing user should be authenticated or a new user enrolled.  * `identifier` - Use the source-specific identifier * `email_link` - Link to a user with identical email address. Can have security implications when a source doesn't validate email addresses. * `email_deny` - Use the user's email address, but deny enrollment when the email address already exists. * `username_link` - Link to a user with identical username. Can have security implications when a username is used with another source. * `username_deny` - Use the user's username, but deny enrollment when the username already exists. (optional)
    verification_kp = 'verification_kp_example' # str |  (optional)

    try:
        api_response = api_instance.sources_saml_list(allow_idp_initiated=allow_idp_initiated, authentication_flow=authentication_flow, binding_type=binding_type, digest_algorithm=digest_algorithm, enabled=enabled, enrollment_flow=enrollment_flow, issuer=issuer, managed=managed, name=name, name_id_policy=name_id_policy, ordering=ordering, page=page, page_size=page_size, policy_engine_mode=policy_engine_mode, pre_authentication_flow=pre_authentication_flow, search=search, signature_algorithm=signature_algorithm, signing_kp=signing_kp, slo_url=slo_url, slug=slug, sso_url=sso_url, temporary_user_delete_after=temporary_user_delete_after, user_matching_mode=user_matching_mode, verification_kp=verification_kp)
        print("The response of SourcesApi->sources_saml_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_saml_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **allow_idp_initiated** | **bool**|  | [optional] 
 **authentication_flow** | **str**|  | [optional] 
 **binding_type** | **str**| * &#x60;REDIRECT&#x60; - Redirect Binding * &#x60;POST&#x60; - POST Binding * &#x60;POST_AUTO&#x60; - POST Binding with auto-confirmation | [optional] 
 **digest_algorithm** | **str**| * &#x60;http://www.w3.org/2000/09/xmldsig#sha1&#x60; - SHA1 * &#x60;http://www.w3.org/2001/04/xmlenc#sha256&#x60; - SHA256 * &#x60;http://www.w3.org/2001/04/xmldsig-more#sha384&#x60; - SHA384 * &#x60;http://www.w3.org/2001/04/xmlenc#sha512&#x60; - SHA512 | [optional] 
 **enabled** | **bool**|  | [optional] 
 **enrollment_flow** | **str**|  | [optional] 
 **issuer** | **str**|  | [optional] 
 **managed** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **name_id_policy** | **str**| NameID Policy sent to the IdP. Can be unset, in which case no Policy is sent.  * &#x60;urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress&#x60; - Email * &#x60;urn:oasis:names:tc:SAML:2.0:nameid-format:persistent&#x60; - Persistent * &#x60;urn:oasis:names:tc:SAML:2.0:nameid-format:X509SubjectName&#x60; - X509 * &#x60;urn:oasis:names:tc:SAML:2.0:nameid-format:WindowsDomainQualifiedName&#x60; - Windows * &#x60;urn:oasis:names:tc:SAML:2.0:nameid-format:transient&#x60; - Transient | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **policy_engine_mode** | **str**| * &#x60;all&#x60; - all, all policies must pass * &#x60;any&#x60; - any, any policy must pass | [optional] 
 **pre_authentication_flow** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **signature_algorithm** | **str**| * &#x60;http://www.w3.org/2000/09/xmldsig#rsa-sha1&#x60; - RSA-SHA1 * &#x60;http://www.w3.org/2001/04/xmldsig-more#rsa-sha256&#x60; - RSA-SHA256 * &#x60;http://www.w3.org/2001/04/xmldsig-more#rsa-sha384&#x60; - RSA-SHA384 * &#x60;http://www.w3.org/2001/04/xmldsig-more#rsa-sha512&#x60; - RSA-SHA512 * &#x60;http://www.w3.org/2000/09/xmldsig#dsa-sha1&#x60; - DSA-SHA1 | [optional] 
 **signing_kp** | **str**|  | [optional] 
 **slo_url** | **str**|  | [optional] 
 **slug** | **str**|  | [optional] 
 **sso_url** | **str**|  | [optional] 
 **temporary_user_delete_after** | **str**|  | [optional] 
 **user_matching_mode** | **str**| How the source determines if an existing user should be authenticated or a new user enrolled.  * &#x60;identifier&#x60; - Use the source-specific identifier * &#x60;email_link&#x60; - Link to a user with identical email address. Can have security implications when a source doesn&#39;t validate email addresses. * &#x60;email_deny&#x60; - Use the user&#39;s email address, but deny enrollment when the email address already exists. * &#x60;username_link&#x60; - Link to a user with identical username. Can have security implications when a username is used with another source. * &#x60;username_deny&#x60; - Use the user&#39;s username, but deny enrollment when the username already exists. | [optional] 
 **verification_kp** | **str**|  | [optional] 

### Return type

[**PaginatedSAMLSourceList**](PaginatedSAMLSourceList.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_saml_metadata_retrieve**
> SAMLMetadata sources_saml_metadata_retrieve(slug)



Return metadata as XML string

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.saml_metadata import SAMLMetadata
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    slug = 'slug_example' # str | 

    try:
        api_response = api_instance.sources_saml_metadata_retrieve(slug)
        print("The response of SourcesApi->sources_saml_metadata_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_saml_metadata_retrieve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

### Return type

[**SAMLMetadata**](SAMLMetadata.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_saml_partial_update**
> SAMLSource sources_saml_partial_update(slug, patched_saml_source_request=patched_saml_source_request)



SAMLSource Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.patched_saml_source_request import PatchedSAMLSourceRequest
from authentik.models.saml_source import SAMLSource
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    slug = 'slug_example' # str | 
    patched_saml_source_request = authentik.PatchedSAMLSourceRequest() # PatchedSAMLSourceRequest |  (optional)

    try:
        api_response = api_instance.sources_saml_partial_update(slug, patched_saml_source_request=patched_saml_source_request)
        print("The response of SourcesApi->sources_saml_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_saml_partial_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **patched_saml_source_request** | [**PatchedSAMLSourceRequest**](PatchedSAMLSourceRequest.md)|  | [optional] 

### Return type

[**SAMLSource**](SAMLSource.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_saml_retrieve**
> SAMLSource sources_saml_retrieve(slug)



SAMLSource Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.saml_source import SAMLSource
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    slug = 'slug_example' # str | 

    try:
        api_response = api_instance.sources_saml_retrieve(slug)
        print("The response of SourcesApi->sources_saml_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_saml_retrieve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

### Return type

[**SAMLSource**](SAMLSource.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_saml_update**
> SAMLSource sources_saml_update(slug, saml_source_request)



SAMLSource Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.saml_source import SAMLSource
from authentik.models.saml_source_request import SAMLSourceRequest
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    slug = 'slug_example' # str | 
    saml_source_request = authentik.SAMLSourceRequest() # SAMLSourceRequest | 

    try:
        api_response = api_instance.sources_saml_update(slug, saml_source_request)
        print("The response of SourcesApi->sources_saml_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_saml_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 
 **saml_source_request** | [**SAMLSourceRequest**](SAMLSourceRequest.md)|  | 

### Return type

[**SAMLSource**](SAMLSource.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_saml_used_by_list**
> List[UsedBy] sources_saml_used_by_list(slug)



Get a list of all objects that use this object

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.used_by import UsedBy
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    slug = 'slug_example' # str | 

    try:
        api_response = api_instance.sources_saml_used_by_list(slug)
        print("The response of SourcesApi->sources_saml_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_saml_used_by_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**|  | 

### Return type

[**List[UsedBy]**](UsedBy.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_user_connections_all_destroy**
> sources_user_connections_all_destroy(id)



User-source connection Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    id = 56 # int | A unique integer value identifying this user source connection.

    try:
        api_instance.sources_user_connections_all_destroy(id)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_user_connections_all_destroy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user source connection. | 

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_user_connections_all_list**
> PaginatedUserSourceConnectionList sources_user_connections_all_list(ordering=ordering, page=page, page_size=page_size, search=search, user=user)



User-source connection Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.paginated_user_source_connection_list import PaginatedUserSourceConnectionList
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)
    user = 56 # int |  (optional)

    try:
        api_response = api_instance.sources_user_connections_all_list(ordering=ordering, page=page, page_size=page_size, search=search, user=user)
        print("The response of SourcesApi->sources_user_connections_all_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_user_connections_all_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **user** | **int**|  | [optional] 

### Return type

[**PaginatedUserSourceConnectionList**](PaginatedUserSourceConnectionList.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_user_connections_all_partial_update**
> UserSourceConnection sources_user_connections_all_partial_update(id)



User-source connection Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.user_source_connection import UserSourceConnection
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    id = 56 # int | A unique integer value identifying this user source connection.

    try:
        api_response = api_instance.sources_user_connections_all_partial_update(id)
        print("The response of SourcesApi->sources_user_connections_all_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_user_connections_all_partial_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user source connection. | 

### Return type

[**UserSourceConnection**](UserSourceConnection.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_user_connections_all_retrieve**
> UserSourceConnection sources_user_connections_all_retrieve(id)



User-source connection Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.user_source_connection import UserSourceConnection
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    id = 56 # int | A unique integer value identifying this user source connection.

    try:
        api_response = api_instance.sources_user_connections_all_retrieve(id)
        print("The response of SourcesApi->sources_user_connections_all_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_user_connections_all_retrieve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user source connection. | 

### Return type

[**UserSourceConnection**](UserSourceConnection.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_user_connections_all_update**
> UserSourceConnection sources_user_connections_all_update(id)



User-source connection Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.user_source_connection import UserSourceConnection
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    id = 56 # int | A unique integer value identifying this user source connection.

    try:
        api_response = api_instance.sources_user_connections_all_update(id)
        print("The response of SourcesApi->sources_user_connections_all_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_user_connections_all_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user source connection. | 

### Return type

[**UserSourceConnection**](UserSourceConnection.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_user_connections_all_used_by_list**
> List[UsedBy] sources_user_connections_all_used_by_list(id)



Get a list of all objects that use this object

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.used_by import UsedBy
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    id = 56 # int | A unique integer value identifying this user source connection.

    try:
        api_response = api_instance.sources_user_connections_all_used_by_list(id)
        print("The response of SourcesApi->sources_user_connections_all_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_user_connections_all_used_by_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this user source connection. | 

### Return type

[**List[UsedBy]**](UsedBy.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_user_connections_oauth_create**
> UserOAuthSourceConnection sources_user_connections_oauth_create(user_o_auth_source_connection_request)



Source Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.user_o_auth_source_connection import UserOAuthSourceConnection
from authentik.models.user_o_auth_source_connection_request import UserOAuthSourceConnectionRequest
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    user_o_auth_source_connection_request = authentik.UserOAuthSourceConnectionRequest() # UserOAuthSourceConnectionRequest | 

    try:
        api_response = api_instance.sources_user_connections_oauth_create(user_o_auth_source_connection_request)
        print("The response of SourcesApi->sources_user_connections_oauth_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_user_connections_oauth_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_o_auth_source_connection_request** | [**UserOAuthSourceConnectionRequest**](UserOAuthSourceConnectionRequest.md)|  | 

### Return type

[**UserOAuthSourceConnection**](UserOAuthSourceConnection.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_user_connections_oauth_destroy**
> sources_user_connections_oauth_destroy(id)



Source Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    id = 56 # int | A unique integer value identifying this User OAuth Source Connection.

    try:
        api_instance.sources_user_connections_oauth_destroy(id)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_user_connections_oauth_destroy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User OAuth Source Connection. | 

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_user_connections_oauth_list**
> PaginatedUserOAuthSourceConnectionList sources_user_connections_oauth_list(ordering=ordering, page=page, page_size=page_size, search=search, source__slug=source__slug)



Source Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.paginated_user_o_auth_source_connection_list import PaginatedUserOAuthSourceConnectionList
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)
    source__slug = 'source__slug_example' # str |  (optional)

    try:
        api_response = api_instance.sources_user_connections_oauth_list(ordering=ordering, page=page, page_size=page_size, search=search, source__slug=source__slug)
        print("The response of SourcesApi->sources_user_connections_oauth_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_user_connections_oauth_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **source__slug** | **str**|  | [optional] 

### Return type

[**PaginatedUserOAuthSourceConnectionList**](PaginatedUserOAuthSourceConnectionList.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_user_connections_oauth_partial_update**
> UserOAuthSourceConnection sources_user_connections_oauth_partial_update(id, patched_user_o_auth_source_connection_request=patched_user_o_auth_source_connection_request)



Source Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.patched_user_o_auth_source_connection_request import PatchedUserOAuthSourceConnectionRequest
from authentik.models.user_o_auth_source_connection import UserOAuthSourceConnection
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    id = 56 # int | A unique integer value identifying this User OAuth Source Connection.
    patched_user_o_auth_source_connection_request = authentik.PatchedUserOAuthSourceConnectionRequest() # PatchedUserOAuthSourceConnectionRequest |  (optional)

    try:
        api_response = api_instance.sources_user_connections_oauth_partial_update(id, patched_user_o_auth_source_connection_request=patched_user_o_auth_source_connection_request)
        print("The response of SourcesApi->sources_user_connections_oauth_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_user_connections_oauth_partial_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User OAuth Source Connection. | 
 **patched_user_o_auth_source_connection_request** | [**PatchedUserOAuthSourceConnectionRequest**](PatchedUserOAuthSourceConnectionRequest.md)|  | [optional] 

### Return type

[**UserOAuthSourceConnection**](UserOAuthSourceConnection.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_user_connections_oauth_retrieve**
> UserOAuthSourceConnection sources_user_connections_oauth_retrieve(id)



Source Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.user_o_auth_source_connection import UserOAuthSourceConnection
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    id = 56 # int | A unique integer value identifying this User OAuth Source Connection.

    try:
        api_response = api_instance.sources_user_connections_oauth_retrieve(id)
        print("The response of SourcesApi->sources_user_connections_oauth_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_user_connections_oauth_retrieve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User OAuth Source Connection. | 

### Return type

[**UserOAuthSourceConnection**](UserOAuthSourceConnection.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_user_connections_oauth_update**
> UserOAuthSourceConnection sources_user_connections_oauth_update(id, user_o_auth_source_connection_request)



Source Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.user_o_auth_source_connection import UserOAuthSourceConnection
from authentik.models.user_o_auth_source_connection_request import UserOAuthSourceConnectionRequest
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    id = 56 # int | A unique integer value identifying this User OAuth Source Connection.
    user_o_auth_source_connection_request = authentik.UserOAuthSourceConnectionRequest() # UserOAuthSourceConnectionRequest | 

    try:
        api_response = api_instance.sources_user_connections_oauth_update(id, user_o_auth_source_connection_request)
        print("The response of SourcesApi->sources_user_connections_oauth_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_user_connections_oauth_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User OAuth Source Connection. | 
 **user_o_auth_source_connection_request** | [**UserOAuthSourceConnectionRequest**](UserOAuthSourceConnectionRequest.md)|  | 

### Return type

[**UserOAuthSourceConnection**](UserOAuthSourceConnection.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_user_connections_oauth_used_by_list**
> List[UsedBy] sources_user_connections_oauth_used_by_list(id)



Get a list of all objects that use this object

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.used_by import UsedBy
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    id = 56 # int | A unique integer value identifying this User OAuth Source Connection.

    try:
        api_response = api_instance.sources_user_connections_oauth_used_by_list(id)
        print("The response of SourcesApi->sources_user_connections_oauth_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_user_connections_oauth_used_by_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User OAuth Source Connection. | 

### Return type

[**List[UsedBy]**](UsedBy.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_user_connections_plex_create**
> PlexSourceConnection sources_user_connections_plex_create(plex_source_connection_request)



Plex Source connection Serializer

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.plex_source_connection import PlexSourceConnection
from authentik.models.plex_source_connection_request import PlexSourceConnectionRequest
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    plex_source_connection_request = authentik.PlexSourceConnectionRequest() # PlexSourceConnectionRequest | 

    try:
        api_response = api_instance.sources_user_connections_plex_create(plex_source_connection_request)
        print("The response of SourcesApi->sources_user_connections_plex_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_user_connections_plex_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plex_source_connection_request** | [**PlexSourceConnectionRequest**](PlexSourceConnectionRequest.md)|  | 

### Return type

[**PlexSourceConnection**](PlexSourceConnection.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_user_connections_plex_destroy**
> sources_user_connections_plex_destroy(id)



Plex Source connection Serializer

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    id = 56 # int | A unique integer value identifying this User Plex Source Connection.

    try:
        api_instance.sources_user_connections_plex_destroy(id)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_user_connections_plex_destroy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User Plex Source Connection. | 

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_user_connections_plex_list**
> PaginatedPlexSourceConnectionList sources_user_connections_plex_list(ordering=ordering, page=page, page_size=page_size, search=search, source__slug=source__slug)



Plex Source connection Serializer

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.paginated_plex_source_connection_list import PaginatedPlexSourceConnectionList
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)
    source__slug = 'source__slug_example' # str |  (optional)

    try:
        api_response = api_instance.sources_user_connections_plex_list(ordering=ordering, page=page, page_size=page_size, search=search, source__slug=source__slug)
        print("The response of SourcesApi->sources_user_connections_plex_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_user_connections_plex_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **source__slug** | **str**|  | [optional] 

### Return type

[**PaginatedPlexSourceConnectionList**](PaginatedPlexSourceConnectionList.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_user_connections_plex_partial_update**
> PlexSourceConnection sources_user_connections_plex_partial_update(id, patched_plex_source_connection_request=patched_plex_source_connection_request)



Plex Source connection Serializer

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.patched_plex_source_connection_request import PatchedPlexSourceConnectionRequest
from authentik.models.plex_source_connection import PlexSourceConnection
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    id = 56 # int | A unique integer value identifying this User Plex Source Connection.
    patched_plex_source_connection_request = authentik.PatchedPlexSourceConnectionRequest() # PatchedPlexSourceConnectionRequest |  (optional)

    try:
        api_response = api_instance.sources_user_connections_plex_partial_update(id, patched_plex_source_connection_request=patched_plex_source_connection_request)
        print("The response of SourcesApi->sources_user_connections_plex_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_user_connections_plex_partial_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User Plex Source Connection. | 
 **patched_plex_source_connection_request** | [**PatchedPlexSourceConnectionRequest**](PatchedPlexSourceConnectionRequest.md)|  | [optional] 

### Return type

[**PlexSourceConnection**](PlexSourceConnection.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_user_connections_plex_retrieve**
> PlexSourceConnection sources_user_connections_plex_retrieve(id)



Plex Source connection Serializer

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.plex_source_connection import PlexSourceConnection
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    id = 56 # int | A unique integer value identifying this User Plex Source Connection.

    try:
        api_response = api_instance.sources_user_connections_plex_retrieve(id)
        print("The response of SourcesApi->sources_user_connections_plex_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_user_connections_plex_retrieve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User Plex Source Connection. | 

### Return type

[**PlexSourceConnection**](PlexSourceConnection.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_user_connections_plex_update**
> PlexSourceConnection sources_user_connections_plex_update(id, plex_source_connection_request)



Plex Source connection Serializer

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.plex_source_connection import PlexSourceConnection
from authentik.models.plex_source_connection_request import PlexSourceConnectionRequest
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    id = 56 # int | A unique integer value identifying this User Plex Source Connection.
    plex_source_connection_request = authentik.PlexSourceConnectionRequest() # PlexSourceConnectionRequest | 

    try:
        api_response = api_instance.sources_user_connections_plex_update(id, plex_source_connection_request)
        print("The response of SourcesApi->sources_user_connections_plex_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_user_connections_plex_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User Plex Source Connection. | 
 **plex_source_connection_request** | [**PlexSourceConnectionRequest**](PlexSourceConnectionRequest.md)|  | 

### Return type

[**PlexSourceConnection**](PlexSourceConnection.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_user_connections_plex_used_by_list**
> List[UsedBy] sources_user_connections_plex_used_by_list(id)



Get a list of all objects that use this object

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.used_by import UsedBy
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    id = 56 # int | A unique integer value identifying this User Plex Source Connection.

    try:
        api_response = api_instance.sources_user_connections_plex_used_by_list(id)
        print("The response of SourcesApi->sources_user_connections_plex_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_user_connections_plex_used_by_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User Plex Source Connection. | 

### Return type

[**List[UsedBy]**](UsedBy.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_user_connections_saml_create**
> UserSAMLSourceConnection sources_user_connections_saml_create(user_saml_source_connection_request)



Source Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.user_saml_source_connection import UserSAMLSourceConnection
from authentik.models.user_saml_source_connection_request import UserSAMLSourceConnectionRequest
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    user_saml_source_connection_request = authentik.UserSAMLSourceConnectionRequest() # UserSAMLSourceConnectionRequest | 

    try:
        api_response = api_instance.sources_user_connections_saml_create(user_saml_source_connection_request)
        print("The response of SourcesApi->sources_user_connections_saml_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_user_connections_saml_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_saml_source_connection_request** | [**UserSAMLSourceConnectionRequest**](UserSAMLSourceConnectionRequest.md)|  | 

### Return type

[**UserSAMLSourceConnection**](UserSAMLSourceConnection.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_user_connections_saml_destroy**
> sources_user_connections_saml_destroy(id)



Source Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    id = 56 # int | A unique integer value identifying this User SAML Source Connection.

    try:
        api_instance.sources_user_connections_saml_destroy(id)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_user_connections_saml_destroy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User SAML Source Connection. | 

### Return type

void (empty response body)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No response body |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_user_connections_saml_list**
> PaginatedUserSAMLSourceConnectionList sources_user_connections_saml_list(ordering=ordering, page=page, page_size=page_size, search=search, source__slug=source__slug)



Source Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.paginated_user_saml_source_connection_list import PaginatedUserSAMLSourceConnectionList
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    search = 'search_example' # str | A search term. (optional)
    source__slug = 'source__slug_example' # str |  (optional)

    try:
        api_response = api_instance.sources_user_connections_saml_list(ordering=ordering, page=page, page_size=page_size, search=search, source__slug=source__slug)
        print("The response of SourcesApi->sources_user_connections_saml_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_user_connections_saml_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **search** | **str**| A search term. | [optional] 
 **source__slug** | **str**|  | [optional] 

### Return type

[**PaginatedUserSAMLSourceConnectionList**](PaginatedUserSAMLSourceConnectionList.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_user_connections_saml_partial_update**
> UserSAMLSourceConnection sources_user_connections_saml_partial_update(id, patched_user_saml_source_connection_request=patched_user_saml_source_connection_request)



Source Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.patched_user_saml_source_connection_request import PatchedUserSAMLSourceConnectionRequest
from authentik.models.user_saml_source_connection import UserSAMLSourceConnection
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    id = 56 # int | A unique integer value identifying this User SAML Source Connection.
    patched_user_saml_source_connection_request = authentik.PatchedUserSAMLSourceConnectionRequest() # PatchedUserSAMLSourceConnectionRequest |  (optional)

    try:
        api_response = api_instance.sources_user_connections_saml_partial_update(id, patched_user_saml_source_connection_request=patched_user_saml_source_connection_request)
        print("The response of SourcesApi->sources_user_connections_saml_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_user_connections_saml_partial_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User SAML Source Connection. | 
 **patched_user_saml_source_connection_request** | [**PatchedUserSAMLSourceConnectionRequest**](PatchedUserSAMLSourceConnectionRequest.md)|  | [optional] 

### Return type

[**UserSAMLSourceConnection**](UserSAMLSourceConnection.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_user_connections_saml_retrieve**
> UserSAMLSourceConnection sources_user_connections_saml_retrieve(id)



Source Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.user_saml_source_connection import UserSAMLSourceConnection
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    id = 56 # int | A unique integer value identifying this User SAML Source Connection.

    try:
        api_response = api_instance.sources_user_connections_saml_retrieve(id)
        print("The response of SourcesApi->sources_user_connections_saml_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_user_connections_saml_retrieve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User SAML Source Connection. | 

### Return type

[**UserSAMLSourceConnection**](UserSAMLSourceConnection.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_user_connections_saml_update**
> UserSAMLSourceConnection sources_user_connections_saml_update(id, user_saml_source_connection_request)



Source Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.user_saml_source_connection import UserSAMLSourceConnection
from authentik.models.user_saml_source_connection_request import UserSAMLSourceConnectionRequest
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    id = 56 # int | A unique integer value identifying this User SAML Source Connection.
    user_saml_source_connection_request = authentik.UserSAMLSourceConnectionRequest() # UserSAMLSourceConnectionRequest | 

    try:
        api_response = api_instance.sources_user_connections_saml_update(id, user_saml_source_connection_request)
        print("The response of SourcesApi->sources_user_connections_saml_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_user_connections_saml_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User SAML Source Connection. | 
 **user_saml_source_connection_request** | [**UserSAMLSourceConnectionRequest**](UserSAMLSourceConnectionRequest.md)|  | 

### Return type

[**UserSAMLSourceConnection**](UserSAMLSourceConnection.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sources_user_connections_saml_used_by_list**
> List[UsedBy] sources_user_connections_saml_used_by_list(id)



Get a list of all objects that use this object

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.used_by import UsedBy
from authentik.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/api/v3
# See configuration.py for a list of all supported configuration parameters.
configuration = authentik.Configuration(
    host = "http://localhost/api/v3"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: authentik
configuration.api_key['authentik'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authentik'] = 'Bearer'

# Enter a context with an instance of the API client
with authentik.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = authentik.SourcesApi(api_client)
    id = 56 # int | A unique integer value identifying this User SAML Source Connection.

    try:
        api_response = api_instance.sources_user_connections_saml_used_by_list(id)
        print("The response of SourcesApi->sources_user_connections_saml_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SourcesApi->sources_user_connections_saml_used_by_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this User SAML Source Connection. | 

### Return type

[**List[UsedBy]**](UsedBy.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

