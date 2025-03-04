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
from datetime import datetime
from typing import Any, ClassVar, Self

from d361api.models.article_content_type import ArticleContentType
from d361api.models.article_status_customer import ArticleStatusCustomer
from d361api.models.language_translation_option import \
    LanguageTranslationOption
from pydantic import (BaseModel, ConfigDict, Field, StrictBool, StrictInt,
                      StrictStr)


class ArticleSimpleDataCustomer(BaseModel):
    """
    ArticleSimpleDataCustomer
    """
    id: StrictStr | None = Field(default=None, description="The ID of the article")
    title: StrictStr | None = Field(default=None, description="The article title")
    public_version: StrictInt | None = Field(default=None, description="The article version number(revision) that is currently published")
    latest_version: StrictInt | None = Field(default=None, description="The latest version number of this article")
    language_code: StrictStr | None = Field(default=None, description="The default language code")
    hidden: StrictBool | None = Field(default=None, description="Indicates if the article is visible on the site")
    status: ArticleStatusCustomer | None = Field(default=None, description="The status of the article: 0 - Draft, 3 - Published")
    order: StrictInt | None = Field(default=None, description="The position of the article inside the parent category")
    slug: StrictStr | None = Field(default=None, description="The slug of the article")
    content_type: ArticleContentType | None = Field(default=None, description="The content type of the article: Markdown = 0, Wysiwyg = 1, Block = 2")
    translation_option: LanguageTranslationOption | None = Field(default=None, description="The Translation status of the article")
    is_shared_article: StrictBool | None = Field(default=None, description="`True` indicates that the article is shared")
    modified_at: datetime | None = Field(default=None, description="Article modified date time")
    __properties: ClassVar[List[str]] = ["id", "title", "public_version", "latest_version", "language_code", "hidden", "status", "order", "slug", "content_type", "translation_option", "is_shared_article", "modified_at"]

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
        """Create an instance of ArticleSimpleDataCustomer from a JSON string"""
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
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if language_code (nullable) is None
        # and model_fields_set contains the field
        if self.language_code is None and "language_code" in self.model_fields_set:
            _dict['language_code'] = None

        # set to None if slug (nullable) is None
        # and model_fields_set contains the field
        if self.slug is None and "slug" in self.model_fields_set:
            _dict['slug'] = None

        # set to None if content_type (nullable) is None
        # and model_fields_set contains the field
        if self.content_type is None and "content_type" in self.model_fields_set:
            _dict['content_type'] = None

        # set to None if modified_at (nullable) is None
        # and model_fields_set contains the field
        if self.modified_at is None and "modified_at" in self.model_fields_set:
            _dict['modified_at'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict[str, Any] | None) -> Self | None:
        """Create an instance of ArticleSimpleDataCustomer from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "title": obj.get("title"),
            "public_version": obj.get("public_version"),
            "latest_version": obj.get("latest_version"),
            "language_code": obj.get("language_code"),
            "hidden": obj.get("hidden"),
            "status": obj.get("status"),
            "order": obj.get("order"),
            "slug": obj.get("slug"),
            "content_type": obj.get("content_type"),
            "translation_option": obj.get("translation_option"),
            "is_shared_article": obj.get("is_shared_article"),
            "modified_at": obj.get("modified_at")
        })
        return _obj


