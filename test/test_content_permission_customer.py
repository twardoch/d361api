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

from d361api.d361api.content_permission_customer import ContentPermissionCustomer

class TestContentPermissionCustomer(unittest.TestCase):
    """ContentPermissionCustomer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ContentPermissionCustomer:
        """Test ContentPermissionCustomer
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ContentPermissionCustomer`
        """
        model = ContentPermissionCustomer()
        if include_optional:
            return ContentPermissionCustomer(
                associated_content_role_id = '0',
                access_scope = d361api.models.add_update_access_scope_customer_v2.AddUpdateAccessScopeCustomerV2(
                    access_level = null, 
                    categories = [
                        d361api.models.category_scope_customer.CategoryScopeCustomer(
                            project_version_id = '0', 
                            category_id = '0', 
                            language_code = '0', )
                        ], 
                    project_versions = [
                        ''
                        ], 
                    languages = [
                        d361api.models.language_scope_customer.LanguageScopeCustomer(
                            project_version_id = '0', 
                            language_code = '0', )
                        ], )
            )
        else:
            return ContentPermissionCustomer(
                associated_content_role_id = '0',
                access_scope = d361api.models.add_update_access_scope_customer_v2.AddUpdateAccessScopeCustomerV2(
                    access_level = null, 
                    categories = [
                        d361api.models.category_scope_customer.CategoryScopeCustomer(
                            project_version_id = '0', 
                            category_id = '0', 
                            language_code = '0', )
                        ], 
                    project_versions = [
                        ''
                        ], 
                    languages = [
                        d361api.models.language_scope_customer.LanguageScopeCustomer(
                            project_version_id = '0', 
                            language_code = '0', )
                        ], ),
        )
        """

    def testContentPermissionCustomer(self):
        """Test ContentPermissionCustomer"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
