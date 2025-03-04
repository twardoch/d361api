"""
    Document360 Customer API

    Document360 RESTful APIs will allow you to integrate your documentation with your software, allowing you to easily onboard new users, manage your articles and more.   You can find detailed API documentation here : [API Documentation](https://apidocs.document360.io/docs)

    The version of the OpenAPI document: 2.0
    Contact: support@document360.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest

from d361api.d361api.get_media_folder_with_id_customer import \
    GetMediaFolderWithIdCustomer


class TestGetMediaFolderWithIdCustomer(unittest.TestCase):
    """GetMediaFolderWithIdCustomer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetMediaFolderWithIdCustomer:
        """Test GetMediaFolderWithIdCustomer
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetMediaFolderWithIdCustomer`
        """
        model = GetMediaFolderWithIdCustomer()
        if include_optional:
            return GetMediaFolderWithIdCustomer(
                data = d361api.models.media_folder_view_meta_data_customer.MediaFolderViewMetaDataCustomer(
                    id = '', 
                    title = '', 
                    order = 56, 
                    parent_folder_id = '', 
                    files = [
                        d361api.models.media_files_meta_data_customer.MediaFilesMetaDataCustomer(
                            id = '0', 
                            file_name = '', 
                            file_type = '', 
                            file_url = '', 
                            updated_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            updated_by = '', 
                            size = '', 
                            tags = [
                                d361api.models.tags_meta_data_customer.TagsMetaDataCustomer(
                                    id = '', 
                                    tag_name = '', )
                                ], 
                            is_starred = True, )
                        ], 
                    icon = '', 
                    items_count = 56, 
                    updated_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_by = '', 
                    is_starred = True, 
                    folder_color = '', 
                    files_count = 56, 
                    sub_folders = [
                        d361api.models.media_folders_data_customer.MediaFoldersDataCustomer(
                            id = '', 
                            title = '', 
                            parent_folder_id = '', 
                            items_count = 56, 
                            updated_by = '', 
                            updated_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            order = 56, 
                            is_starred = True, )
                        ], ),
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
            return GetMediaFolderWithIdCustomer(
        )
        """

    def testGetMediaFolderWithIdCustomer(self):
        """Test GetMediaFolderWithIdCustomer"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
