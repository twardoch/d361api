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
from typing_extensions import Annotated
from d361api.models.article_content_type import ArticleContentType
from d361api.models.article_type import ArticleType
from typing import Optional, Set
from typing_extensions import Self

class CreateArticleRequest(BaseModel):
    """
    CreateArticleRequest
    """ # noqa: E501
    title: Annotated[str, Field(min_length=1, strict=True)] = Field(description="The title of the article")
    content: Optional[StrictStr] = Field(default=None, description="The content of the article, for any Editor type, use this property")
    category_id: Optional[StrictStr] = Field(default=None, description="The ID of the category where the article will be created, CategoryId will be null for custom pages")
    project_version_id: Annotated[str, Field(min_length=1, strict=True)] = Field(description="The project version ID in which the article will be created")
    order: Optional[StrictInt] = Field(default=None, description="The position of the article in the category tree (By default, it will be placed at the bottom of the category)")
    user_id: Annotated[str, Field(min_length=1, strict=True)] = Field(description="The ID of the team account that will be marked as a contributor of the article")
    content_type: Optional[ArticleContentType] = Field(default=None, description="0 - Markdown; 1 - WYSIWYG(HTML); 2 - Advanced WYSIWYG")
    article_type: Optional[ArticleType] = None
    __properties: ClassVar[List[str]] = ["title", "content", "category_id", "project_version_id", "order", "user_id", "content_type", "article_type"]

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
        """Create an instance of CreateArticleRequest from a JSON string"""
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
        # set to None if content (nullable) is None
        # and model_fields_set contains the field
        if self.content is None and "content" in self.model_fields_set:
            _dict['content'] = None

        # set to None if category_id (nullable) is None
        # and model_fields_set contains the field
        if self.category_id is None and "category_id" in self.model_fields_set:
            _dict['category_id'] = None

        # set to None if content_type (nullable) is None
        # and model_fields_set contains the field
        if self.content_type is None and "content_type" in self.model_fields_set:
            _dict['content_type'] = None

        # set to None if article_type (nullable) is None
        # and model_fields_set contains the field
        if self.article_type is None and "article_type" in self.model_fields_set:
            _dict['article_type'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateArticleRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "title": obj.get("title"),
            "content": obj.get("content"),
            "category_id": obj.get("category_id"),
            "project_version_id": obj.get("project_version_id"),
            "order": obj.get("order"),
            "user_id": obj.get("user_id"),
            "content_type": obj.get("content_type"),
            "article_type": obj.get("article_type")
        })
        return _obj


