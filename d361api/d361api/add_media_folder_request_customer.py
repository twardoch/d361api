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


class AddMediaFolderRequestCustomer(BaseModel):
    """
    AddMediaFolderRequestCustomer
    """
    title: StrictStr | None = Field(default=None, description="The title of the folder")
    parent_folder_id: StrictStr | None = Field(default=None, description="The parent media folder ID")
    user_id: StrictStr | None = Field(default=None, description="The ID of the user")
    order: StrictInt | None = Field(default=None, description="The order of the folder")
    __properties: ClassVar[List[str]] = ["title", "parent_folder_id", "user_id", "order"]

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
        """Create an instance of AddMediaFolderRequestCustomer from a JSON string"""
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
        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if parent_folder_id (nullable) is None
        # and model_fields_set contains the field
        if self.parent_folder_id is None and "parent_folder_id" in self.model_fields_set:
            _dict['parent_folder_id'] = None

        # set to None if user_id (nullable) is None
        # and model_fields_set contains the field
        if self.user_id is None and "user_id" in self.model_fields_set:
            _dict['user_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict[str, Any] | None) -> Self | None:
        """Create an instance of AddMediaFolderRequestCustomer from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "title": obj.get("title"),
            "parent_folder_id": obj.get("parent_folder_id"),
            "user_id": obj.get("user_id"),
            "order": obj.get("order")
        })
        return _obj


