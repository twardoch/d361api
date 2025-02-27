# coding: utf-8

"""
    Document360 Customer API

    Document360 RESTful APIs will allow you to integrate your documentation with your software, allowing you to easily onboard new users, manage your articles and more.   You can find detailed API documentation here : [API Documentation](https://apidocs.document360.io/docs)

    The version of the OpenAPI document: 2.0
    Contact: support@document360.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from d361api.models.base_error import BaseError
from d361api.models.base_information import BaseInformation
from d361api.models.base_response_context import BaseResponseContext
from d361api.models.base_warning import BaseWarning
from d361api.models.feature_explorer_status import FeatureExplorerStatus
from d361api.models.ui_element import UIElement
from d361api.models.vector_search_reference_articles import VectorSearchReferenceArticles
from typing import Optional, Set
from typing_extensions import Self

class AIAssistiveSearch(BaseModel):
    """
    AIAssistiveSearch
    """ # noqa: E501
    prompt: Optional[StrictStr] = None
    result: Optional[StrictStr] = None
    reference_articles: Optional[List[VectorSearchReferenceArticles]] = None
    limit_exceeded: Optional[StrictBool] = None
    analytics_id: Optional[StrictStr] = None
    remaining_credits: Optional[StrictInt] = None
    extension_data: Optional[Dict[str, Any]] = None
    context: Optional[BaseResponseContext] = None
    success: Optional[StrictBool] = None
    errors: Optional[List[BaseError]] = None
    warnings: Optional[List[BaseWarning]] = None
    information: Optional[List[BaseInformation]] = None
    feature_explorer_status: Optional[FeatureExplorerStatus] = None
    custom_page_element: Optional[UIElement] = None
    __properties: ClassVar[List[str]] = ["prompt", "result", "reference_articles", "limit_exceeded", "analytics_id", "remaining_credits", "extension_data", "context", "success", "errors", "warnings", "information", "feature_explorer_status", "custom_page_element"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of AIAssistiveSearch from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in reference_articles (list)
        _items = []
        if self.reference_articles:
            for _item_reference_articles in self.reference_articles:
                if _item_reference_articles:
                    _items.append(_item_reference_articles.to_dict())
            _dict['reference_articles'] = _items
        # override the default output from pydantic by calling `to_dict()` of context
        if self.context:
            _dict['context'] = self.context.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in errors (list)
        _items = []
        if self.errors:
            for _item_errors in self.errors:
                if _item_errors:
                    _items.append(_item_errors.to_dict())
            _dict['errors'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in warnings (list)
        _items = []
        if self.warnings:
            for _item_warnings in self.warnings:
                if _item_warnings:
                    _items.append(_item_warnings.to_dict())
            _dict['warnings'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in information (list)
        _items = []
        if self.information:
            for _item_information in self.information:
                if _item_information:
                    _items.append(_item_information.to_dict())
            _dict['information'] = _items
        # override the default output from pydantic by calling `to_dict()` of feature_explorer_status
        if self.feature_explorer_status:
            _dict['feature_explorer_status'] = self.feature_explorer_status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of custom_page_element
        if self.custom_page_element:
            _dict['custom_page_element'] = self.custom_page_element.to_dict()
        # set to None if prompt (nullable) is None
        # and model_fields_set contains the field
        if self.prompt is None and "prompt" in self.model_fields_set:
            _dict['prompt'] = None

        # set to None if result (nullable) is None
        # and model_fields_set contains the field
        if self.result is None and "result" in self.model_fields_set:
            _dict['result'] = None

        # set to None if reference_articles (nullable) is None
        # and model_fields_set contains the field
        if self.reference_articles is None and "reference_articles" in self.model_fields_set:
            _dict['reference_articles'] = None

        # set to None if analytics_id (nullable) is None
        # and model_fields_set contains the field
        if self.analytics_id is None and "analytics_id" in self.model_fields_set:
            _dict['analytics_id'] = None

        # set to None if extension_data (nullable) is None
        # and model_fields_set contains the field
        if self.extension_data is None and "extension_data" in self.model_fields_set:
            _dict['extension_data'] = None

        # set to None if context (nullable) is None
        # and model_fields_set contains the field
        if self.context is None and "context" in self.model_fields_set:
            _dict['context'] = None

        # set to None if errors (nullable) is None
        # and model_fields_set contains the field
        if self.errors is None and "errors" in self.model_fields_set:
            _dict['errors'] = None

        # set to None if warnings (nullable) is None
        # and model_fields_set contains the field
        if self.warnings is None and "warnings" in self.model_fields_set:
            _dict['warnings'] = None

        # set to None if information (nullable) is None
        # and model_fields_set contains the field
        if self.information is None and "information" in self.model_fields_set:
            _dict['information'] = None

        # set to None if feature_explorer_status (nullable) is None
        # and model_fields_set contains the field
        if self.feature_explorer_status is None and "feature_explorer_status" in self.model_fields_set:
            _dict['feature_explorer_status'] = None

        # set to None if custom_page_element (nullable) is None
        # and model_fields_set contains the field
        if self.custom_page_element is None and "custom_page_element" in self.model_fields_set:
            _dict['custom_page_element'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AIAssistiveSearch from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "prompt": obj.get("prompt"),
            "result": obj.get("result"),
            "reference_articles": [VectorSearchReferenceArticles.from_dict(_item) for _item in obj["reference_articles"]] if obj.get("reference_articles") is not None else None,
            "limit_exceeded": obj.get("limit_exceeded"),
            "analytics_id": obj.get("analytics_id"),
            "remaining_credits": obj.get("remaining_credits"),
            "extension_data": obj.get("extension_data"),
            "context": BaseResponseContext.from_dict(obj["context"]) if obj.get("context") is not None else None,
            "success": obj.get("success"),
            "errors": [BaseError.from_dict(_item) for _item in obj["errors"]] if obj.get("errors") is not None else None,
            "warnings": [BaseWarning.from_dict(_item) for _item in obj["warnings"]] if obj.get("warnings") is not None else None,
            "information": [BaseInformation.from_dict(_item) for _item in obj["information"]] if obj.get("information") is not None else None,
            "feature_explorer_status": FeatureExplorerStatus.from_dict(obj["feature_explorer_status"]) if obj.get("feature_explorer_status") is not None else None,
            "custom_page_element": UIElement.from_dict(obj["custom_page_element"]) if obj.get("custom_page_element") is not None else None
        })
        return _obj


