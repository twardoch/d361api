"""
    Document360 Customer API

    Document360 RESTful APIs will allow you to integrate your documentation with your software, allowing you to easily onboard new users, manage your articles and more.   You can find detailed API documentation here : [API Documentation](https://apidocs.document360.io/docs)

    The version of the OpenAPI document: 2.0
    Contact: support@document360.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations

import json
import pprint
import re  # noqa: F401
from typing import Any, ClassVar, Self

from d361api.models.base_error import BaseError
from d361api.models.base_information import BaseInformation
from d361api.models.base_warning import BaseWarning
from d361api.models.category_simple_version_customer import \
    CategorySimpleVersionCustomer
from pydantic import BaseModel, ConfigDict, Field, StrictBool


class GetCategoryVersionsResponse(BaseModel):
    """
    GetCategoryVersionsResponse
    """
    versions: list[CategorySimpleVersionCustomer] | None = Field(default=None, description="get category data by version")
    extension_data: dict[str, Any] | None = Field(default=None, description="Extention data for customer API response")
    success: StrictBool | None = Field(default=None, description="Status indication for customer API response")
    errors: list[BaseError] | None = Field(default=None, description="Errors in the customer API response")
    warnings: list[BaseWarning] | None = Field(default=None, description="Warnings in the customer API response")
    information: list[BaseInformation] | None = Field(default=None, description="Information passed by the customer API response")
    __properties: ClassVar[list[str]] = ["versions", "extension_data", "success", "errors", "warnings", "information"]

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
    def from_json(cls, json_str: str) -> Self | None:
        """Create an instance of GetCategoryVersionsResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: set[str] = set()

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in versions (list)
        _items = []
        if self.versions:
            for _item_versions in self.versions:
                if _item_versions:
                    _items.append(_item_versions.to_dict())
            _dict['versions'] = _items
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
        # set to None if versions (nullable) is None
        # and model_fields_set contains the field
        if self.versions is None and "versions" in self.model_fields_set:
            _dict['versions'] = None

        # set to None if extension_data (nullable) is None
        # and model_fields_set contains the field
        if self.extension_data is None and "extension_data" in self.model_fields_set:
            _dict['extension_data'] = None

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

        return _dict

    @classmethod
    def from_dict(cls, obj: dict[str, Any] | None) -> Self | None:
        """Create an instance of GetCategoryVersionsResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "versions": [CategorySimpleVersionCustomer.from_dict(_item) for _item in obj["versions"]] if obj.get("versions") is not None else None,
            "extension_data": obj.get("extension_data"),
            "success": obj.get("success"),
            "errors": [BaseError.from_dict(_item) for _item in obj["errors"]] if obj.get("errors") is not None else None,
            "warnings": [BaseWarning.from_dict(_item) for _item in obj["warnings"]] if obj.get("warnings") is not None else None,
            "information": [BaseInformation.from_dict(_item) for _item in obj["information"]] if obj.get("information") is not None else None
        })
        return _obj


