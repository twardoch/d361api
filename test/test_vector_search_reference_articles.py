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

from d361api.d361api.vector_search_reference_articles import VectorSearchReferenceArticles

class TestVectorSearchReferenceArticles(unittest.TestCase):
    """VectorSearchReferenceArticles unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VectorSearchReferenceArticles:
        """Test VectorSearchReferenceArticles
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VectorSearchReferenceArticles`
        """
        model = VectorSearchReferenceArticles()
        if include_optional:
            return VectorSearchReferenceArticles(
                id = '',
                citation_id = '',
                category_id = '',
                category_title = '',
                category_slug = '',
                version_name = '',
                version_slug = '',
                article_id = '',
                article_title = '',
                article_slug = '',
                version_display_name = '',
                language_code = '',
                data_source_type = 0,
                external_source_link = '',
                external_source_name = '',
                external_source_id = ''
            )
        else:
            return VectorSearchReferenceArticles(
        )
        """

    def testVectorSearchReferenceArticles(self):
        """Test VectorSearchReferenceArticles"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
