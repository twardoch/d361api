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
from enum import Enum
from typing import Self


class SectionTypeEnum(int, Enum):
    """
    SectionTypeEnum
    """

    """
    allowed enum values
    """
    NUMBER_0 = 0
    NUMBER_1 = 1
    NUMBER_2 = 2
    NUMBER_3 = 3
    NUMBER_4 = 4
    NUMBER_5 = 5

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of SectionTypeEnum from a JSON string"""
        return cls(json.loads(json_str))


