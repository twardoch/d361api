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

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from d361api.models.add_user_data import AddUserData
from d361api.models.base_error import BaseError
from d361api.models.base_information import BaseInformation
from d361api.models.base_warning import BaseWarning
from typing import Optional, Set
from typing_extensions import Self

class AddUserDataCustomerApiResponse(BaseModel):
    """
    AddUserDataCustomerApiResponse
    """ # noqa: E501
    result: Optional[AddUserData] = Field(default=None, description="Customer API response data")
    extension_data: Optional[Dict[str, Any]] = Field(default=None, description="Extention data for customer API response")
    success: Optional[StrictBool] = Field(default=None, description="Status indication for customer API response")
    errors: Optional[List[BaseError]] = Field(default=None, description="Errors in the customer API response")
    warnings: Optional[List[BaseWarning]] = Field(default=None, description="Warnings in the customer API response")
    information: Optional[List[BaseInformation]] = Field(default=None, description="Information passed by the customer API response")
    __properties: ClassVar[List[str]] = ["result", "extension_data", "success", "errors", "warnings", "information"]

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
        """Create an instance of AddUserDataCustomerApiResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of result
        if self.result:
            _dict['result'] = self.result.to_dict()
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
        # set to None if result (nullable) is None
        # and model_fields_set contains the field
        if self.result is None and "result" in self.model_fields_set:
            _dict['result'] = None

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
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AddUserDataCustomerApiResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "result": AddUserData.from_dict(obj["result"]) if obj.get("result") is not None else None,
            "extension_data": obj.get("extension_data"),
            "success": obj.get("success"),
            "errors": [BaseError.from_dict(_item) for _item in obj["errors"]] if obj.get("errors") is not None else None,
            "warnings": [BaseWarning.from_dict(_item) for _item in obj["warnings"]] if obj.get("warnings") is not None else None,
            "information": [BaseInformation.from_dict(_item) for _item in obj["information"]] if obj.get("information") is not None else None
        })
        return _obj


