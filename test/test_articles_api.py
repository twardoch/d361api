"""
    Document360 Customer API

    Document360 RESTful APIs will allow you to integrate your documentation with your software, allowing you to easily onboard new users, manage your articles and more.   You can find detailed API documentation here : [API Documentation](https://apidocs.document360.io/docs)

    The version of the OpenAPI document: 2.0
    Contact: support@document360.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest

from d361api.articles_api import ArticlesApi


class TestArticlesApi(unittest.IsolatedAsyncioTestCase):
    """ArticlesApi unit test stubs"""

    async def asyncSetUp(self) -> None:
        self.api = ArticlesApi()

    async def asyncTearDown(self) -> None:
        await self.api.api_client.close()

    async def test_v2_articles_article_id_delete(self) -> None:
        """Test case for v2_articles_article_id_delete

        Deletes an article with an ID
        """
        pass

    async def test_v2_articles_article_id_fork_put(self) -> None:
        """Test case for v2_articles_article_id_fork_put

        Forks an article with an id
        """
        pass

    async def test_v2_articles_article_id_lang_code_get(self) -> None:
        """Test case for v2_articles_article_id_lang_code_get

        Gets an article
        """
        pass

    async def test_v2_articles_article_id_lang_code_publish_post(self) -> None:
        """Test case for v2_articles_article_id_lang_code_publish_post

        Publishes an article with an id
        """
        pass

    async def test_v2_articles_article_id_lang_code_put(self) -> None:
        """Test case for v2_articles_article_id_lang_code_put

        Updates an article with the ID
        """
        pass

    async def test_v2_articles_article_id_lang_code_settings_get(self) -> None:
        """Test case for v2_articles_article_id_lang_code_settings_get

        Gets settings for the article
        """
        pass

    async def test_v2_articles_article_id_lang_code_settings_put(self) -> None:
        """Test case for v2_articles_article_id_lang_code_settings_put

        Updates settings for the article
        """
        pass

    async def test_v2_articles_article_id_lang_code_update_description_put(self) -> None:
        """Test case for v2_articles_article_id_lang_code_update_description_put

        Update the Article Description
        """
        pass

    async def test_v2_articles_article_id_lang_code_version_version_number_delete(self) -> None:
        """Test case for v2_articles_article_id_lang_code_version_version_number_delete

        Deletes an article version
        """
        pass

    async def test_v2_articles_article_id_lang_code_versions_get(self) -> None:
        """Test case for v2_articles_article_id_lang_code_versions_get

        Gets all article versions
        """
        pass

    async def test_v2_articles_article_id_lang_code_versions_version_number_get(self) -> None:
        """Test case for v2_articles_article_id_lang_code_versions_version_number_get

        Gets article by a version number
        """
        pass

    async def test_v2_articles_article_id_publish_post(self) -> None:
        """Test case for v2_articles_article_id_publish_post

        Publishes an article with an id
        """
        pass

    async def test_v2_articles_article_id_settings_get(self) -> None:
        """Test case for v2_articles_article_id_settings_get

        Gets settings for the article
        """
        pass

    async def test_v2_articles_article_id_settings_put(self) -> None:
        """Test case for v2_articles_article_id_settings_put

        Updates settings for the article
        """
        pass

    async def test_v2_articles_article_id_update_description_put(self) -> None:
        """Test case for v2_articles_article_id_update_description_put

        Update the Article Description
        """
        pass

    async def test_v2_articles_article_id_version_version_number_delete(self) -> None:
        """Test case for v2_articles_article_id_version_version_number_delete

        Deletes an article version
        """
        pass

    async def test_v2_articles_article_id_versions_get(self) -> None:
        """Test case for v2_articles_article_id_versions_get

        Gets all article versions
        """
        pass

    async def test_v2_articles_article_id_versions_version_number_get(self) -> None:
        """Test case for v2_articles_article_id_versions_version_number_get

        Gets article by a version number
        """
        pass

    async def test_v2_articles_bulkcreate_post(self) -> None:
        """Test case for v2_articles_bulkcreate_post

        Adds multiple articles
        """
        pass

    async def test_v2_articles_bulkdelete_article_versions_delete(self) -> None:
        """Test case for v2_articles_bulkdelete_article_versions_delete

        Delete multiple article versions
        """
        pass

    async def test_v2_articles_bulkdelete_delete(self) -> None:
        """Test case for v2_articles_bulkdelete_delete

        Deletes multiple articles
        """
        pass

    async def test_v2_articles_bulkpublish_lang_code_post(self) -> None:
        """Test case for v2_articles_bulkpublish_lang_code_post

        Publishes multiple articles
        """
        pass

    async def test_v2_articles_bulkupdate_put(self) -> None:
        """Test case for v2_articles_bulkupdate_put

        Updates multiple articles
        """
        pass

    async def test_v2_articles_post(self) -> None:
        """Test case for v2_articles_post

        Adds an article to an existing category
        """
        pass


if __name__ == '__main__':
    unittest.main()
