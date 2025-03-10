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

from d361api.models.article_stale_status import ArticleStaleStatus
from pydantic import BaseModel, ConfigDict, Field, StrictStr


class StaleStatus(BaseModel):
    """
    StaleStatus
    """
    article_stale_status: ArticleStaleStatus | None = Field(default=None, description="The status of the article: 0 - None, 1 - New, 2 - Updated, 3 - Custom")
    stale_reason: StrictStr | None = None
    expired_at: datetime | None = None
    __properties: ClassVar[List[str]] = ["article_stale_status", "stale_reason", "expired_at"]

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
        """Create an instance of StaleStatus from a JSON string"""
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
        # set to None if stale_reason (nullable) is None
        # and model_fields_set contains the field
        if self.stale_reason is None and "stale_reason" in self.model_fields_set:
            _dict['stale_reason'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict[str, Any] | None) -> Self | None:
        """Create an instance of StaleStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "article_stale_status": obj.get("article_stale_status"),
            "stale_reason": obj.get("stale_reason"),
            "expired_at": obj.get("expired_at")
        })
        return _obj


