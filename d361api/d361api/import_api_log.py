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

from d361api.models.import_documentation_log_action import \
    ImportDocumentationLogAction
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr


class ImportAPILog(BaseModel):
    """
    ImportAPILog
    """
    new_versions: StrictInt | None = Field(default=None, description="The number of versions imported")
    categories: StrictInt | None = Field(default=None, description="The number of categories imported")
    articles: StrictInt | None = Field(default=None, description="The number of articles imported")
    languages: StrictStr | None = Field(default=None, description="The number of languages imported")
    messages: list[ImportDocumentationLogAction] | None = None
    __properties: ClassVar[list[str]] = ["new_versions", "categories", "articles", "languages", "messages"]

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
        """Create an instance of ImportAPILog from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in messages (list)
        _items = []
        if self.messages:
            for _item_messages in self.messages:
                if _item_messages:
                    _items.append(_item_messages.to_dict())
            _dict['messages'] = _items
        # set to None if languages (nullable) is None
        # and model_fields_set contains the field
        if self.languages is None and "languages" in self.model_fields_set:
            _dict['languages'] = None

        # set to None if messages (nullable) is None
        # and model_fields_set contains the field
        if self.messages is None and "messages" in self.model_fields_set:
            _dict['messages'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict[str, Any] | None) -> Self | None:
        """Create an instance of ImportAPILog from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "new_versions": obj.get("new_versions"),
            "categories": obj.get("categories"),
            "articles": obj.get("articles"),
            "languages": obj.get("languages"),
            "messages": [ImportDocumentationLogAction.from_dict(_item) for _item in obj["messages"]] if obj.get("messages") is not None else None
        })
        return _obj


