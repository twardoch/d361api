"""
    Document360 Customer API

    Document360 RESTful APIs will allow you to integrate your documentation with your software, allowing you to easily onboard new users, manage your articles and more.   You can find detailed API documentation here : [API Documentation](https://apidocs.document360.io/docs)

    The version of the OpenAPI document: 2.0
    Contact: support@document360.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest

from d361api.d361api.sso_scheme_reponse import SSOSchemeReponse


class TestSSOSchemeReponse(unittest.TestCase):
    """SSOSchemeReponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SSOSchemeReponse:
        """Test SSOSchemeReponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SSOSchemeReponse`
        """
        model = SSOSchemeReponse()
        if include_optional:
            return SSOSchemeReponse(
                schemes = [
                    d361api.models.sso_scheme_details.SSOSchemeDetails(
                        id = '', 
                        sso_name = '', 
                        project_id = '', 
                        scheme_name = '', 
                        display_name = '', )
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
            return SSOSchemeReponse(
        )
        """

    def testSSOSchemeReponse(self):
        """Test SSOSchemeReponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
