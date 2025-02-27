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

from d361api.d361api.article_simple_data_customer import ArticleSimpleDataCustomer

class TestArticleSimpleDataCustomer(unittest.TestCase):
    """ArticleSimpleDataCustomer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ArticleSimpleDataCustomer:
        """Test ArticleSimpleDataCustomer
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ArticleSimpleDataCustomer`
        """
        model = ArticleSimpleDataCustomer()
        if include_optional:
            return ArticleSimpleDataCustomer(
                id = '',
                title = '',
                public_version = 56,
                latest_version = 56,
                language_code = '',
                hidden = True,
                status = 0,
                order = 56,
                slug = '',
                content_type = 0,
                translation_option = 0,
                is_shared_article = True,
                modified_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return ArticleSimpleDataCustomer(
        )
        """

    def testArticleSimpleDataCustomer(self):
        """Test ArticleSimpleDataCustomer"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
