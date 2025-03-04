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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr


class UpdateCategoryContentRequest(BaseModel):
    """
    Update category content
    """
    category_id: StrictStr | None = Field(default=None, description="Category ID for updating the content")
    lang_code: StrictStr | None = Field(default=None, description="Language Code for updating the content")
    title: StrictStr | None = Field(default=None, description="The title of the category")
    content: StrictStr | None = Field(default=None, description="The content of the category, for any Editor type, use this property.")
    html_content: StrictStr | None = Field(default=None, description="The HTML content of the category. If the editor type is WYSIWYG (HTML), use this property - (This property is deprecated and will be removed in a future version of the API, Kindly use **content** property instead of this.)")
    block_content: StrictStr | None = Field(default=None, description="The HTML content of the category. If the editor type is Block Editor (HTML), use this property - (This property is deprecated and will be removed in a future version of the API, Kindly use **content** property instead of this.)")
    version_number: StrictInt | None = Field(default=None, description="The version number of the category to be updated. The latest version is updated by default.")
    translation_option: StrictStr | None = Field(default=None, description="Translation status of the category. 0 - None, 1 - Needs translation, 2 Translated")
    source: StrictStr | None = Field(default=None, description="Free text used for future reference")
    updated_by: StrictStr | None = Field(default=None, description="The ID of the team account responsible for the category update")
    __properties: ClassVar[List[str]] = ["category_id", "lang_code", "title", "content", "html_content", "block_content", "version_number", "translation_option", "source", "updated_by"]

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
        """Create an instance of UpdateCategoryContentRequest from a JSON string"""
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
        # set to None if category_id (nullable) is None
        # and model_fields_set contains the field
        if self.category_id is None and "category_id" in self.model_fields_set:
            _dict['category_id'] = None

        # set to None if lang_code (nullable) is None
        # and model_fields_set contains the field
        if self.lang_code is None and "lang_code" in self.model_fields_set:
            _dict['lang_code'] = None

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
    def from_dict(cls, obj: dict[str, Any] | None) -> Self | None:
        """Create an instance of UpdateCategoryContentRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "category_id": obj.get("category_id"),
            "lang_code": obj.get("lang_code"),
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


