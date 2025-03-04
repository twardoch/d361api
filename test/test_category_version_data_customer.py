"""
    Document360 Customer API

    Document360 RESTful APIs will allow you to integrate your documentation with your software, allowing you to easily onboard new users, manage your articles and more.   You can find detailed API documentation here : [API Documentation](https://apidocs.document360.io/docs)

    The version of the OpenAPI document: 2.0
    Contact: support@document360.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest

from d361api.d361api.category_version_data_customer import \
    CategoryVersionDataCustomer


class TestCategoryVersionDataCustomer(unittest.TestCase):
    """CategoryVersionDataCustomer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CategoryVersionDataCustomer:
        """Test CategoryVersionDataCustomer
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CategoryVersionDataCustomer`
        """
        model = CategoryVersionDataCustomer()
        if include_optional:
            return CategoryVersionDataCustomer(
                id = '',
                title = '',
                content = '',
                html_content = '',
                block_content = '',
                category_id = '',
                project_version_id = '',
                version_number = 56,
                public_version = 56,
                latest_version = 56,
                enable_rtl = True,
                hidden = True,
                status = 0,
                order = 56,
                created_by = '',
                authors = [
                    d361api.models.user_profile_customer.UserProfileCustomer(
                        id = '', 
                        first_name = '', 
                        last_name = '', 
                        email_id = '', 
                        profile_logo_url = '', 
                        user_role = null, 
                        last_login_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        unique_user_name = '', 
                        sso_user_type = null, 
                        is_sso_user = True, )
                    ],
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                modified_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                slug = '',
                is_fall_back_content = True
            )
        else:
            return CategoryVersionDataCustomer(
        )
        """

    def testCategoryVersionDataCustomer(self):
        """Test CategoryVersionDataCustomer"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
