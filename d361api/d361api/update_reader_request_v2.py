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

from d361api.models.add_update_access_scope_customer_v2 import \
    AddUpdateAccessScopeCustomerV2
from d361api.models.sso_user_types import SSOUserTypes
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr


class UpdateReaderRequestV2(BaseModel):
    """
    UpdateReaderRequestV2
    """
    first_name: StrictStr | None = Field(default=None, description="The first name of the reader")
    last_name: StrictStr | None = Field(default=None, description="The last name of the reader")
    associated_reader_groups: list[StrictStr] = Field(description="List of reader group IDs. If the value is null or not given, then the reader would be removed from all associated reader groups.")
    access_scope: AddUpdateAccessScopeCustomerV2 = Field(description="Access level of the reader. 0-None, 1-Category, 2-Version, 3-Project, 4-Language.")
    is_invitation_id: StrictBool | None = Field(default=None, description="Applicable only for Single Sign-On readers. Set this property to true, if the reader is a Single Sign-On reader who hasn't logged in to the application yet.")
    sso_user_type: SSOUserTypes | None = Field(default=None, description="SSO user type 0 - Normal user, 1 - SSO user, 2 - Invited SSO user")
    __properties: ClassVar[list[str]] = ["first_name", "last_name", "associated_reader_groups", "access_scope", "is_invitation_id", "sso_user_type"]

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
        """Create an instance of UpdateReaderRequestV2 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of access_scope
        if self.access_scope:
            _dict['access_scope'] = self.access_scope.to_dict()
        # set to None if first_name (nullable) is None
        # and model_fields_set contains the field
        if self.first_name is None and "first_name" in self.model_fields_set:
            _dict['first_name'] = None

        # set to None if last_name (nullable) is None
        # and model_fields_set contains the field
        if self.last_name is None and "last_name" in self.model_fields_set:
            _dict['last_name'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict[str, Any] | None) -> Self | None:
        """Create an instance of UpdateReaderRequestV2 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "first_name": obj.get("first_name"),
            "last_name": obj.get("last_name"),
            "associated_reader_groups": obj.get("associated_reader_groups"),
            "access_scope": AddUpdateAccessScopeCustomerV2.from_dict(obj["access_scope"]) if obj.get("access_scope") is not None else None,
            "is_invitation_id": obj.get("is_invitation_id"),
            "sso_user_type": obj.get("sso_user_type")
        })
        return _obj


