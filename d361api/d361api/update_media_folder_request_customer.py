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
import re
from typing import Annotated, Any, ClassVar, Self

from pydantic import (BaseModel, ConfigDict, Field, StrictBool, StrictInt,
                      StrictStr, field_validator)


class UpdateMediaFolderRequestCustomer(BaseModel):
    """
    UpdateMediaFolderRequestCustomer
    """
    name: StrictStr | None = Field(default=None, description="The new name for the folder being updated")
    order: StrictInt | None = Field(default=None, description="The order of the folder")
    folder_color: Annotated[str, Field(strict=True)] | None = Field(default=None, description="The color of the folder - should be in hexadecimal color code format")
    is_starred: StrictBool | None = Field(default=None, description="To update the folder as starred")
    __properties: ClassVar[List[str]] = ["name", "order", "folder_color", "is_starred"]

    @field_validator('folder_color')
    def folder_color_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$", value):
            raise ValueError(r"must validate the regular expression /^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$/")
        return value

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
        """Create an instance of UpdateMediaFolderRequestCustomer from a JSON string"""
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
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if order (nullable) is None
        # and model_fields_set contains the field
        if self.order is None and "order" in self.model_fields_set:
            _dict['order'] = None

        # set to None if folder_color (nullable) is None
        # and model_fields_set contains the field
        if self.folder_color is None and "folder_color" in self.model_fields_set:
            _dict['folder_color'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict[str, Any] | None) -> Self | None:
        """Create an instance of UpdateMediaFolderRequestCustomer from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "order": obj.get("order"),
            "folder_color": obj.get("folder_color"),
            "is_starred": obj.get("is_starred")
        })
        return _obj


