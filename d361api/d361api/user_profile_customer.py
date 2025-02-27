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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, Optional
from d361api.models.sso_user_types import SSOUserTypes
from d361api.models.user_access import UserAccess
from typing import Optional, Set
from typing_extensions import Self

class UserProfileCustomer(BaseModel):
    """
    UserProfileCustomer
    """ # noqa: E501
    id: Optional[StrictStr] = None
    first_name: Optional[StrictStr] = None
    last_name: Optional[StrictStr] = None
    email_id: Optional[StrictStr] = None
    profile_logo_url: Optional[StrictStr] = None
    user_role: Optional[UserAccess] = None
    last_login_at: Optional[datetime] = None
    unique_user_name: Optional[StrictStr] = None
    sso_user_type: Optional[SSOUserTypes] = Field(default=None, description="SSO user type 0 - Normal user, 1 - SSO user, 2 - Invited SSO user")
    is_sso_user: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["id", "first_name", "last_name", "email_id", "profile_logo_url", "user_role", "last_login_at", "unique_user_name", "sso_user_type", "is_sso_user"]

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
        """Create an instance of UserProfileCustomer from a JSON string"""
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
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if first_name (nullable) is None
        # and model_fields_set contains the field
        if self.first_name is None and "first_name" in self.model_fields_set:
            _dict['first_name'] = None

        # set to None if last_name (nullable) is None
        # and model_fields_set contains the field
        if self.last_name is None and "last_name" in self.model_fields_set:
            _dict['last_name'] = None

        # set to None if email_id (nullable) is None
        # and model_fields_set contains the field
        if self.email_id is None and "email_id" in self.model_fields_set:
            _dict['email_id'] = None

        # set to None if profile_logo_url (nullable) is None
        # and model_fields_set contains the field
        if self.profile_logo_url is None and "profile_logo_url" in self.model_fields_set:
            _dict['profile_logo_url'] = None

        # set to None if last_login_at (nullable) is None
        # and model_fields_set contains the field
        if self.last_login_at is None and "last_login_at" in self.model_fields_set:
            _dict['last_login_at'] = None

        # set to None if unique_user_name (nullable) is None
        # and model_fields_set contains the field
        if self.unique_user_name is None and "unique_user_name" in self.model_fields_set:
            _dict['unique_user_name'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UserProfileCustomer from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "first_name": obj.get("first_name"),
            "last_name": obj.get("last_name"),
            "email_id": obj.get("email_id"),
            "profile_logo_url": obj.get("profile_logo_url"),
            "user_role": obj.get("user_role"),
            "last_login_at": obj.get("last_login_at"),
            "unique_user_name": obj.get("unique_user_name"),
            "sso_user_type": obj.get("sso_user_type"),
            "is_sso_user": obj.get("is_sso_user")
        })
        return _obj


