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


class FeatureListEnum(int, Enum):
    """
    FeatureListEnum
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
    NUMBER_6 = 6
    NUMBER_7 = 7
    NUMBER_8 = 8
    NUMBER_9 = 9
    NUMBER_10 = 10
    NUMBER_11 = 11
    NUMBER_12 = 12
    NUMBER_13 = 13
    NUMBER_14 = 14
    NUMBER_15 = 15
    NUMBER_16 = 16
    NUMBER_17 = 17
    NUMBER_18 = 18
    NUMBER_19 = 19
    NUMBER_20 = 20
    NUMBER_21 = 21
    NUMBER_22 = 22
    NUMBER_23 = 23
    NUMBER_24 = 24
    NUMBER_25 = 25
    NUMBER_26 = 26

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of FeatureListEnum from a JSON string"""
        return cls(json.loads(json_str))


