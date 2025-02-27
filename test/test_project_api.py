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

from d361api.project_api import ProjectApi


class TestProjectApi(unittest.IsolatedAsyncioTestCase):
    """ProjectApi unit test stubs"""

    async def asyncSetUp(self) -> None:
        self.api = ProjectApi()

    async def asyncTearDown(self) -> None:
        await self.api.api_client.close()

    async def test_v2_project_export_export_id_get(self) -> None:
        """Test case for v2_project_export_export_id_get

        Get the status of export
        """
        pass

    async def test_v2_project_export_post(self) -> None:
        """Test case for v2_project_export_post

        Start a new export
        """
        pass

    async def test_v2_project_import_import_id_get(self) -> None:
        """Test case for v2_project_import_import_id_get

        Get the status of import
        """
        pass

    async def test_v2_project_import_post(self) -> None:
        """Test case for v2_project_import_post

        Import documentation
        """
        pass

    async def test_v2_project_schemes_get(self) -> None:
        """Test case for v2_project_schemes_get

        Get all the schemes for the project
        """
        pass


if __name__ == '__main__':
    unittest.main()
