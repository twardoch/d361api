"""
    Document360 Customer API

    Document360 RESTful APIs will allow you to integrate your documentation with your software, allowing you to easily onboard new users, manage your articles and more.   You can find detailed API documentation here : [API Documentation](https://apidocs.document360.io/docs)

    The version of the OpenAPI document: 2.0
    Contact: support@document360.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest

from d361api.d361api.add_user_data_customer_api_response import \
    AddUserDataCustomerApiResponse


class TestAddUserDataCustomerApiResponse(unittest.TestCase):
    """AddUserDataCustomerApiResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AddUserDataCustomerApiResponse:
        """Test AddUserDataCustomerApiResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AddUserDataCustomerApiResponse`
        """
        model = AddUserDataCustomerApiResponse()
        if include_optional:
            return AddUserDataCustomerApiResponse(
                result = d361api.models.add_user_data.AddUserData(
                    id = '', ),
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
            return AddUserDataCustomerApiResponse(
        )
        """

    def testAddUserDataCustomerApiResponse(self):
        """Test AddUserDataCustomerApiResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
