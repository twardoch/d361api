# coding: utf-8

"""
    Document360 Customer API

    Document360 RESTful APIs will allow you to integrate your documentation with your software, allowing you to easily onboard new users, manage your articles and more.   You can find detailed API documentation here : [API Documentation](https://apidocs.document360.io/docs)

    The version of the OpenAPI document: 2.0
    Contact: support@document360.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from d361api.d361api.access_scope_customer_v2 import AccessScopeCustomerV2

class TestAccessScopeCustomerV2(unittest.TestCase):
    """AccessScopeCustomerV2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AccessScopeCustomerV2:
        """Test AccessScopeCustomerV2
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AccessScopeCustomerV2`
        """
        model = AccessScopeCustomerV2()
        if include_optional:
            return AccessScopeCustomerV2(
                access_level = 0,
                categories = [
                    d361api.models.category_summary_customer_v2.CategorySummaryCustomerV2(
                        category_id = '', 
                        project_version_id = '', 
                        language_code = '', )
                    ],
                project_versions = [
                    ''
                    ],
                languages = [
                    d361api.models.language_summary_customer.LanguageSummaryCustomer(
                        project_version_id = '', 
                        language_code = '', )
                    ]
            )
        else:
            return AccessScopeCustomerV2(
        )
        """

    def testAccessScopeCustomerV2(self):
        """Test AccessScopeCustomerV2"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
