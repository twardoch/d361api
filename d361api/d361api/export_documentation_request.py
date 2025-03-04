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

from d361api.models.category_meta import CategoryMeta
from d361api.models.date_range import DateRange
from d361api.models.language_meta import LanguageMeta
from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr


class ExportDocumentationRequest(BaseModel):
    """
    ExportDocumentationRequest
    """
    entity: StrictStr | None = None
    version_id: list[StrictStr] | None = None
    selected_languages: list[LanguageMeta] | None = None
    selected_categories: list[CategoryMeta] | None = None
    exclude_media_files: StrictBool | None = None
    filter_by_article_modified_at: DateRange | None = None
    __properties: ClassVar[list[str]] = ["entity", "version_id", "selected_languages", "selected_categories", "exclude_media_files", "filter_by_article_modified_at"]

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
        """Create an instance of ExportDocumentationRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in selected_languages (list)
        _items = []
        if self.selected_languages:
            for _item_selected_languages in self.selected_languages:
                if _item_selected_languages:
                    _items.append(_item_selected_languages.to_dict())
            _dict['selected_languages'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in selected_categories (list)
        _items = []
        if self.selected_categories:
            for _item_selected_categories in self.selected_categories:
                if _item_selected_categories:
                    _items.append(_item_selected_categories.to_dict())
            _dict['selected_categories'] = _items
        # override the default output from pydantic by calling `to_dict()` of filter_by_article_modified_at
        if self.filter_by_article_modified_at:
            _dict['filter_by_article_modified_at'] = self.filter_by_article_modified_at.to_dict()
        # set to None if entity (nullable) is None
        # and model_fields_set contains the field
        if self.entity is None and "entity" in self.model_fields_set:
            _dict['entity'] = None

        # set to None if version_id (nullable) is None
        # and model_fields_set contains the field
        if self.version_id is None and "version_id" in self.model_fields_set:
            _dict['version_id'] = None

        # set to None if selected_languages (nullable) is None
        # and model_fields_set contains the field
        if self.selected_languages is None and "selected_languages" in self.model_fields_set:
            _dict['selected_languages'] = None

        # set to None if selected_categories (nullable) is None
        # and model_fields_set contains the field
        if self.selected_categories is None and "selected_categories" in self.model_fields_set:
            _dict['selected_categories'] = None

        # set to None if filter_by_article_modified_at (nullable) is None
        # and model_fields_set contains the field
        if self.filter_by_article_modified_at is None and "filter_by_article_modified_at" in self.model_fields_set:
            _dict['filter_by_article_modified_at'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict[str, Any] | None) -> Self | None:
        """Create an instance of ExportDocumentationRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "entity": obj.get("entity"),
            "version_id": obj.get("version_id"),
            "selected_languages": [LanguageMeta.from_dict(_item) for _item in obj["selected_languages"]] if obj.get("selected_languages") is not None else None,
            "selected_categories": [CategoryMeta.from_dict(_item) for _item in obj["selected_categories"]] if obj.get("selected_categories") is not None else None,
            "exclude_media_files": obj.get("exclude_media_files"),
            "filter_by_article_modified_at": DateRange.from_dict(obj["filter_by_article_modified_at"]) if obj.get("filter_by_article_modified_at") is not None else None
        })
        return _obj


