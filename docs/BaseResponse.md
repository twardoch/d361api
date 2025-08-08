# BaseResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extension_data** | **object** |  | [optional] 
**context** | [**BaseResponseContext**](BaseResponseContext.md) |  | [optional] 
**success** | **bool** |  | [optional] 
**errors** | [**List[BaseError]**](BaseError.md) |  | [optional] 
**warnings** | [**List[BaseWarning]**](BaseWarning.md) |  | [optional] 
**information** | [**List[BaseInformation]**](BaseInformation.md) |  | [optional] 
**feature_explorer_status** | [**FeatureExplorerStatus**](FeatureExplorerStatus.md) |  | [optional] 
**custom_page_element** | [**UIElement**](UIElement.md) |  | [optional] 

## Example

```python
from d361api.d361api.base_response import BaseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BaseResponse from a JSON string
base_response_instance = BaseResponse.from_json(json)
# print the JSON string representation of the object
print(BaseResponse.to_json())

# convert the object into a dict
base_response_dict = base_response_instance.to_dict()
# create an instance of BaseResponse from a dict
base_response_from_dict = BaseResponse.from_dict(base_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


