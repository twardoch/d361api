"""
    Document360 Customer API

    Document360 RESTful APIs will allow you to integrate your documentation with your software, allowing you to easily onboard new users, manage your articles and more.   You can find detailed API documentation here : [API Documentation](https://apidocs.document360.io/docs)

    The version of the OpenAPI document: 2.0
    Contact: support@document360.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest

from d361api.d361api.get_logs_details_response_customer import \
    GetLogsDetailsResponseCustomer


class TestGetLogsDetailsResponseCustomer(unittest.TestCase):
    """GetLogsDetailsResponseCustomer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetLogsDetailsResponseCustomer:
        """Test GetLogsDetailsResponseCustomer
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetLogsDetailsResponseCustomer`
        """
        model = GetLogsDetailsResponseCustomer()
        if include_optional:
            return GetLogsDetailsResponseCustomer(
                api_reference_errors = [
                    d361api.models.api_logs.ApiLogs(
                        message = '', 
                        pointer = '', )
                    ],
                api_reference_alerts = [
                    d361api.models.api_logs.ApiLogs(
                        message = '', 
                        pointer = '', )
                    ],
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
            return GetLogsDetailsResponseCustomer(
        )
        """

    def testGetLogsDetailsResponseCustomer(self):
        """Test GetLogsDetailsResponseCustomer"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
