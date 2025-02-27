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

from d361api.d361api.project_version_customer import ProjectVersionCustomer

class TestProjectVersionCustomer(unittest.TestCase):
    """ProjectVersionCustomer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProjectVersionCustomer:
        """Test ProjectVersionCustomer
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProjectVersionCustomer`
        """
        model = ProjectVersionCustomer()
        if include_optional:
            return ProjectVersionCustomer(
                id = '',
                version_number = 1.337,
                base_version_number = 1.337,
                version_code_name = '',
                is_main_version = True,
                is_beta = True,
                is_public = True,
                is_deprecated = True,
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                modified_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                language_versions = [
                    d361api.models.language.Language(
                        id = '', 
                        name = '', 
                        code = '', 
                        set_as_default = True, 
                        hidden = True, 
                        enable_rtl = True, 
                        site_protection_level = null, 
                        is_inheritance_disabled = True, 
                        has_inheritance_disabled_categories_or_articles = True, 
                        country_flag_code = '', 
                        display_name = '', 
                        is_home_page_enabled = True, 
                        version_display_name = '', )
                    ],
                slug = '',
                order = 56,
                version_type = 0
            )
        else:
            return ProjectVersionCustomer(
        )
        """

    def testProjectVersionCustomer(self):
        """Test ProjectVersionCustomer"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
