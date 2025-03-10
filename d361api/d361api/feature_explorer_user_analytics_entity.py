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

from d361api.models.feature_analytics import FeatureAnalytics
from d361api.models.trophy_status import TrophyStatus
from pydantic import (BaseModel, ConfigDict, StrictBool, StrictFloat,
                      StrictInt, StrictStr)


class FeatureExplorerUserAnalyticsEntity(BaseModel):
    """
    FeatureExplorerUserAnalyticsEntity
    """
    id: StrictStr | None = None
    project_id: StrictStr | None = None
    user_id: StrictStr | None = None
    trophy_status: TrophyStatus | None = None
    show_default: StrictBool | None = None
    show_advanced_section_popup: StrictBool | None = None
    hide_popup: StrictBool | None = None
    hide_popup_date: datetime | None = None
    is_advanced_section_unlocked: StrictBool | None = None
    usage_score: StrictFloat | StrictInt | None = None
    features: list[FeatureAnalytics] | None = None
    is_closed_content_reuse_info: StrictBool | None = None
    __properties: ClassVar[list[str]] = ["id", "project_id", "user_id", "trophy_status", "show_default", "show_advanced_section_popup", "hide_popup", "hide_popup_date", "is_advanced_section_unlocked", "usage_score", "features", "is_closed_content_reuse_info"]

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
        """Create an instance of FeatureExplorerUserAnalyticsEntity from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of trophy_status
        if self.trophy_status:
            _dict['trophy_status'] = self.trophy_status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in features (list)
        _items = []
        if self.features:
            for _item_features in self.features:
                if _item_features:
                    _items.append(_item_features.to_dict())
            _dict['features'] = _items
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if project_id (nullable) is None
        # and model_fields_set contains the field
        if self.project_id is None and "project_id" in self.model_fields_set:
            _dict['project_id'] = None

        # set to None if user_id (nullable) is None
        # and model_fields_set contains the field
        if self.user_id is None and "user_id" in self.model_fields_set:
            _dict['user_id'] = None

        # set to None if trophy_status (nullable) is None
        # and model_fields_set contains the field
        if self.trophy_status is None and "trophy_status" in self.model_fields_set:
            _dict['trophy_status'] = None

        # set to None if features (nullable) is None
        # and model_fields_set contains the field
        if self.features is None and "features" in self.model_fields_set:
            _dict['features'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict[str, Any] | None) -> Self | None:
        """Create an instance of FeatureExplorerUserAnalyticsEntity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "project_id": obj.get("project_id"),
            "user_id": obj.get("user_id"),
            "trophy_status": TrophyStatus.from_dict(obj["trophy_status"]) if obj.get("trophy_status") is not None else None,
            "show_default": obj.get("show_default"),
            "show_advanced_section_popup": obj.get("show_advanced_section_popup"),
            "hide_popup": obj.get("hide_popup"),
            "hide_popup_date": obj.get("hide_popup_date"),
            "is_advanced_section_unlocked": obj.get("is_advanced_section_unlocked"),
            "usage_score": obj.get("usage_score"),
            "features": [FeatureAnalytics.from_dict(_item) for _item in obj["features"]] if obj.get("features") is not None else None,
            "is_closed_content_reuse_info": obj.get("is_closed_content_reuse_info")
        })
        return _obj


