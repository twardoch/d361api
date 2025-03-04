"""
    Document360 Customer API

    Document360 RESTful APIs will allow you to integrate your documentation with your software, allowing you to easily onboard new users, manage your articles and more.   You can find detailed API documentation here : [API Documentation](https://apidocs.document360.io/docs)

    The version of the OpenAPI document: 2.0
    Contact: support@document360.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest

from d361api.d361api.all_files_with_count_response_customer import \
    AllFilesWithCountResponseCustomer


class TestAllFilesWithCountResponseCustomer(unittest.TestCase):
    """AllFilesWithCountResponseCustomer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AllFilesWithCountResponseCustomer:
        """Test AllFilesWithCountResponseCustomer
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AllFilesWithCountResponseCustomer`
        """
        model = AllFilesWithCountResponseCustomer()
        if include_optional:
            return AllFilesWithCountResponseCustomer(
                data = d361api.models.all_files_with_count_customer.AllFilesWithCountCustomer(
                    all_files = [
                        d361api.models.deletedand_starred_meta_data_customer.DeletedandStarredMetaDataCustomer(
                            id = '', 
                            file_name = '', 
                            file_type = '', 
                            file_url = '', 
                            updated_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            updated_by = '', 
                            size = '', 
                            height = '', 
                            width = '', 
                            title = '', 
                            alternative_text = '', 
                            is_starred = True, 
                            parent_folder_id = '', 
                            tag_ids = [
                                ''
                                ], )
                        ], 
                    count = 56, ),
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
            return AllFilesWithCountResponseCustomer(
        )
        """

    def testAllFilesWithCountResponseCustomer(self):
        """Test AllFilesWithCountResponseCustomer"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
