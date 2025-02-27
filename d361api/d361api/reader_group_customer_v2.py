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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from d361api.models.access_scope_customer_v2 import AccessScopeCustomerV2
from typing import Optional, Set
from typing_extensions import Self

class ReaderGroupCustomerV2(BaseModel):
    """
    ReaderGroupCustomerV2
    """ # noqa: E501
    reader_group_id: Optional[StrictStr] = Field(default=None, description="The ID of the reader group.")
    title: Optional[StrictStr] = Field(default=None, description="The name of the reader group.")
    description: Optional[StrictStr] = Field(default=None, description="Description of the reader group.")
    associated_readers: Optional[List[StrictStr]] = Field(default=None, description="List of reader IDs to be associated with this reader group.")
    associated_invited_sso_users: Optional[List[StrictStr]] = Field(default=None, description="List of reader invitation IDs. Applicable only for SSO readers.")
    access_scope: Optional[AccessScopeCustomerV2] = Field(default=None, description="Access scope of this reader group.")
    __properties: ClassVar[List[str]] = ["reader_group_id", "title", "description", "associated_readers", "associated_invited_sso_users", "access_scope"]

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
        """Create an instance of ReaderGroupCustomerV2 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of access_scope
        if self.access_scope:
            _dict['access_scope'] = self.access_scope.to_dict()
        # set to None if reader_group_id (nullable) is None
        # and model_fields_set contains the field
        if self.reader_group_id is None and "reader_group_id" in self.model_fields_set:
            _dict['reader_group_id'] = None

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if associated_readers (nullable) is None
        # and model_fields_set contains the field
        if self.associated_readers is None and "associated_readers" in self.model_fields_set:
            _dict['associated_readers'] = None

        # set to None if associated_invited_sso_users (nullable) is None
        # and model_fields_set contains the field
        if self.associated_invited_sso_users is None and "associated_invited_sso_users" in self.model_fields_set:
            _dict['associated_invited_sso_users'] = None

        # set to None if access_scope (nullable) is None
        # and model_fields_set contains the field
        if self.access_scope is None and "access_scope" in self.model_fields_set:
            _dict['access_scope'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ReaderGroupCustomerV2 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "reader_group_id": obj.get("reader_group_id"),
            "title": obj.get("title"),
            "description": obj.get("description"),
            "associated_readers": obj.get("associated_readers"),
            "associated_invited_sso_users": obj.get("associated_invited_sso_users"),
            "access_scope": AccessScopeCustomerV2.from_dict(obj["access_scope"]) if obj.get("access_scope") is not None else None
        })
        return _obj


