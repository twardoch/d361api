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

from pydantic import (BaseModel, ConfigDict, Field, StrictBool, StrictInt,
                      StrictStr)


class MediaFolderMetaDataCustomer(BaseModel):
    """
    MediaFolderMetaDataCustomer
    """
    media_folder_id: StrictStr | None = Field(default=None, description="The folder ID")
    media_folder_title: StrictStr | None = Field(default=None, description="The folder title")
    order: StrictInt | None = Field(default=None, description="The folder order")
    icon: StrictStr | None = Field(default=None, description="The folder icon")
    updated_on: datetime | None = Field(default=None, description="The date the file was modified")
    folder_color: StrictStr | None = Field(default=None, description="The folder color")
    is_starred: StrictBool | None = Field(default=None, description="This denotes the file is starred or not")
    updated_by: StrictStr | None = Field(default=None, description="The ID of the user who uploaded the folder")
    parent_media_folder_id: StrictStr | None = Field(default=None, description="The parent folder ID")
    __properties: ClassVar[List[str]] = ["media_folder_id", "media_folder_title", "order", "icon", "updated_on", "folder_color", "is_starred", "updated_by", "parent_media_folder_id"]

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
        """Create an instance of MediaFolderMetaDataCustomer from a JSON string"""
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
        # set to None if media_folder_id (nullable) is None
        # and model_fields_set contains the field
        if self.media_folder_id is None and "media_folder_id" in self.model_fields_set:
            _dict['media_folder_id'] = None

        # set to None if media_folder_title (nullable) is None
        # and model_fields_set contains the field
        if self.media_folder_title is None and "media_folder_title" in self.model_fields_set:
            _dict['media_folder_title'] = None

        # set to None if icon (nullable) is None
        # and model_fields_set contains the field
        if self.icon is None and "icon" in self.model_fields_set:
            _dict['icon'] = None

        # set to None if folder_color (nullable) is None
        # and model_fields_set contains the field
        if self.folder_color is None and "folder_color" in self.model_fields_set:
            _dict['folder_color'] = None

        # set to None if updated_by (nullable) is None
        # and model_fields_set contains the field
        if self.updated_by is None and "updated_by" in self.model_fields_set:
            _dict['updated_by'] = None

        # set to None if parent_media_folder_id (nullable) is None
        # and model_fields_set contains the field
        if self.parent_media_folder_id is None and "parent_media_folder_id" in self.model_fields_set:
            _dict['parent_media_folder_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict[str, Any] | None) -> Self | None:
        """Create an instance of MediaFolderMetaDataCustomer from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "media_folder_id": obj.get("media_folder_id"),
            "media_folder_title": obj.get("media_folder_title"),
            "order": obj.get("order"),
            "icon": obj.get("icon"),
            "updated_on": obj.get("updated_on"),
            "folder_color": obj.get("folder_color"),
            "is_starred": obj.get("is_starred"),
            "updated_by": obj.get("updated_by"),
            "parent_media_folder_id": obj.get("parent_media_folder_id")
        })
        return _obj


