# authentik.AdminApi

All URIs are relative to *http://localhost/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_apps_list**](AdminApi.md#admin_apps_list) | **GET** /admin/apps/ | 
[**admin_metrics_retrieve**](AdminApi.md#admin_metrics_retrieve) | **GET** /admin/metrics/ | 
[**admin_models_list**](AdminApi.md#admin_models_list) | **GET** /admin/models/ | 
[**admin_system_create**](AdminApi.md#admin_system_create) | **POST** /admin/system/ | 
[**admin_system_retrieve**](AdminApi.md#admin_system_retrieve) | **GET** /admin/system/ | 
[**admin_system_tasks_list**](AdminApi.md#admin_system_tasks_list) | **GET** /admin/system_tasks/ | 
[**admin_system_tasks_retrieve**](AdminApi.md#admin_system_tasks_retrieve) | **GET** /admin/system_tasks/{id}/ | 
[**admin_system_tasks_retry_create**](AdminApi.md#admin_system_tasks_retry_create) | **POST** /admin/system_tasks/{id}/retry/ | 
[**admin_version_retrieve**](AdminApi.md#admin_version_retrieve) | **GET** /admin/version/ | 
[**admin_workers_retrieve**](AdminApi.md#admin_workers_retrieve) | **GET** /admin/workers/ | 


# **admin_apps_list**
> List[App] admin_apps_list()



Read-only view list all installed apps

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.app import App
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
    api_instance = authentik.AdminApi(api_client)

    try:
        api_response = api_instance.admin_apps_list()
        print("The response of AdminApi->admin_apps_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_apps_list: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[App]**](App.md)

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

# **admin_metrics_retrieve**
> LoginMetrics admin_metrics_retrieve()



Login Metrics per 1h

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.login_metrics import LoginMetrics
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
    api_instance = authentik.AdminApi(api_client)

    try:
        api_response = api_instance.admin_metrics_retrieve()
        print("The response of AdminApi->admin_metrics_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_metrics_retrieve: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**LoginMetrics**](LoginMetrics.md)

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

# **admin_models_list**
> List[App] admin_models_list()



Read-only view list all installed models

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.app import App
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
    api_instance = authentik.AdminApi(api_client)

    try:
        api_response = api_instance.admin_models_list()
        print("The response of AdminApi->admin_models_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_models_list: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**List[App]**](App.md)

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

# **admin_system_create**
> System admin_system_create()



Get system information.

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.system import System
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
    api_instance = authentik.AdminApi(api_client)

    try:
        api_response = api_instance.admin_system_create()
        print("The response of AdminApi->admin_system_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_system_create: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**System**](System.md)

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

# **admin_system_retrieve**
> System admin_system_retrieve()



Get system information.

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.system import System
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
    api_instance = authentik.AdminApi(api_client)

    try:
        api_response = api_instance.admin_system_retrieve()
        print("The response of AdminApi->admin_system_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_system_retrieve: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**System**](System.md)

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

# **admin_system_tasks_list**
> List[Task] admin_system_tasks_list()



List system tasks

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
    api_instance = authentik.AdminApi(api_client)

    try:
        api_response = api_instance.admin_system_tasks_list()
        print("The response of AdminApi->admin_system_tasks_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_system_tasks_list: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

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

# **admin_system_tasks_retrieve**
> Task admin_system_tasks_retrieve(id)



Get a single system task

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
    api_instance = authentik.AdminApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.admin_system_tasks_retrieve(id)
        print("The response of AdminApi->admin_system_tasks_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_system_tasks_retrieve: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Task**](Task.md)

### Authorization

[authentik](../README.md#authentik)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**404** | Task not found |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_system_tasks_retry_create**
> admin_system_tasks_retry_create(id)



Retry task

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
    api_instance = authentik.AdminApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.admin_system_tasks_retry_create(id)
    except Exception as e:
        print("Exception when calling AdminApi->admin_system_tasks_retry_create: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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
**204** | Task retried successfully |  -  |
**404** | Task not found |  -  |
**500** | Failed to retry task |  -  |
**400** |  |  -  |
**403** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_version_retrieve**
> Version admin_version_retrieve()



Get running and latest version.

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.version import Version
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
    api_instance = authentik.AdminApi(api_client)

    try:
        api_response = api_instance.admin_version_retrieve()
        print("The response of AdminApi->admin_version_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_version_retrieve: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**Version**](Version.md)

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

# **admin_workers_retrieve**
> Workers admin_workers_retrieve()



Get currently connected worker count.

### Example

* Api Key Authentication (authentik):
```python
import time
import os
import authentik
from authentik.models.workers import Workers
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
    api_instance = authentik.AdminApi(api_client)

    try:
        api_response = api_instance.admin_workers_retrieve()
        print("The response of AdminApi->admin_workers_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_workers_retrieve: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**Workers**](Workers.md)

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

