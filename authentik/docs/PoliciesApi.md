# authentik.PoliciesApi

All URIs are relative to *http://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**policies_all_cache_clear_create**](PoliciesApi.md#policies_all_cache_clear_create) | **POST** /policies/all/cache_clear/ | 
[**policies_all_cache_info_retrieve**](PoliciesApi.md#policies_all_cache_info_retrieve) | **GET** /policies/all/cache_info/ | 
[**policies_all_destroy**](PoliciesApi.md#policies_all_destroy) | **DELETE** /policies/all/{policy_uuid}/ | 
[**policies_all_list**](PoliciesApi.md#policies_all_list) | **GET** /policies/all/ | 
[**policies_all_retrieve**](PoliciesApi.md#policies_all_retrieve) | **GET** /policies/all/{policy_uuid}/ | 
[**policies_all_test_create**](PoliciesApi.md#policies_all_test_create) | **POST** /policies/all/{policy_uuid}/test/ | 
[**policies_all_types_list**](PoliciesApi.md#policies_all_types_list) | **GET** /policies/all/types/ | 
[**policies_all_used_by_list**](PoliciesApi.md#policies_all_used_by_list) | **GET** /policies/all/{policy_uuid}/used_by/ | 
[**policies_bindings_create**](PoliciesApi.md#policies_bindings_create) | **POST** /policies/bindings/ | 
[**policies_bindings_destroy**](PoliciesApi.md#policies_bindings_destroy) | **DELETE** /policies/bindings/{policy_binding_uuid}/ | 
[**policies_bindings_list**](PoliciesApi.md#policies_bindings_list) | **GET** /policies/bindings/ | 
[**policies_bindings_partial_update**](PoliciesApi.md#policies_bindings_partial_update) | **PATCH** /policies/bindings/{policy_binding_uuid}/ | 
[**policies_bindings_retrieve**](PoliciesApi.md#policies_bindings_retrieve) | **GET** /policies/bindings/{policy_binding_uuid}/ | 
[**policies_bindings_update**](PoliciesApi.md#policies_bindings_update) | **PUT** /policies/bindings/{policy_binding_uuid}/ | 
[**policies_bindings_used_by_list**](PoliciesApi.md#policies_bindings_used_by_list) | **GET** /policies/bindings/{policy_binding_uuid}/used_by/ | 
[**policies_dummy_create**](PoliciesApi.md#policies_dummy_create) | **POST** /policies/dummy/ | 
[**policies_dummy_destroy**](PoliciesApi.md#policies_dummy_destroy) | **DELETE** /policies/dummy/{policy_uuid}/ | 
[**policies_dummy_list**](PoliciesApi.md#policies_dummy_list) | **GET** /policies/dummy/ | 
[**policies_dummy_partial_update**](PoliciesApi.md#policies_dummy_partial_update) | **PATCH** /policies/dummy/{policy_uuid}/ | 
[**policies_dummy_retrieve**](PoliciesApi.md#policies_dummy_retrieve) | **GET** /policies/dummy/{policy_uuid}/ | 
[**policies_dummy_update**](PoliciesApi.md#policies_dummy_update) | **PUT** /policies/dummy/{policy_uuid}/ | 
[**policies_dummy_used_by_list**](PoliciesApi.md#policies_dummy_used_by_list) | **GET** /policies/dummy/{policy_uuid}/used_by/ | 
[**policies_event_matcher_create**](PoliciesApi.md#policies_event_matcher_create) | **POST** /policies/event_matcher/ | 
[**policies_event_matcher_destroy**](PoliciesApi.md#policies_event_matcher_destroy) | **DELETE** /policies/event_matcher/{policy_uuid}/ | 
[**policies_event_matcher_list**](PoliciesApi.md#policies_event_matcher_list) | **GET** /policies/event_matcher/ | 
[**policies_event_matcher_partial_update**](PoliciesApi.md#policies_event_matcher_partial_update) | **PATCH** /policies/event_matcher/{policy_uuid}/ | 
[**policies_event_matcher_retrieve**](PoliciesApi.md#policies_event_matcher_retrieve) | **GET** /policies/event_matcher/{policy_uuid}/ | 
[**policies_event_matcher_update**](PoliciesApi.md#policies_event_matcher_update) | **PUT** /policies/event_matcher/{policy_uuid}/ | 
[**policies_event_matcher_used_by_list**](PoliciesApi.md#policies_event_matcher_used_by_list) | **GET** /policies/event_matcher/{policy_uuid}/used_by/ | 
[**policies_expression_create**](PoliciesApi.md#policies_expression_create) | **POST** /policies/expression/ | 
[**policies_expression_destroy**](PoliciesApi.md#policies_expression_destroy) | **DELETE** /policies/expression/{policy_uuid}/ | 
[**policies_expression_list**](PoliciesApi.md#policies_expression_list) | **GET** /policies/expression/ | 
[**policies_expression_partial_update**](PoliciesApi.md#policies_expression_partial_update) | **PATCH** /policies/expression/{policy_uuid}/ | 
[**policies_expression_retrieve**](PoliciesApi.md#policies_expression_retrieve) | **GET** /policies/expression/{policy_uuid}/ | 
[**policies_expression_update**](PoliciesApi.md#policies_expression_update) | **PUT** /policies/expression/{policy_uuid}/ | 
[**policies_expression_used_by_list**](PoliciesApi.md#policies_expression_used_by_list) | **GET** /policies/expression/{policy_uuid}/used_by/ | 
[**policies_password_create**](PoliciesApi.md#policies_password_create) | **POST** /policies/password/ | 
[**policies_password_destroy**](PoliciesApi.md#policies_password_destroy) | **DELETE** /policies/password/{policy_uuid}/ | 
[**policies_password_expiry_create**](PoliciesApi.md#policies_password_expiry_create) | **POST** /policies/password_expiry/ | 
[**policies_password_expiry_destroy**](PoliciesApi.md#policies_password_expiry_destroy) | **DELETE** /policies/password_expiry/{policy_uuid}/ | 
[**policies_password_expiry_list**](PoliciesApi.md#policies_password_expiry_list) | **GET** /policies/password_expiry/ | 
[**policies_password_expiry_partial_update**](PoliciesApi.md#policies_password_expiry_partial_update) | **PATCH** /policies/password_expiry/{policy_uuid}/ | 
[**policies_password_expiry_retrieve**](PoliciesApi.md#policies_password_expiry_retrieve) | **GET** /policies/password_expiry/{policy_uuid}/ | 
[**policies_password_expiry_update**](PoliciesApi.md#policies_password_expiry_update) | **PUT** /policies/password_expiry/{policy_uuid}/ | 
[**policies_password_expiry_used_by_list**](PoliciesApi.md#policies_password_expiry_used_by_list) | **GET** /policies/password_expiry/{policy_uuid}/used_by/ | 
[**policies_password_list**](PoliciesApi.md#policies_password_list) | **GET** /policies/password/ | 
[**policies_password_partial_update**](PoliciesApi.md#policies_password_partial_update) | **PATCH** /policies/password/{policy_uuid}/ | 
[**policies_password_retrieve**](PoliciesApi.md#policies_password_retrieve) | **GET** /policies/password/{policy_uuid}/ | 
[**policies_password_update**](PoliciesApi.md#policies_password_update) | **PUT** /policies/password/{policy_uuid}/ | 
[**policies_password_used_by_list**](PoliciesApi.md#policies_password_used_by_list) | **GET** /policies/password/{policy_uuid}/used_by/ | 
[**policies_reputation_create**](PoliciesApi.md#policies_reputation_create) | **POST** /policies/reputation/ | 
[**policies_reputation_destroy**](PoliciesApi.md#policies_reputation_destroy) | **DELETE** /policies/reputation/{policy_uuid}/ | 
[**policies_reputation_list**](PoliciesApi.md#policies_reputation_list) | **GET** /policies/reputation/ | 
[**policies_reputation_partial_update**](PoliciesApi.md#policies_reputation_partial_update) | **PATCH** /policies/reputation/{policy_uuid}/ | 
[**policies_reputation_retrieve**](PoliciesApi.md#policies_reputation_retrieve) | **GET** /policies/reputation/{policy_uuid}/ | 
[**policies_reputation_scores_destroy**](PoliciesApi.md#policies_reputation_scores_destroy) | **DELETE** /policies/reputation/scores/{reputation_uuid}/ | 
[**policies_reputation_scores_list**](PoliciesApi.md#policies_reputation_scores_list) | **GET** /policies/reputation/scores/ | 
[**policies_reputation_scores_retrieve**](PoliciesApi.md#policies_reputation_scores_retrieve) | **GET** /policies/reputation/scores/{reputation_uuid}/ | 
[**policies_reputation_scores_used_by_list**](PoliciesApi.md#policies_reputation_scores_used_by_list) | **GET** /policies/reputation/scores/{reputation_uuid}/used_by/ | 
[**policies_reputation_update**](PoliciesApi.md#policies_reputation_update) | **PUT** /policies/reputation/{policy_uuid}/ | 
[**policies_reputation_used_by_list**](PoliciesApi.md#policies_reputation_used_by_list) | **GET** /policies/reputation/{policy_uuid}/used_by/ | 


# **policies_all_cache_clear_create**
> policies_all_cache_clear_create()



Clear policy cache

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
    api_instance = authentik.PoliciesApi(api_client)

    try:
        api_instance.policies_all_cache_clear_create()
    except Exception as e:
        print("Exception when calling PoliciesApi->policies_all_cache_clear_create: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

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
**204** | Successfully cleared cache |  -  |
**400** | Bad request |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **policies_all_cache_info_retrieve**
> Cache policies_all_cache_info_retrieve()



Info about cached policies

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.cache import Cache
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
    api_instance = authentik.PoliciesApi(api_client)

    try:
        api_response = api_instance.policies_all_cache_info_retrieve()
        print("The response of PoliciesApi->policies_all_cache_info_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->policies_all_cache_info_retrieve: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**Cache**](Cache.md)

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

# **policies_all_destroy**
> policies_all_destroy(policy_uuid)



Policy Viewset

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
    api_instance = authentik.PoliciesApi(api_client)
    policy_uuid = 'policy_uuid_example' # str | A UUID string identifying this Policy.

    try:
        api_instance.policies_all_destroy(policy_uuid)
    except Exception as e:
        print("Exception when calling PoliciesApi->policies_all_destroy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_uuid** | **str**| A UUID string identifying this Policy. | 

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

# **policies_all_list**
> PaginatedPolicyList policies_all_list(bindings__isnull=bindings__isnull, ordering=ordering, page=page, page_size=page_size, promptstage__isnull=promptstage__isnull, search=search)



Policy Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.paginated_policy_list import PaginatedPolicyList
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
    api_instance = authentik.PoliciesApi(api_client)
    bindings__isnull = True # bool |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    promptstage__isnull = True # bool |  (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.policies_all_list(bindings__isnull=bindings__isnull, ordering=ordering, page=page, page_size=page_size, promptstage__isnull=promptstage__isnull, search=search)
        print("The response of PoliciesApi->policies_all_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->policies_all_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bindings__isnull** | **bool**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **promptstage__isnull** | **bool**|  | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedPolicyList**](PaginatedPolicyList.md)

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

# **policies_all_retrieve**
> Policy policies_all_retrieve(policy_uuid)



Policy Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.policy import Policy
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
    api_instance = authentik.PoliciesApi(api_client)
    policy_uuid = 'policy_uuid_example' # str | A UUID string identifying this Policy.

    try:
        api_response = api_instance.policies_all_retrieve(policy_uuid)
        print("The response of PoliciesApi->policies_all_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->policies_all_retrieve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_uuid** | **str**| A UUID string identifying this Policy. | 

### Return type

[**Policy**](Policy.md)

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

# **policies_all_test_create**
> PolicyTestResult policies_all_test_create(policy_uuid, policy_test_request)



Test policy

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.policy_test_request import PolicyTestRequest
from authentik.models.policy_test_result import PolicyTestResult
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
    api_instance = authentik.PoliciesApi(api_client)
    policy_uuid = 'policy_uuid_example' # str | A UUID string identifying this Policy.
    policy_test_request = authentik.PolicyTestRequest() # PolicyTestRequest | 

    try:
        api_response = api_instance.policies_all_test_create(policy_uuid, policy_test_request)
        print("The response of PoliciesApi->policies_all_test_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->policies_all_test_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_uuid** | **str**| A UUID string identifying this Policy. | 
 **policy_test_request** | [**PolicyTestRequest**](PolicyTestRequest.md)|  | 

### Return type

[**PolicyTestResult**](PolicyTestResult.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | Invalid parameters |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **policies_all_types_list**
> List[TypeCreate] policies_all_types_list()



Get all creatable policy types

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
    api_instance = authentik.PoliciesApi(api_client)

    try:
        api_response = api_instance.policies_all_types_list()
        print("The response of PoliciesApi->policies_all_types_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->policies_all_types_list: %s\n" % e)
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

# **policies_all_used_by_list**
> List[UsedBy] policies_all_used_by_list(policy_uuid)



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
    api_instance = authentik.PoliciesApi(api_client)
    policy_uuid = 'policy_uuid_example' # str | A UUID string identifying this Policy.

    try:
        api_response = api_instance.policies_all_used_by_list(policy_uuid)
        print("The response of PoliciesApi->policies_all_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->policies_all_used_by_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_uuid** | **str**| A UUID string identifying this Policy. | 

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

# **policies_bindings_create**
> PolicyBinding policies_bindings_create(policy_binding_request)



PolicyBinding Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.policy_binding import PolicyBinding
from authentik.models.policy_binding_request import PolicyBindingRequest
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
    api_instance = authentik.PoliciesApi(api_client)
    policy_binding_request = authentik.PolicyBindingRequest() # PolicyBindingRequest | 

    try:
        api_response = api_instance.policies_bindings_create(policy_binding_request)
        print("The response of PoliciesApi->policies_bindings_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->policies_bindings_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_binding_request** | [**PolicyBindingRequest**](PolicyBindingRequest.md)|  | 

### Return type

[**PolicyBinding**](PolicyBinding.md)

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

# **policies_bindings_destroy**
> policies_bindings_destroy(policy_binding_uuid)



PolicyBinding Viewset

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
    api_instance = authentik.PoliciesApi(api_client)
    policy_binding_uuid = 'policy_binding_uuid_example' # str | A UUID string identifying this Policy Binding.

    try:
        api_instance.policies_bindings_destroy(policy_binding_uuid)
    except Exception as e:
        print("Exception when calling PoliciesApi->policies_bindings_destroy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_binding_uuid** | **str**| A UUID string identifying this Policy Binding. | 

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

# **policies_bindings_list**
> PaginatedPolicyBindingList policies_bindings_list(enabled=enabled, order=order, ordering=ordering, page=page, page_size=page_size, policy=policy, policy__isnull=policy__isnull, search=search, target=target, target_in=target_in, timeout=timeout)



PolicyBinding Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.paginated_policy_binding_list import PaginatedPolicyBindingList
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
    api_instance = authentik.PoliciesApi(api_client)
    enabled = True # bool |  (optional)
    order = 56 # int |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    policy = 'policy_example' # str |  (optional)
    policy__isnull = True # bool |  (optional)
    search = 'search_example' # str | A search term. (optional)
    target = 'target_example' # str |  (optional)
    target_in = ['target_in_example'] # List[str] |  (optional)
    timeout = 56 # int |  (optional)

    try:
        api_response = api_instance.policies_bindings_list(enabled=enabled, order=order, ordering=ordering, page=page, page_size=page_size, policy=policy, policy__isnull=policy__isnull, search=search, target=target, target_in=target_in, timeout=timeout)
        print("The response of PoliciesApi->policies_bindings_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->policies_bindings_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enabled** | **bool**|  | [optional] 
 **order** | **int**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **policy** | **str**|  | [optional] 
 **policy__isnull** | **bool**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **target** | **str**|  | [optional] 
 **target_in** | [**List[str]**](str.md)|  | [optional] 
 **timeout** | **int**|  | [optional] 

### Return type

[**PaginatedPolicyBindingList**](PaginatedPolicyBindingList.md)

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

# **policies_bindings_partial_update**
> PolicyBinding policies_bindings_partial_update(policy_binding_uuid, patched_policy_binding_request=patched_policy_binding_request)



PolicyBinding Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.patched_policy_binding_request import PatchedPolicyBindingRequest
from authentik.models.policy_binding import PolicyBinding
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
    api_instance = authentik.PoliciesApi(api_client)
    policy_binding_uuid = 'policy_binding_uuid_example' # str | A UUID string identifying this Policy Binding.
    patched_policy_binding_request = authentik.PatchedPolicyBindingRequest() # PatchedPolicyBindingRequest |  (optional)

    try:
        api_response = api_instance.policies_bindings_partial_update(policy_binding_uuid, patched_policy_binding_request=patched_policy_binding_request)
        print("The response of PoliciesApi->policies_bindings_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->policies_bindings_partial_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_binding_uuid** | **str**| A UUID string identifying this Policy Binding. | 
 **patched_policy_binding_request** | [**PatchedPolicyBindingRequest**](PatchedPolicyBindingRequest.md)|  | [optional] 

### Return type

[**PolicyBinding**](PolicyBinding.md)

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

# **policies_bindings_retrieve**
> PolicyBinding policies_bindings_retrieve(policy_binding_uuid)



PolicyBinding Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.policy_binding import PolicyBinding
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
    api_instance = authentik.PoliciesApi(api_client)
    policy_binding_uuid = 'policy_binding_uuid_example' # str | A UUID string identifying this Policy Binding.

    try:
        api_response = api_instance.policies_bindings_retrieve(policy_binding_uuid)
        print("The response of PoliciesApi->policies_bindings_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->policies_bindings_retrieve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_binding_uuid** | **str**| A UUID string identifying this Policy Binding. | 

### Return type

[**PolicyBinding**](PolicyBinding.md)

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

# **policies_bindings_update**
> PolicyBinding policies_bindings_update(policy_binding_uuid, policy_binding_request)



PolicyBinding Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.policy_binding import PolicyBinding
from authentik.models.policy_binding_request import PolicyBindingRequest
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
    api_instance = authentik.PoliciesApi(api_client)
    policy_binding_uuid = 'policy_binding_uuid_example' # str | A UUID string identifying this Policy Binding.
    policy_binding_request = authentik.PolicyBindingRequest() # PolicyBindingRequest | 

    try:
        api_response = api_instance.policies_bindings_update(policy_binding_uuid, policy_binding_request)
        print("The response of PoliciesApi->policies_bindings_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->policies_bindings_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_binding_uuid** | **str**| A UUID string identifying this Policy Binding. | 
 **policy_binding_request** | [**PolicyBindingRequest**](PolicyBindingRequest.md)|  | 

### Return type

[**PolicyBinding**](PolicyBinding.md)

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

# **policies_bindings_used_by_list**
> List[UsedBy] policies_bindings_used_by_list(policy_binding_uuid)



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
    api_instance = authentik.PoliciesApi(api_client)
    policy_binding_uuid = 'policy_binding_uuid_example' # str | A UUID string identifying this Policy Binding.

    try:
        api_response = api_instance.policies_bindings_used_by_list(policy_binding_uuid)
        print("The response of PoliciesApi->policies_bindings_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->policies_bindings_used_by_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_binding_uuid** | **str**| A UUID string identifying this Policy Binding. | 

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

# **policies_dummy_create**
> DummyPolicy policies_dummy_create(dummy_policy_request)



Dummy Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.dummy_policy import DummyPolicy
from authentik.models.dummy_policy_request import DummyPolicyRequest
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
    api_instance = authentik.PoliciesApi(api_client)
    dummy_policy_request = authentik.DummyPolicyRequest() # DummyPolicyRequest | 

    try:
        api_response = api_instance.policies_dummy_create(dummy_policy_request)
        print("The response of PoliciesApi->policies_dummy_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->policies_dummy_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dummy_policy_request** | [**DummyPolicyRequest**](DummyPolicyRequest.md)|  | 

### Return type

[**DummyPolicy**](DummyPolicy.md)

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

# **policies_dummy_destroy**
> policies_dummy_destroy(policy_uuid)



Dummy Viewset

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
    api_instance = authentik.PoliciesApi(api_client)
    policy_uuid = 'policy_uuid_example' # str | A UUID string identifying this Dummy Policy.

    try:
        api_instance.policies_dummy_destroy(policy_uuid)
    except Exception as e:
        print("Exception when calling PoliciesApi->policies_dummy_destroy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_uuid** | **str**| A UUID string identifying this Dummy Policy. | 

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

# **policies_dummy_list**
> PaginatedDummyPolicyList policies_dummy_list(created=created, execution_logging=execution_logging, last_updated=last_updated, name=name, ordering=ordering, page=page, page_size=page_size, policy_uuid=policy_uuid, result=result, search=search, wait_max=wait_max, wait_min=wait_min)



Dummy Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.paginated_dummy_policy_list import PaginatedDummyPolicyList
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
    api_instance = authentik.PoliciesApi(api_client)
    created = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    execution_logging = True # bool |  (optional)
    last_updated = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    policy_uuid = 'policy_uuid_example' # str |  (optional)
    result = True # bool |  (optional)
    search = 'search_example' # str | A search term. (optional)
    wait_max = 56 # int |  (optional)
    wait_min = 56 # int |  (optional)

    try:
        api_response = api_instance.policies_dummy_list(created=created, execution_logging=execution_logging, last_updated=last_updated, name=name, ordering=ordering, page=page, page_size=page_size, policy_uuid=policy_uuid, result=result, search=search, wait_max=wait_max, wait_min=wait_min)
        print("The response of PoliciesApi->policies_dummy_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->policies_dummy_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **created** | **datetime**|  | [optional] 
 **execution_logging** | **bool**|  | [optional] 
 **last_updated** | **datetime**|  | [optional] 
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **policy_uuid** | **str**|  | [optional] 
 **result** | **bool**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **wait_max** | **int**|  | [optional] 
 **wait_min** | **int**|  | [optional] 

### Return type

[**PaginatedDummyPolicyList**](PaginatedDummyPolicyList.md)

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

# **policies_dummy_partial_update**
> DummyPolicy policies_dummy_partial_update(policy_uuid, patched_dummy_policy_request=patched_dummy_policy_request)



Dummy Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.dummy_policy import DummyPolicy
from authentik.models.patched_dummy_policy_request import PatchedDummyPolicyRequest
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
    api_instance = authentik.PoliciesApi(api_client)
    policy_uuid = 'policy_uuid_example' # str | A UUID string identifying this Dummy Policy.
    patched_dummy_policy_request = authentik.PatchedDummyPolicyRequest() # PatchedDummyPolicyRequest |  (optional)

    try:
        api_response = api_instance.policies_dummy_partial_update(policy_uuid, patched_dummy_policy_request=patched_dummy_policy_request)
        print("The response of PoliciesApi->policies_dummy_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->policies_dummy_partial_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_uuid** | **str**| A UUID string identifying this Dummy Policy. | 
 **patched_dummy_policy_request** | [**PatchedDummyPolicyRequest**](PatchedDummyPolicyRequest.md)|  | [optional] 

### Return type

[**DummyPolicy**](DummyPolicy.md)

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

# **policies_dummy_retrieve**
> DummyPolicy policies_dummy_retrieve(policy_uuid)



Dummy Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.dummy_policy import DummyPolicy
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
    api_instance = authentik.PoliciesApi(api_client)
    policy_uuid = 'policy_uuid_example' # str | A UUID string identifying this Dummy Policy.

    try:
        api_response = api_instance.policies_dummy_retrieve(policy_uuid)
        print("The response of PoliciesApi->policies_dummy_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->policies_dummy_retrieve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_uuid** | **str**| A UUID string identifying this Dummy Policy. | 

### Return type

[**DummyPolicy**](DummyPolicy.md)

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

# **policies_dummy_update**
> DummyPolicy policies_dummy_update(policy_uuid, dummy_policy_request)



Dummy Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.dummy_policy import DummyPolicy
from authentik.models.dummy_policy_request import DummyPolicyRequest
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
    api_instance = authentik.PoliciesApi(api_client)
    policy_uuid = 'policy_uuid_example' # str | A UUID string identifying this Dummy Policy.
    dummy_policy_request = authentik.DummyPolicyRequest() # DummyPolicyRequest | 

    try:
        api_response = api_instance.policies_dummy_update(policy_uuid, dummy_policy_request)
        print("The response of PoliciesApi->policies_dummy_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->policies_dummy_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_uuid** | **str**| A UUID string identifying this Dummy Policy. | 
 **dummy_policy_request** | [**DummyPolicyRequest**](DummyPolicyRequest.md)|  | 

### Return type

[**DummyPolicy**](DummyPolicy.md)

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

# **policies_dummy_used_by_list**
> List[UsedBy] policies_dummy_used_by_list(policy_uuid)



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
    api_instance = authentik.PoliciesApi(api_client)
    policy_uuid = 'policy_uuid_example' # str | A UUID string identifying this Dummy Policy.

    try:
        api_response = api_instance.policies_dummy_used_by_list(policy_uuid)
        print("The response of PoliciesApi->policies_dummy_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->policies_dummy_used_by_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_uuid** | **str**| A UUID string identifying this Dummy Policy. | 

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

# **policies_event_matcher_create**
> EventMatcherPolicy policies_event_matcher_create(event_matcher_policy_request)



Event Matcher Policy Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.event_matcher_policy import EventMatcherPolicy
from authentik.models.event_matcher_policy_request import EventMatcherPolicyRequest
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
    api_instance = authentik.PoliciesApi(api_client)
    event_matcher_policy_request = authentik.EventMatcherPolicyRequest() # EventMatcherPolicyRequest | 

    try:
        api_response = api_instance.policies_event_matcher_create(event_matcher_policy_request)
        print("The response of PoliciesApi->policies_event_matcher_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->policies_event_matcher_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_matcher_policy_request** | [**EventMatcherPolicyRequest**](EventMatcherPolicyRequest.md)|  | 

### Return type

[**EventMatcherPolicy**](EventMatcherPolicy.md)

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

# **policies_event_matcher_destroy**
> policies_event_matcher_destroy(policy_uuid)



Event Matcher Policy Viewset

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
    api_instance = authentik.PoliciesApi(api_client)
    policy_uuid = 'policy_uuid_example' # str | A UUID string identifying this Event Matcher Policy.

    try:
        api_instance.policies_event_matcher_destroy(policy_uuid)
    except Exception as e:
        print("Exception when calling PoliciesApi->policies_event_matcher_destroy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_uuid** | **str**| A UUID string identifying this Event Matcher Policy. | 

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

# **policies_event_matcher_list**
> PaginatedEventMatcherPolicyList policies_event_matcher_list(action=action, app=app, client_ip=client_ip, created=created, execution_logging=execution_logging, last_updated=last_updated, model=model, name=name, ordering=ordering, page=page, page_size=page_size, policy_uuid=policy_uuid, search=search)



Event Matcher Policy Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.paginated_event_matcher_policy_list import PaginatedEventMatcherPolicyList
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
    api_instance = authentik.PoliciesApi(api_client)
    action = 'action_example' # str | Match created events with this action type. When left empty, all action types will be matched.  * `login` - Login * `login_failed` - Login Failed * `logout` - Logout * `user_write` - User Write * `suspicious_request` - Suspicious Request * `password_set` - Password Set * `secret_view` - Secret View * `secret_rotate` - Secret Rotate * `invitation_used` - Invite Used * `authorize_application` - Authorize Application * `source_linked` - Source Linked * `impersonation_started` - Impersonation Started * `impersonation_ended` - Impersonation Ended * `flow_execution` - Flow Execution * `policy_execution` - Policy Execution * `policy_exception` - Policy Exception * `property_mapping_exception` - Property Mapping Exception * `system_task_execution` - System Task Execution * `system_task_exception` - System Task Exception * `system_exception` - System Exception * `configuration_error` - Configuration Error * `model_created` - Model Created * `model_updated` - Model Updated * `model_deleted` - Model Deleted * `email_sent` - Email Sent * `update_available` - Update Available * `custom_` - Custom Prefix (optional)
    app = 'app_example' # str |  (optional)
    client_ip = 'client_ip_example' # str |  (optional)
    created = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    execution_logging = True # bool |  (optional)
    last_updated = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    model = 'model_example' # str |  (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    policy_uuid = 'policy_uuid_example' # str |  (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.policies_event_matcher_list(action=action, app=app, client_ip=client_ip, created=created, execution_logging=execution_logging, last_updated=last_updated, model=model, name=name, ordering=ordering, page=page, page_size=page_size, policy_uuid=policy_uuid, search=search)
        print("The response of PoliciesApi->policies_event_matcher_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->policies_event_matcher_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action** | **str**| Match created events with this action type. When left empty, all action types will be matched.  * &#x60;login&#x60; - Login * &#x60;login_failed&#x60; - Login Failed * &#x60;logout&#x60; - Logout * &#x60;user_write&#x60; - User Write * &#x60;suspicious_request&#x60; - Suspicious Request * &#x60;password_set&#x60; - Password Set * &#x60;secret_view&#x60; - Secret View * &#x60;secret_rotate&#x60; - Secret Rotate * &#x60;invitation_used&#x60; - Invite Used * &#x60;authorize_application&#x60; - Authorize Application * &#x60;source_linked&#x60; - Source Linked * &#x60;impersonation_started&#x60; - Impersonation Started * &#x60;impersonation_ended&#x60; - Impersonation Ended * &#x60;flow_execution&#x60; - Flow Execution * &#x60;policy_execution&#x60; - Policy Execution * &#x60;policy_exception&#x60; - Policy Exception * &#x60;property_mapping_exception&#x60; - Property Mapping Exception * &#x60;system_task_execution&#x60; - System Task Execution * &#x60;system_task_exception&#x60; - System Task Exception * &#x60;system_exception&#x60; - System Exception * &#x60;configuration_error&#x60; - Configuration Error * &#x60;model_created&#x60; - Model Created * &#x60;model_updated&#x60; - Model Updated * &#x60;model_deleted&#x60; - Model Deleted * &#x60;email_sent&#x60; - Email Sent * &#x60;update_available&#x60; - Update Available * &#x60;custom_&#x60; - Custom Prefix | [optional] 
 **app** | **str**|  | [optional] 
 **client_ip** | **str**|  | [optional] 
 **created** | **datetime**|  | [optional] 
 **execution_logging** | **bool**|  | [optional] 
 **last_updated** | **datetime**|  | [optional] 
 **model** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **policy_uuid** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedEventMatcherPolicyList**](PaginatedEventMatcherPolicyList.md)

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

# **policies_event_matcher_partial_update**
> EventMatcherPolicy policies_event_matcher_partial_update(policy_uuid, patched_event_matcher_policy_request=patched_event_matcher_policy_request)



Event Matcher Policy Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.event_matcher_policy import EventMatcherPolicy
from authentik.models.patched_event_matcher_policy_request import PatchedEventMatcherPolicyRequest
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
    api_instance = authentik.PoliciesApi(api_client)
    policy_uuid = 'policy_uuid_example' # str | A UUID string identifying this Event Matcher Policy.
    patched_event_matcher_policy_request = authentik.PatchedEventMatcherPolicyRequest() # PatchedEventMatcherPolicyRequest |  (optional)

    try:
        api_response = api_instance.policies_event_matcher_partial_update(policy_uuid, patched_event_matcher_policy_request=patched_event_matcher_policy_request)
        print("The response of PoliciesApi->policies_event_matcher_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->policies_event_matcher_partial_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_uuid** | **str**| A UUID string identifying this Event Matcher Policy. | 
 **patched_event_matcher_policy_request** | [**PatchedEventMatcherPolicyRequest**](PatchedEventMatcherPolicyRequest.md)|  | [optional] 

### Return type

[**EventMatcherPolicy**](EventMatcherPolicy.md)

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

# **policies_event_matcher_retrieve**
> EventMatcherPolicy policies_event_matcher_retrieve(policy_uuid)



Event Matcher Policy Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.event_matcher_policy import EventMatcherPolicy
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
    api_instance = authentik.PoliciesApi(api_client)
    policy_uuid = 'policy_uuid_example' # str | A UUID string identifying this Event Matcher Policy.

    try:
        api_response = api_instance.policies_event_matcher_retrieve(policy_uuid)
        print("The response of PoliciesApi->policies_event_matcher_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->policies_event_matcher_retrieve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_uuid** | **str**| A UUID string identifying this Event Matcher Policy. | 

### Return type

[**EventMatcherPolicy**](EventMatcherPolicy.md)

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

# **policies_event_matcher_update**
> EventMatcherPolicy policies_event_matcher_update(policy_uuid, event_matcher_policy_request)



Event Matcher Policy Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.event_matcher_policy import EventMatcherPolicy
from authentik.models.event_matcher_policy_request import EventMatcherPolicyRequest
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
    api_instance = authentik.PoliciesApi(api_client)
    policy_uuid = 'policy_uuid_example' # str | A UUID string identifying this Event Matcher Policy.
    event_matcher_policy_request = authentik.EventMatcherPolicyRequest() # EventMatcherPolicyRequest | 

    try:
        api_response = api_instance.policies_event_matcher_update(policy_uuid, event_matcher_policy_request)
        print("The response of PoliciesApi->policies_event_matcher_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->policies_event_matcher_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_uuid** | **str**| A UUID string identifying this Event Matcher Policy. | 
 **event_matcher_policy_request** | [**EventMatcherPolicyRequest**](EventMatcherPolicyRequest.md)|  | 

### Return type

[**EventMatcherPolicy**](EventMatcherPolicy.md)

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

# **policies_event_matcher_used_by_list**
> List[UsedBy] policies_event_matcher_used_by_list(policy_uuid)



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
    api_instance = authentik.PoliciesApi(api_client)
    policy_uuid = 'policy_uuid_example' # str | A UUID string identifying this Event Matcher Policy.

    try:
        api_response = api_instance.policies_event_matcher_used_by_list(policy_uuid)
        print("The response of PoliciesApi->policies_event_matcher_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->policies_event_matcher_used_by_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_uuid** | **str**| A UUID string identifying this Event Matcher Policy. | 

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

# **policies_expression_create**
> ExpressionPolicy policies_expression_create(expression_policy_request)



Source Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.expression_policy import ExpressionPolicy
from authentik.models.expression_policy_request import ExpressionPolicyRequest
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
    api_instance = authentik.PoliciesApi(api_client)
    expression_policy_request = authentik.ExpressionPolicyRequest() # ExpressionPolicyRequest | 

    try:
        api_response = api_instance.policies_expression_create(expression_policy_request)
        print("The response of PoliciesApi->policies_expression_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->policies_expression_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expression_policy_request** | [**ExpressionPolicyRequest**](ExpressionPolicyRequest.md)|  | 

### Return type

[**ExpressionPolicy**](ExpressionPolicy.md)

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

# **policies_expression_destroy**
> policies_expression_destroy(policy_uuid)



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
    api_instance = authentik.PoliciesApi(api_client)
    policy_uuid = 'policy_uuid_example' # str | A UUID string identifying this Expression Policy.

    try:
        api_instance.policies_expression_destroy(policy_uuid)
    except Exception as e:
        print("Exception when calling PoliciesApi->policies_expression_destroy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_uuid** | **str**| A UUID string identifying this Expression Policy. | 

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

# **policies_expression_list**
> PaginatedExpressionPolicyList policies_expression_list(created=created, execution_logging=execution_logging, expression=expression, last_updated=last_updated, name=name, ordering=ordering, page=page, page_size=page_size, policy_uuid=policy_uuid, search=search)



Source Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.paginated_expression_policy_list import PaginatedExpressionPolicyList
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
    api_instance = authentik.PoliciesApi(api_client)
    created = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    execution_logging = True # bool |  (optional)
    expression = 'expression_example' # str |  (optional)
    last_updated = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    policy_uuid = 'policy_uuid_example' # str |  (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.policies_expression_list(created=created, execution_logging=execution_logging, expression=expression, last_updated=last_updated, name=name, ordering=ordering, page=page, page_size=page_size, policy_uuid=policy_uuid, search=search)
        print("The response of PoliciesApi->policies_expression_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->policies_expression_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **created** | **datetime**|  | [optional] 
 **execution_logging** | **bool**|  | [optional] 
 **expression** | **str**|  | [optional] 
 **last_updated** | **datetime**|  | [optional] 
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **policy_uuid** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedExpressionPolicyList**](PaginatedExpressionPolicyList.md)

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

# **policies_expression_partial_update**
> ExpressionPolicy policies_expression_partial_update(policy_uuid, patched_expression_policy_request=patched_expression_policy_request)



Source Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.expression_policy import ExpressionPolicy
from authentik.models.patched_expression_policy_request import PatchedExpressionPolicyRequest
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
    api_instance = authentik.PoliciesApi(api_client)
    policy_uuid = 'policy_uuid_example' # str | A UUID string identifying this Expression Policy.
    patched_expression_policy_request = authentik.PatchedExpressionPolicyRequest() # PatchedExpressionPolicyRequest |  (optional)

    try:
        api_response = api_instance.policies_expression_partial_update(policy_uuid, patched_expression_policy_request=patched_expression_policy_request)
        print("The response of PoliciesApi->policies_expression_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->policies_expression_partial_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_uuid** | **str**| A UUID string identifying this Expression Policy. | 
 **patched_expression_policy_request** | [**PatchedExpressionPolicyRequest**](PatchedExpressionPolicyRequest.md)|  | [optional] 

### Return type

[**ExpressionPolicy**](ExpressionPolicy.md)

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

# **policies_expression_retrieve**
> ExpressionPolicy policies_expression_retrieve(policy_uuid)



Source Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.expression_policy import ExpressionPolicy
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
    api_instance = authentik.PoliciesApi(api_client)
    policy_uuid = 'policy_uuid_example' # str | A UUID string identifying this Expression Policy.

    try:
        api_response = api_instance.policies_expression_retrieve(policy_uuid)
        print("The response of PoliciesApi->policies_expression_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->policies_expression_retrieve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_uuid** | **str**| A UUID string identifying this Expression Policy. | 

### Return type

[**ExpressionPolicy**](ExpressionPolicy.md)

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

# **policies_expression_update**
> ExpressionPolicy policies_expression_update(policy_uuid, expression_policy_request)



Source Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.expression_policy import ExpressionPolicy
from authentik.models.expression_policy_request import ExpressionPolicyRequest
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
    api_instance = authentik.PoliciesApi(api_client)
    policy_uuid = 'policy_uuid_example' # str | A UUID string identifying this Expression Policy.
    expression_policy_request = authentik.ExpressionPolicyRequest() # ExpressionPolicyRequest | 

    try:
        api_response = api_instance.policies_expression_update(policy_uuid, expression_policy_request)
        print("The response of PoliciesApi->policies_expression_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->policies_expression_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_uuid** | **str**| A UUID string identifying this Expression Policy. | 
 **expression_policy_request** | [**ExpressionPolicyRequest**](ExpressionPolicyRequest.md)|  | 

### Return type

[**ExpressionPolicy**](ExpressionPolicy.md)

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

# **policies_expression_used_by_list**
> List[UsedBy] policies_expression_used_by_list(policy_uuid)



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
    api_instance = authentik.PoliciesApi(api_client)
    policy_uuid = 'policy_uuid_example' # str | A UUID string identifying this Expression Policy.

    try:
        api_response = api_instance.policies_expression_used_by_list(policy_uuid)
        print("The response of PoliciesApi->policies_expression_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->policies_expression_used_by_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_uuid** | **str**| A UUID string identifying this Expression Policy. | 

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

# **policies_password_create**
> PasswordPolicy policies_password_create(password_policy_request)



Password Policy Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.password_policy import PasswordPolicy
from authentik.models.password_policy_request import PasswordPolicyRequest
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
    api_instance = authentik.PoliciesApi(api_client)
    password_policy_request = authentik.PasswordPolicyRequest() # PasswordPolicyRequest | 

    try:
        api_response = api_instance.policies_password_create(password_policy_request)
        print("The response of PoliciesApi->policies_password_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->policies_password_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password_policy_request** | [**PasswordPolicyRequest**](PasswordPolicyRequest.md)|  | 

### Return type

[**PasswordPolicy**](PasswordPolicy.md)

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

# **policies_password_destroy**
> policies_password_destroy(policy_uuid)



Password Policy Viewset

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
    api_instance = authentik.PoliciesApi(api_client)
    policy_uuid = 'policy_uuid_example' # str | A UUID string identifying this Password Policy.

    try:
        api_instance.policies_password_destroy(policy_uuid)
    except Exception as e:
        print("Exception when calling PoliciesApi->policies_password_destroy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_uuid** | **str**| A UUID string identifying this Password Policy. | 

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

# **policies_password_expiry_create**
> PasswordExpiryPolicy policies_password_expiry_create(password_expiry_policy_request)



Password Expiry Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.password_expiry_policy import PasswordExpiryPolicy
from authentik.models.password_expiry_policy_request import PasswordExpiryPolicyRequest
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
    api_instance = authentik.PoliciesApi(api_client)
    password_expiry_policy_request = authentik.PasswordExpiryPolicyRequest() # PasswordExpiryPolicyRequest | 

    try:
        api_response = api_instance.policies_password_expiry_create(password_expiry_policy_request)
        print("The response of PoliciesApi->policies_password_expiry_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->policies_password_expiry_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password_expiry_policy_request** | [**PasswordExpiryPolicyRequest**](PasswordExpiryPolicyRequest.md)|  | 

### Return type

[**PasswordExpiryPolicy**](PasswordExpiryPolicy.md)

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

# **policies_password_expiry_destroy**
> policies_password_expiry_destroy(policy_uuid)



Password Expiry Viewset

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
    api_instance = authentik.PoliciesApi(api_client)
    policy_uuid = 'policy_uuid_example' # str | A UUID string identifying this Password Expiry Policy.

    try:
        api_instance.policies_password_expiry_destroy(policy_uuid)
    except Exception as e:
        print("Exception when calling PoliciesApi->policies_password_expiry_destroy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_uuid** | **str**| A UUID string identifying this Password Expiry Policy. | 

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

# **policies_password_expiry_list**
> PaginatedPasswordExpiryPolicyList policies_password_expiry_list(created=created, days=days, deny_only=deny_only, execution_logging=execution_logging, last_updated=last_updated, name=name, ordering=ordering, page=page, page_size=page_size, policy_uuid=policy_uuid, search=search)



Password Expiry Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.paginated_password_expiry_policy_list import PaginatedPasswordExpiryPolicyList
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
    api_instance = authentik.PoliciesApi(api_client)
    created = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    days = 56 # int |  (optional)
    deny_only = True # bool |  (optional)
    execution_logging = True # bool |  (optional)
    last_updated = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    policy_uuid = 'policy_uuid_example' # str |  (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.policies_password_expiry_list(created=created, days=days, deny_only=deny_only, execution_logging=execution_logging, last_updated=last_updated, name=name, ordering=ordering, page=page, page_size=page_size, policy_uuid=policy_uuid, search=search)
        print("The response of PoliciesApi->policies_password_expiry_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->policies_password_expiry_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **created** | **datetime**|  | [optional] 
 **days** | **int**|  | [optional] 
 **deny_only** | **bool**|  | [optional] 
 **execution_logging** | **bool**|  | [optional] 
 **last_updated** | **datetime**|  | [optional] 
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **policy_uuid** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedPasswordExpiryPolicyList**](PaginatedPasswordExpiryPolicyList.md)

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

# **policies_password_expiry_partial_update**
> PasswordExpiryPolicy policies_password_expiry_partial_update(policy_uuid, patched_password_expiry_policy_request=patched_password_expiry_policy_request)



Password Expiry Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.password_expiry_policy import PasswordExpiryPolicy
from authentik.models.patched_password_expiry_policy_request import PatchedPasswordExpiryPolicyRequest
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
    api_instance = authentik.PoliciesApi(api_client)
    policy_uuid = 'policy_uuid_example' # str | A UUID string identifying this Password Expiry Policy.
    patched_password_expiry_policy_request = authentik.PatchedPasswordExpiryPolicyRequest() # PatchedPasswordExpiryPolicyRequest |  (optional)

    try:
        api_response = api_instance.policies_password_expiry_partial_update(policy_uuid, patched_password_expiry_policy_request=patched_password_expiry_policy_request)
        print("The response of PoliciesApi->policies_password_expiry_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->policies_password_expiry_partial_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_uuid** | **str**| A UUID string identifying this Password Expiry Policy. | 
 **patched_password_expiry_policy_request** | [**PatchedPasswordExpiryPolicyRequest**](PatchedPasswordExpiryPolicyRequest.md)|  | [optional] 

### Return type

[**PasswordExpiryPolicy**](PasswordExpiryPolicy.md)

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

# **policies_password_expiry_retrieve**
> PasswordExpiryPolicy policies_password_expiry_retrieve(policy_uuid)



Password Expiry Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.password_expiry_policy import PasswordExpiryPolicy
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
    api_instance = authentik.PoliciesApi(api_client)
    policy_uuid = 'policy_uuid_example' # str | A UUID string identifying this Password Expiry Policy.

    try:
        api_response = api_instance.policies_password_expiry_retrieve(policy_uuid)
        print("The response of PoliciesApi->policies_password_expiry_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->policies_password_expiry_retrieve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_uuid** | **str**| A UUID string identifying this Password Expiry Policy. | 

### Return type

[**PasswordExpiryPolicy**](PasswordExpiryPolicy.md)

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

# **policies_password_expiry_update**
> PasswordExpiryPolicy policies_password_expiry_update(policy_uuid, password_expiry_policy_request)



Password Expiry Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.password_expiry_policy import PasswordExpiryPolicy
from authentik.models.password_expiry_policy_request import PasswordExpiryPolicyRequest
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
    api_instance = authentik.PoliciesApi(api_client)
    policy_uuid = 'policy_uuid_example' # str | A UUID string identifying this Password Expiry Policy.
    password_expiry_policy_request = authentik.PasswordExpiryPolicyRequest() # PasswordExpiryPolicyRequest | 

    try:
        api_response = api_instance.policies_password_expiry_update(policy_uuid, password_expiry_policy_request)
        print("The response of PoliciesApi->policies_password_expiry_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->policies_password_expiry_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_uuid** | **str**| A UUID string identifying this Password Expiry Policy. | 
 **password_expiry_policy_request** | [**PasswordExpiryPolicyRequest**](PasswordExpiryPolicyRequest.md)|  | 

### Return type

[**PasswordExpiryPolicy**](PasswordExpiryPolicy.md)

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

# **policies_password_expiry_used_by_list**
> List[UsedBy] policies_password_expiry_used_by_list(policy_uuid)



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
    api_instance = authentik.PoliciesApi(api_client)
    policy_uuid = 'policy_uuid_example' # str | A UUID string identifying this Password Expiry Policy.

    try:
        api_response = api_instance.policies_password_expiry_used_by_list(policy_uuid)
        print("The response of PoliciesApi->policies_password_expiry_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->policies_password_expiry_used_by_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_uuid** | **str**| A UUID string identifying this Password Expiry Policy. | 

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

# **policies_password_list**
> PaginatedPasswordPolicyList policies_password_list(amount_digits=amount_digits, amount_lowercase=amount_lowercase, amount_symbols=amount_symbols, amount_uppercase=amount_uppercase, check_have_i_been_pwned=check_have_i_been_pwned, check_static_rules=check_static_rules, check_zxcvbn=check_zxcvbn, created=created, error_message=error_message, execution_logging=execution_logging, hibp_allowed_count=hibp_allowed_count, last_updated=last_updated, length_min=length_min, name=name, ordering=ordering, page=page, page_size=page_size, password_field=password_field, policy_uuid=policy_uuid, search=search, symbol_charset=symbol_charset, zxcvbn_score_threshold=zxcvbn_score_threshold)



Password Policy Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.paginated_password_policy_list import PaginatedPasswordPolicyList
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
    api_instance = authentik.PoliciesApi(api_client)
    amount_digits = 56 # int |  (optional)
    amount_lowercase = 56 # int |  (optional)
    amount_symbols = 56 # int |  (optional)
    amount_uppercase = 56 # int |  (optional)
    check_have_i_been_pwned = True # bool |  (optional)
    check_static_rules = True # bool |  (optional)
    check_zxcvbn = True # bool |  (optional)
    created = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    error_message = 'error_message_example' # str |  (optional)
    execution_logging = True # bool |  (optional)
    hibp_allowed_count = 56 # int |  (optional)
    last_updated = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    length_min = 56 # int |  (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    password_field = 'password_field_example' # str |  (optional)
    policy_uuid = 'policy_uuid_example' # str |  (optional)
    search = 'search_example' # str | A search term. (optional)
    symbol_charset = 'symbol_charset_example' # str |  (optional)
    zxcvbn_score_threshold = 56 # int |  (optional)

    try:
        api_response = api_instance.policies_password_list(amount_digits=amount_digits, amount_lowercase=amount_lowercase, amount_symbols=amount_symbols, amount_uppercase=amount_uppercase, check_have_i_been_pwned=check_have_i_been_pwned, check_static_rules=check_static_rules, check_zxcvbn=check_zxcvbn, created=created, error_message=error_message, execution_logging=execution_logging, hibp_allowed_count=hibp_allowed_count, last_updated=last_updated, length_min=length_min, name=name, ordering=ordering, page=page, page_size=page_size, password_field=password_field, policy_uuid=policy_uuid, search=search, symbol_charset=symbol_charset, zxcvbn_score_threshold=zxcvbn_score_threshold)
        print("The response of PoliciesApi->policies_password_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->policies_password_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **amount_digits** | **int**|  | [optional] 
 **amount_lowercase** | **int**|  | [optional] 
 **amount_symbols** | **int**|  | [optional] 
 **amount_uppercase** | **int**|  | [optional] 
 **check_have_i_been_pwned** | **bool**|  | [optional] 
 **check_static_rules** | **bool**|  | [optional] 
 **check_zxcvbn** | **bool**|  | [optional] 
 **created** | **datetime**|  | [optional] 
 **error_message** | **str**|  | [optional] 
 **execution_logging** | **bool**|  | [optional] 
 **hibp_allowed_count** | **int**|  | [optional] 
 **last_updated** | **datetime**|  | [optional] 
 **length_min** | **int**|  | [optional] 
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **password_field** | **str**|  | [optional] 
 **policy_uuid** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **symbol_charset** | **str**|  | [optional] 
 **zxcvbn_score_threshold** | **int**|  | [optional] 

### Return type

[**PaginatedPasswordPolicyList**](PaginatedPasswordPolicyList.md)

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

# **policies_password_partial_update**
> PasswordPolicy policies_password_partial_update(policy_uuid, patched_password_policy_request=patched_password_policy_request)



Password Policy Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.password_policy import PasswordPolicy
from authentik.models.patched_password_policy_request import PatchedPasswordPolicyRequest
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
    api_instance = authentik.PoliciesApi(api_client)
    policy_uuid = 'policy_uuid_example' # str | A UUID string identifying this Password Policy.
    patched_password_policy_request = authentik.PatchedPasswordPolicyRequest() # PatchedPasswordPolicyRequest |  (optional)

    try:
        api_response = api_instance.policies_password_partial_update(policy_uuid, patched_password_policy_request=patched_password_policy_request)
        print("The response of PoliciesApi->policies_password_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->policies_password_partial_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_uuid** | **str**| A UUID string identifying this Password Policy. | 
 **patched_password_policy_request** | [**PatchedPasswordPolicyRequest**](PatchedPasswordPolicyRequest.md)|  | [optional] 

### Return type

[**PasswordPolicy**](PasswordPolicy.md)

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

# **policies_password_retrieve**
> PasswordPolicy policies_password_retrieve(policy_uuid)



Password Policy Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.password_policy import PasswordPolicy
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
    api_instance = authentik.PoliciesApi(api_client)
    policy_uuid = 'policy_uuid_example' # str | A UUID string identifying this Password Policy.

    try:
        api_response = api_instance.policies_password_retrieve(policy_uuid)
        print("The response of PoliciesApi->policies_password_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->policies_password_retrieve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_uuid** | **str**| A UUID string identifying this Password Policy. | 

### Return type

[**PasswordPolicy**](PasswordPolicy.md)

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

# **policies_password_update**
> PasswordPolicy policies_password_update(policy_uuid, password_policy_request)



Password Policy Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.password_policy import PasswordPolicy
from authentik.models.password_policy_request import PasswordPolicyRequest
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
    api_instance = authentik.PoliciesApi(api_client)
    policy_uuid = 'policy_uuid_example' # str | A UUID string identifying this Password Policy.
    password_policy_request = authentik.PasswordPolicyRequest() # PasswordPolicyRequest | 

    try:
        api_response = api_instance.policies_password_update(policy_uuid, password_policy_request)
        print("The response of PoliciesApi->policies_password_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->policies_password_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_uuid** | **str**| A UUID string identifying this Password Policy. | 
 **password_policy_request** | [**PasswordPolicyRequest**](PasswordPolicyRequest.md)|  | 

### Return type

[**PasswordPolicy**](PasswordPolicy.md)

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

# **policies_password_used_by_list**
> List[UsedBy] policies_password_used_by_list(policy_uuid)



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
    api_instance = authentik.PoliciesApi(api_client)
    policy_uuid = 'policy_uuid_example' # str | A UUID string identifying this Password Policy.

    try:
        api_response = api_instance.policies_password_used_by_list(policy_uuid)
        print("The response of PoliciesApi->policies_password_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->policies_password_used_by_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_uuid** | **str**| A UUID string identifying this Password Policy. | 

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

# **policies_reputation_create**
> ReputationPolicy policies_reputation_create(reputation_policy_request)



Reputation Policy Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.reputation_policy import ReputationPolicy
from authentik.models.reputation_policy_request import ReputationPolicyRequest
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
    api_instance = authentik.PoliciesApi(api_client)
    reputation_policy_request = authentik.ReputationPolicyRequest() # ReputationPolicyRequest | 

    try:
        api_response = api_instance.policies_reputation_create(reputation_policy_request)
        print("The response of PoliciesApi->policies_reputation_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->policies_reputation_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reputation_policy_request** | [**ReputationPolicyRequest**](ReputationPolicyRequest.md)|  | 

### Return type

[**ReputationPolicy**](ReputationPolicy.md)

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

# **policies_reputation_destroy**
> policies_reputation_destroy(policy_uuid)



Reputation Policy Viewset

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
    api_instance = authentik.PoliciesApi(api_client)
    policy_uuid = 'policy_uuid_example' # str | A UUID string identifying this Reputation Policy.

    try:
        api_instance.policies_reputation_destroy(policy_uuid)
    except Exception as e:
        print("Exception when calling PoliciesApi->policies_reputation_destroy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_uuid** | **str**| A UUID string identifying this Reputation Policy. | 

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

# **policies_reputation_list**
> PaginatedReputationPolicyList policies_reputation_list(check_ip=check_ip, check_username=check_username, created=created, execution_logging=execution_logging, last_updated=last_updated, name=name, ordering=ordering, page=page, page_size=page_size, policy_uuid=policy_uuid, search=search, threshold=threshold)



Reputation Policy Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.paginated_reputation_policy_list import PaginatedReputationPolicyList
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
    api_instance = authentik.PoliciesApi(api_client)
    check_ip = True # bool |  (optional)
    check_username = True # bool |  (optional)
    created = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    execution_logging = True # bool |  (optional)
    last_updated = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    name = 'name_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    policy_uuid = 'policy_uuid_example' # str |  (optional)
    search = 'search_example' # str | A search term. (optional)
    threshold = 56 # int |  (optional)

    try:
        api_response = api_instance.policies_reputation_list(check_ip=check_ip, check_username=check_username, created=created, execution_logging=execution_logging, last_updated=last_updated, name=name, ordering=ordering, page=page, page_size=page_size, policy_uuid=policy_uuid, search=search, threshold=threshold)
        print("The response of PoliciesApi->policies_reputation_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->policies_reputation_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_ip** | **bool**|  | [optional] 
 **check_username** | **bool**|  | [optional] 
 **created** | **datetime**|  | [optional] 
 **execution_logging** | **bool**|  | [optional] 
 **last_updated** | **datetime**|  | [optional] 
 **name** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **policy_uuid** | **str**|  | [optional] 
 **search** | **str**| A search term. | [optional] 
 **threshold** | **int**|  | [optional] 

### Return type

[**PaginatedReputationPolicyList**](PaginatedReputationPolicyList.md)

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

# **policies_reputation_partial_update**
> ReputationPolicy policies_reputation_partial_update(policy_uuid, patched_reputation_policy_request=patched_reputation_policy_request)



Reputation Policy Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.patched_reputation_policy_request import PatchedReputationPolicyRequest
from authentik.models.reputation_policy import ReputationPolicy
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
    api_instance = authentik.PoliciesApi(api_client)
    policy_uuid = 'policy_uuid_example' # str | A UUID string identifying this Reputation Policy.
    patched_reputation_policy_request = authentik.PatchedReputationPolicyRequest() # PatchedReputationPolicyRequest |  (optional)

    try:
        api_response = api_instance.policies_reputation_partial_update(policy_uuid, patched_reputation_policy_request=patched_reputation_policy_request)
        print("The response of PoliciesApi->policies_reputation_partial_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->policies_reputation_partial_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_uuid** | **str**| A UUID string identifying this Reputation Policy. | 
 **patched_reputation_policy_request** | [**PatchedReputationPolicyRequest**](PatchedReputationPolicyRequest.md)|  | [optional] 

### Return type

[**ReputationPolicy**](ReputationPolicy.md)

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

# **policies_reputation_retrieve**
> ReputationPolicy policies_reputation_retrieve(policy_uuid)



Reputation Policy Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.reputation_policy import ReputationPolicy
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
    api_instance = authentik.PoliciesApi(api_client)
    policy_uuid = 'policy_uuid_example' # str | A UUID string identifying this Reputation Policy.

    try:
        api_response = api_instance.policies_reputation_retrieve(policy_uuid)
        print("The response of PoliciesApi->policies_reputation_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->policies_reputation_retrieve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_uuid** | **str**| A UUID string identifying this Reputation Policy. | 

### Return type

[**ReputationPolicy**](ReputationPolicy.md)

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

# **policies_reputation_scores_destroy**
> policies_reputation_scores_destroy(reputation_uuid)



Reputation Viewset

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
    api_instance = authentik.PoliciesApi(api_client)
    reputation_uuid = 'reputation_uuid_example' # str | A UUID string identifying this reputation.

    try:
        api_instance.policies_reputation_scores_destroy(reputation_uuid)
    except Exception as e:
        print("Exception when calling PoliciesApi->policies_reputation_scores_destroy: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reputation_uuid** | **str**| A UUID string identifying this reputation. | 

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

# **policies_reputation_scores_list**
> PaginatedReputationList policies_reputation_scores_list(identifier=identifier, ip=ip, ordering=ordering, page=page, page_size=page_size, score=score, search=search)



Reputation Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.paginated_reputation_list import PaginatedReputationList
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
    api_instance = authentik.PoliciesApi(api_client)
    identifier = 'identifier_example' # str |  (optional)
    ip = 'ip_example' # str |  (optional)
    ordering = 'ordering_example' # str | Which field to use when ordering the results. (optional)
    page = 56 # int | A page number within the paginated result set. (optional)
    page_size = 56 # int | Number of results to return per page. (optional)
    score = 56 # int |  (optional)
    search = 'search_example' # str | A search term. (optional)

    try:
        api_response = api_instance.policies_reputation_scores_list(identifier=identifier, ip=ip, ordering=ordering, page=page, page_size=page_size, score=score, search=search)
        print("The response of PoliciesApi->policies_reputation_scores_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->policies_reputation_scores_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identifier** | **str**|  | [optional] 
 **ip** | **str**|  | [optional] 
 **ordering** | **str**| Which field to use when ordering the results. | [optional] 
 **page** | **int**| A page number within the paginated result set. | [optional] 
 **page_size** | **int**| Number of results to return per page. | [optional] 
 **score** | **int**|  | [optional] 
 **search** | **str**| A search term. | [optional] 

### Return type

[**PaginatedReputationList**](PaginatedReputationList.md)

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

# **policies_reputation_scores_retrieve**
> Reputation policies_reputation_scores_retrieve(reputation_uuid)



Reputation Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.reputation import Reputation
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
    api_instance = authentik.PoliciesApi(api_client)
    reputation_uuid = 'reputation_uuid_example' # str | A UUID string identifying this reputation.

    try:
        api_response = api_instance.policies_reputation_scores_retrieve(reputation_uuid)
        print("The response of PoliciesApi->policies_reputation_scores_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->policies_reputation_scores_retrieve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reputation_uuid** | **str**| A UUID string identifying this reputation. | 

### Return type

[**Reputation**](Reputation.md)

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

# **policies_reputation_scores_used_by_list**
> List[UsedBy] policies_reputation_scores_used_by_list(reputation_uuid)



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
    api_instance = authentik.PoliciesApi(api_client)
    reputation_uuid = 'reputation_uuid_example' # str | A UUID string identifying this reputation.

    try:
        api_response = api_instance.policies_reputation_scores_used_by_list(reputation_uuid)
        print("The response of PoliciesApi->policies_reputation_scores_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->policies_reputation_scores_used_by_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reputation_uuid** | **str**| A UUID string identifying this reputation. | 

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

# **policies_reputation_update**
> ReputationPolicy policies_reputation_update(policy_uuid, reputation_policy_request)



Reputation Policy Viewset

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.reputation_policy import ReputationPolicy
from authentik.models.reputation_policy_request import ReputationPolicyRequest
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
    api_instance = authentik.PoliciesApi(api_client)
    policy_uuid = 'policy_uuid_example' # str | A UUID string identifying this Reputation Policy.
    reputation_policy_request = authentik.ReputationPolicyRequest() # ReputationPolicyRequest | 

    try:
        api_response = api_instance.policies_reputation_update(policy_uuid, reputation_policy_request)
        print("The response of PoliciesApi->policies_reputation_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->policies_reputation_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_uuid** | **str**| A UUID string identifying this Reputation Policy. | 
 **reputation_policy_request** | [**ReputationPolicyRequest**](ReputationPolicyRequest.md)|  | 

### Return type

[**ReputationPolicy**](ReputationPolicy.md)

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

# **policies_reputation_used_by_list**
> List[UsedBy] policies_reputation_used_by_list(policy_uuid)



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
    api_instance = authentik.PoliciesApi(api_client)
    policy_uuid = 'policy_uuid_example' # str | A UUID string identifying this Reputation Policy.

    try:
        api_response = api_instance.policies_reputation_used_by_list(policy_uuid)
        print("The response of PoliciesApi->policies_reputation_used_by_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PoliciesApi->policies_reputation_used_by_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_uuid** | **str**| A UUID string identifying this Reputation Policy. | 

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

