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

from d361api.d361api.get_category_content_response import GetCategoryContentResponse

class TestGetCategoryContentResponse(unittest.TestCase):
    """GetCategoryContentResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetCategoryContentResponse:
        """Test GetCategoryContentResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetCategoryContentResponse`
        """
        model = GetCategoryContentResponse()
        if include_optional:
            return GetCategoryContentResponse(
                category = d361api.models.category_version_data.CategoryVersionData(
                    id = '', 
                    title = '', 
                    content = '', 
                    html_content = '', 
                    block_content = '', 
                    parent_category_id = '', 
                    project_document_version_id = '', 
                    version_number = 56, 
                    public_version = 56, 
                    latest_version = 56, 
                    enable_rtl = True, 
                    hidden = True, 
                    status = null, 
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
                    is_fall_back_content = True, 
                    stale_status = null, 
                    content_type = '', 
                    is_block_editor = True, ),
                extension_data = None,
                success = True,
                errors = [
                    d361api.models.base_error.BaseError(
                        extension_data = null, 
                        stack_trace = '', 
                        description = '', 
                        error_code = '', 
                        custom_data = {
                            'key' : null
                            }, )
                    ],
                warnings = [
                    d361api.models.base_warning.BaseWarning(
                        extension_data = null, 
                        description = '', 
                        warning_code = '', )
                    ],
                information = [
                    d361api.models.base_information.BaseInformation(
                        extension_data = null, 
                        description = '', )
                    ]
            )
        else:
            return GetCategoryContentResponse(
        )
        """

    def testGetCategoryContentResponse(self):
        """Test GetCategoryContentResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
