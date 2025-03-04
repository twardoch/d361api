"""
    Document360 Customer API

    Document360 RESTful APIs will allow you to integrate your documentation with your software, allowing you to easily onboard new users, manage your articles and more.   You can find detailed API documentation here : [API Documentation](https://apidocs.document360.io/docs)

    The version of the OpenAPI document: 2.0
    Contact: support@document360.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest

from d361api.d361api.feature_explorer_status import FeatureExplorerStatus


class TestFeatureExplorerStatus(unittest.TestCase):
    """FeatureExplorerStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FeatureExplorerStatus:
        """Test FeatureExplorerStatus
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FeatureExplorerStatus`
        """
        model = FeatureExplorerStatus()
        if include_optional:
            return FeatureExplorerStatus(
                feature_usage_score = 1.337,
                section = 0,
                feature_id = '',
                feature_name = 0,
                advanced_feature_user_role = 0,
                feature_explorer_user_analytics = d361api.models.feature_explorer_user_analytics_entity.FeatureExplorerUserAnalyticsEntity(
                    id = '', 
                    project_id = '', 
                    user_id = '', 
                    trophy_status = null, 
                    show_default = True, 
                    show_advanced_section_popup = True, 
                    hide_popup = True, 
                    hide_popup_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    is_advanced_section_unlocked = True, 
                    usage_score = 1.337, 
                    features = [
                        d361api.models.feature_analytics.FeatureAnalytics(
                            section = null, 
                            feature_name = null, 
                            is_feature_explored = True, 
                            time_stamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                        ], 
                    is_closed_content_reuse_info = True, )
            )
        else:
            return FeatureExplorerStatus(
        )
        """

    def testFeatureExplorerStatus(self):
        """Test FeatureExplorerStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
