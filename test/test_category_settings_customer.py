"""
    Document360 Customer API

    Document360 RESTful APIs will allow you to integrate your documentation with your software, allowing you to easily onboard new users, manage your articles and more.   You can find detailed API documentation here : [API Documentation](https://apidocs.document360.io/docs)

    The version of the OpenAPI document: 2.0
    Contact: support@document360.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest

from d361api.d361api.category_settings_customer import CategorySettingsCustomer


class TestCategorySettingsCustomer(unittest.TestCase):
    """CategorySettingsCustomer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CategorySettingsCustomer:
        """Test CategorySettingsCustomer
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CategorySettingsCustomer`
        """
        model = CategorySettingsCustomer()
        if include_optional:
            return CategorySettingsCustomer(
                slug = '',
                seo_title = '',
                description = '',
                allow_comments = True,
                show_table_of_contents = True,
                featured_image_url = '',
                tags = [
                    ''
                    ],
                status_indicator = 0,
                status_indicator_expiry_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                exclude_from_search = True,
                exclude_from_ai_search = True,
                related_articles = [
                    d361api.models.related_article_data.RelatedArticleData(
                        id = '', 
                        title = '', 
                        hidden = True, 
                        slug = '', )
                    ],
                content_type = 0,
                is_acknowledgement_enabled = True
            )
        else:
            return CategorySettingsCustomer(
        )
        """

    def testCategorySettingsCustomer(self):
        """Test CategorySettingsCustomer"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
