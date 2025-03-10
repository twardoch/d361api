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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr


class Title(BaseModel):
    """
    Title
    """
    value: StrictStr | None = Field(default=None, description="Markup text with occurrences highlighted.")
    match_level: StrictStr | None = Field(default=None, description="Indicates how well the attribute matched the search query. Can be: none, partial, full")
    fully_highlighted: StrictBool | None = None
    matched_words: list[StrictStr] | None = Field(default=None, description="List of words from the query that matched the object.")
    __properties: ClassVar[list[str]] = ["value", "match_level", "fully_highlighted", "matched_words"]

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
        """Create an instance of Title from a JSON string"""
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
        # set to None if value (nullable) is None
        # and model_fields_set contains the field
        if self.value is None and "value" in self.model_fields_set:
            _dict['value'] = None

        # set to None if match_level (nullable) is None
        # and model_fields_set contains the field
        if self.match_level is None and "match_level" in self.model_fields_set:
            _dict['match_level'] = None

        # set to None if matched_words (nullable) is None
        # and model_fields_set contains the field
        if self.matched_words is None and "matched_words" in self.model_fields_set:
            _dict['matched_words'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict[str, Any] | None) -> Self | None:
        """Create an instance of Title from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "value": obj.get("value"),
            "match_level": obj.get("match_level"),
            "fully_highlighted": obj.get("fully_highlighted"),
            "matched_words": obj.get("matched_words")
        })
        return _obj


