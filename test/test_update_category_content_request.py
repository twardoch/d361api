"""
    Document360 Customer API

    Document360 RESTful APIs will allow you to integrate your documentation with your software, allowing you to easily onboard new users, manage your articles and more.   You can find detailed API documentation here : [API Documentation](https://apidocs.document360.io/docs)

    The version of the OpenAPI document: 2.0
    Contact: support@document360.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest

from d361api.d361api.update_category_content_request import \
    UpdateCategoryContentRequest


class TestUpdateCategoryContentRequest(unittest.TestCase):
    """UpdateCategoryContentRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateCategoryContentRequest:
        """Test UpdateCategoryContentRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateCategoryContentRequest`
        """
        model = UpdateCategoryContentRequest()
        if include_optional:
            return UpdateCategoryContentRequest(
                category_id = '',
                lang_code = '',
                title = '',
                content = '',
                html_content = '',
                block_content = '',
                version_number = 56,
                translation_option = '',
                source = '',
                updated_by = ''
            )
        else:
            return UpdateCategoryContentRequest(
        )
        """

    def testUpdateCategoryContentRequest(self):
        """Test UpdateCategoryContentRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
