# stylelens_search.SearchApi

All URIs are relative to *http://search.stylelens.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_image**](SearchApi.md#search_image) | **POST** /images | Query to search images


# **search_image**
> ImageSearchResponse search_image(file=file)

Query to search images



### Example 
```python
from __future__ import print_function
import time
import stylelens_search
from stylelens_search.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = stylelens_search.SearchApi()
file = '/path/to/file.jpg' # file | Image file to upload (only support jpg format yet) (optional)

try: 
    # Query to search images
    api_response = api_instance.search_image(file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| Image file to upload (only support jpg format yet) | [optional] 

### Return type

[**ImageSearchResponse**](ImageSearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

