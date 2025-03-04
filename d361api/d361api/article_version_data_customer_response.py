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
from d361api.models.category_type import CategoryType
from d361api.models.language_translation_option import \
    LanguageTranslationOption
from d361api.models.user_details_customer import UserDetailsCustomer
from pydantic import (BaseModel, ConfigDict, Field, StrictBool, StrictInt,
                      StrictStr)


class ArticleVersionDataCustomerResponse(BaseModel):
    """
    ArticleVersionDataCustomerResponse
    """
    id: StrictStr | None = Field(default=None, description="The ID of the article")
    title: StrictStr | None = Field(default=None, description="The title of the article")
    content: StrictStr | None = Field(default=None, description="If the article editor is **Markdown**, then the article content will be present in this property")
    html_content: StrictStr | None = Field(default=None, description=" If the article editor is **WYSIWYG (HTML)**, then the content will be present in this property.   **Note**: Markdown editor will also have HTML content (read-only).")
    category_id: StrictStr | None = Field(default=None, description="The ID of the article's parent category")
    project_version_id: StrictStr | None = Field(default=None, description="The ID of the project version where the article is located")
    version_number: StrictInt | None = Field(default=None, description="The currently fetched version number of the article")
    public_version: StrictInt | None = Field(default=None, description="The currently published version number of the article")
    latest_version: StrictInt | None = Field(default=None, description="The latest version number of the article")
    enable_rtl: StrictBool | None = Field(default=None, description="`True` indicates that **Right to Left** alignment is enabled for the article language")
    hidden: StrictBool | None = Field(default=None, description="`False` indicates that the article is visible on the site")
    status: ArticleStatusCustomer | None = Field(default=None, description="The status of the article: 0 - Draft, 3 - Published")
    order: StrictInt | None = Field(default=None, description="The position inside the parent category")
    created_by: StrictStr | None = Field(default=None, description="The ID of the team account who created the article")
    authors: list[UserDetailsCustomer] | None = Field(default=None, description="The list of contributors in the article")
    created_at: datetime | None = Field(default=None, description="The date on which the article was created")
    modified_at: datetime | None = Field(default=None, description="The date on which the article was last modified")
    slug: StrictStr | None = Field(default=None, description="The slug of the article")
    is_fall_back_content: StrictBool | None = Field(default=None, description="`True` indicates that the article content is a fallback of the default language content")
    description: StrictStr | None = Field(default=None, description="The description of the article")
    category_type: CategoryType | None = Field(default=None, description="0 - Folder, 1 - Page, 2 - Index")
    content_type: ArticleContentType | None = Field(default=None, description="0 - Markdown; 1 - WYSIWYG(HTML); 2 - Advanced WYSIWYG")
    is_shared_article: StrictBool | None = Field(default=None, description="`True` indicates that the article is shared")
    translation_option: LanguageTranslationOption | None = Field(default=None, description="The Translation status of the article")
    url: StrictStr | None = Field(default=None, description="Url of the article")
    __properties: ClassVar[list[str]] = ["id", "title", "content", "html_content", "category_id", "project_version_id", "version_number", "public_version", "latest_version", "enable_rtl", "hidden", "status", "order", "created_by", "authors", "created_at", "modified_at", "slug", "is_fall_back_content", "description", "category_type", "content_type", "is_shared_article", "translation_option", "url"]

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
        """Create an instance of ArticleVersionDataCustomerResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in authors (list)
        _items = []
        if self.authors:
            for _item_authors in self.authors:
                if _item_authors:
                    _items.append(_item_authors.to_dict())
            _dict['authors'] = _items
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

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

        # set to None if category_id (nullable) is None
        # and model_fields_set contains the field
        if self.category_id is None and "category_id" in self.model_fields_set:
            _dict['category_id'] = None

        # set to None if project_version_id (nullable) is None
        # and model_fields_set contains the field
        if self.project_version_id is None and "project_version_id" in self.model_fields_set:
            _dict['project_version_id'] = None

        # set to None if created_by (nullable) is None
        # and model_fields_set contains the field
        if self.created_by is None and "created_by" in self.model_fields_set:
            _dict['created_by'] = None

        # set to None if authors (nullable) is None
        # and model_fields_set contains the field
        if self.authors is None and "authors" in self.model_fields_set:
            _dict['authors'] = None

        # set to None if slug (nullable) is None
        # and model_fields_set contains the field
        if self.slug is None and "slug" in self.model_fields_set:
            _dict['slug'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if category_type (nullable) is None
        # and model_fields_set contains the field
        if self.category_type is None and "category_type" in self.model_fields_set:
            _dict['category_type'] = None

        # set to None if content_type (nullable) is None
        # and model_fields_set contains the field
        if self.content_type is None and "content_type" in self.model_fields_set:
            _dict['content_type'] = None

        # set to None if url (nullable) is None
        # and model_fields_set contains the field
        if self.url is None and "url" in self.model_fields_set:
            _dict['url'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict[str, Any] | None) -> Self | None:
        """Create an instance of ArticleVersionDataCustomerResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "title": obj.get("title"),
            "content": obj.get("content"),
            "html_content": obj.get("html_content"),
            "category_id": obj.get("category_id"),
            "project_version_id": obj.get("project_version_id"),
            "version_number": obj.get("version_number"),
            "public_version": obj.get("public_version"),
            "latest_version": obj.get("latest_version"),
            "enable_rtl": obj.get("enable_rtl"),
            "hidden": obj.get("hidden"),
            "status": obj.get("status"),
            "order": obj.get("order"),
            "created_by": obj.get("created_by"),
            "authors": [UserDetailsCustomer.from_dict(_item) for _item in obj["authors"]] if obj.get("authors") is not None else None,
            "created_at": obj.get("created_at"),
            "modified_at": obj.get("modified_at"),
            "slug": obj.get("slug"),
            "is_fall_back_content": obj.get("is_fall_back_content"),
            "description": obj.get("description"),
            "category_type": obj.get("category_type"),
            "content_type": obj.get("content_type"),
            "is_shared_article": obj.get("is_shared_article"),
            "translation_option": obj.get("translation_option"),
            "url": obj.get("url")
        })
        return _obj


