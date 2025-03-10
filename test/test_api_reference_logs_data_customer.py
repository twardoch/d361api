"""
    Document360 Customer API

    Document360 RESTful APIs will allow you to integrate your documentation with your software, allowing you to easily onboard new users, manage your articles and more.   You can find detailed API documentation here : [API Documentation](https://apidocs.document360.io/docs)

    The version of the OpenAPI document: 2.0
    Contact: support@document360.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest

from d361api.d361api.api_reference_logs_data_customer import \
    ApiReferenceLogsDataCustomer


class TestApiReferenceLogsDataCustomer(unittest.TestCase):
    """ApiReferenceLogsDataCustomer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiReferenceLogsDataCustomer:
        """Test ApiReferenceLogsDataCustomer
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiReferenceLogsDataCustomer`
        """
        model = ApiReferenceLogsDataCustomer()
        if include_optional:
            return ApiReferenceLogsDataCustomer(
                logs_id = '',
                user_name = '',
                user_id = '',
                title = '',
                modified_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                error_count = 56,
                alerts_count = 56
            )
        else:
            return ApiReferenceLogsDataCustomer(
        )
        """

    def testApiReferenceLogsDataCustomer(self):
        """Test ApiReferenceLogsDataCustomer"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
