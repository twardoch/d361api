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

from d361api.models.feature_explorer_user_analytics_entity import \
    FeatureExplorerUserAnalyticsEntity
from d361api.models.feature_explorer_user_role_enum import \
    FeatureExplorerUserRoleEnum
from d361api.models.feature_list_enum import FeatureListEnum
from d361api.models.section_type_enum import SectionTypeEnum
from pydantic import BaseModel, ConfigDict, StrictFloat, StrictInt, StrictStr


class FeatureExplorerStatus(BaseModel):
    """
    FeatureExplorerStatus
    """
    feature_usage_score: StrictFloat | StrictInt | None = None
    section: SectionTypeEnum | None = None
    feature_id: StrictStr | None = None
    feature_name: FeatureListEnum | None = None
    advanced_feature_user_role: FeatureExplorerUserRoleEnum | None = None
    feature_explorer_user_analytics: FeatureExplorerUserAnalyticsEntity | None = None
    __properties: ClassVar[List[str]] = ["feature_usage_score", "section", "feature_id", "feature_name", "advanced_feature_user_role", "feature_explorer_user_analytics"]

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
        """Create an instance of FeatureExplorerStatus from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of feature_explorer_user_analytics
        if self.feature_explorer_user_analytics:
            _dict['feature_explorer_user_analytics'] = self.feature_explorer_user_analytics.to_dict()
        # set to None if feature_id (nullable) is None
        # and model_fields_set contains the field
        if self.feature_id is None and "feature_id" in self.model_fields_set:
            _dict['feature_id'] = None

        # set to None if feature_explorer_user_analytics (nullable) is None
        # and model_fields_set contains the field
        if self.feature_explorer_user_analytics is None and "feature_explorer_user_analytics" in self.model_fields_set:
            _dict['feature_explorer_user_analytics'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict[str, Any] | None) -> Self | None:
        """Create an instance of FeatureExplorerStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "feature_usage_score": obj.get("feature_usage_score"),
            "section": obj.get("section"),
            "feature_id": obj.get("feature_id"),
            "feature_name": obj.get("feature_name"),
            "advanced_feature_user_role": obj.get("advanced_feature_user_role"),
            "feature_explorer_user_analytics": FeatureExplorerUserAnalyticsEntity.from_dict(obj["feature_explorer_user_analytics"]) if obj.get("feature_explorer_user_analytics") is not None else None
        })
        return _obj


