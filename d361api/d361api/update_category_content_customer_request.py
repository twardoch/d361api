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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, Optional
from typing import Optional, Set
from typing_extensions import Self

class UpdateCategoryContentCustomerRequest(BaseModel):
    """
    UpdateCategoryContentCustomerRequest
    """ # noqa: E501
    title: Optional[StrictStr] = Field(default=None, description="The title of the category")
    content: Optional[StrictStr] = Field(default=None, description="The content of the category, for any Editor type, use this property.")
    html_content: Optional[StrictStr] = Field(default=None, description="The HTML content of the category. If the editor type is WYSIWYG (HTML), use this property - (This property is deprecated and will be removed in a future version of the API, Kindly use **content** property instead of this.)")
    block_content: Optional[StrictStr] = Field(default=None, description="The HTML content of the category. If the editor type is Block Editor (HTML), use this property - (This property is deprecated and will be removed in a future version of the API, Kindly use **content** property instead of this.)")
    version_number: Optional[StrictInt] = Field(default=None, description="The version number of the category to be updated. The latest version is updated by default.")
    translation_option: Optional[StrictStr] = Field(default=None, description="Translation status of the category. 0 - None, 1 - Needs translation, 2 Translated")
    source: Optional[StrictStr] = Field(default=None, description="Free text used for future reference")
    updated_by: Optional[StrictStr] = Field(default=None, description="The ID of the team account responsible for the category update")
    __properties: ClassVar[List[str]] = ["title", "content", "html_content", "block_content", "version_number", "translation_option", "source", "updated_by"]

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
        """Create an instance of UpdateCategoryContentCustomerRequest from a JSON string"""
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
        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if content (nullable) is None
        # and model_fields_set contains the field
        if self.content is None and "content" in self.model_fields_set:
            _dict['content'] = None

        # set to None if html_content (nullable) is None
        # and model_fields_set contains the field
        if self.html_content is None and "html_content" in self.model_fields_set:
            _dict['html_content'] = None

        # set to None if block_content (nullable) is None
        # and model_fields_set contains the field
        if self.block_content is None and "block_content" in self.model_fields_set:
            _dict['block_content'] = None

        # set to None if version_number (nullable) is None
        # and model_fields_set contains the field
        if self.version_number is None and "version_number" in self.model_fields_set:
            _dict['version_number'] = None

        # set to None if translation_option (nullable) is None
        # and model_fields_set contains the field
        if self.translation_option is None and "translation_option" in self.model_fields_set:
            _dict['translation_option'] = None

        # set to None if source (nullable) is None
        # and model_fields_set contains the field
        if self.source is None and "source" in self.model_fields_set:
            _dict['source'] = None

        # set to None if updated_by (nullable) is None
        # and model_fields_set contains the field
        if self.updated_by is None and "updated_by" in self.model_fields_set:
            _dict['updated_by'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpdateCategoryContentCustomerRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "title": obj.get("title"),
            "content": obj.get("content"),
            "html_content": obj.get("html_content"),
            "block_content": obj.get("block_content"),
            "version_number": obj.get("version_number"),
            "translation_option": obj.get("translation_option"),
            "source": obj.get("source"),
            "updated_by": obj.get("updated_by")
        })
        return _obj


