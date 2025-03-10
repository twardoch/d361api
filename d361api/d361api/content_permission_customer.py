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
from typing import Annotated, Any, ClassVar, Self

from d361api.models.add_update_access_scope_customer_v2 import \
    AddUpdateAccessScopeCustomerV2
from pydantic import BaseModel, ConfigDict, Field


class ContentPermissionCustomer(BaseModel):
    """
    The content permission of the team account
    """
    associated_content_role_id: Annotated[str, Field(min_length=1, strict=True)] = Field(description="The content role id of the team account.Please refer GET **/Teams/roles** endpoint to get the list of content roles.")
    access_scope: AddUpdateAccessScopeCustomerV2 = Field(description="The access level of the team account. With the access level, you will be able to set the permissions at a granular level. For example, you can limit the user to view articles only for a particular language/category/version.")
    __properties: ClassVar[List[str]] = ["associated_content_role_id", "access_scope"]

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
        """Create an instance of ContentPermissionCustomer from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: dict[str, Any] | None) -> Self | None:
        """Create an instance of ContentPermissionCustomer from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "associated_content_role_id": obj.get("associated_content_role_id"),
            "access_scope": AddUpdateAccessScopeCustomerV2.from_dict(obj["access_scope"]) if obj.get("access_scope") is not None else None
        })
        return _obj


