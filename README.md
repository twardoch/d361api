# D361API: Auto-Generated Document360 API Client

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://badge.fury.io/py/d361api.svg)](https://badge.fury.io/py/d361api)
[![Python Versions](https://img.shields.io/pypi/pyversions/d361api.svg)](https://pypi.org/project/d361api/)
[![API Version](https://img.shields.io/badge/API-v2.0-blue.svg)](https://apidocs.document360.io/docs)

## 🚀 **TL;DR**

D361API is the **auto-generated Python client** for Document360's REST API, providing complete programmatic access to Document360 knowledge bases. As part of the Document360 unified toolkit, it enables real-time integration, content synchronization, and API-driven documentation workflows.

**Quick Start:**
```bash
# Install the API client
pip install d361api

# Basic usage - get all articles  
import d361api
import asyncio
import os

async def main():
    configuration = d361api.Configuration(host="https://apihub.document360.io")
    configuration.api_key['api_token'] = os.environ["DOCUMENT360_API_TOKEN"]
    
    async with d361api.ApiClient(configuration) as api_client:
        articles_api = d361api.ArticlesApi(api_client)
        project_versions_api = d361api.ProjectVersionsApi(api_client)
        
        # Get project versions
        versions = await project_versions_api.v2_project_versions_get()
        project_version_id = versions.data[0].id
        
        # Get all articles for the project version
        articles = await project_versions_api.v2_project_versions_project_version_id_articles_get(
            project_version_id=project_version_id
        )
        
        print(f"Found {len(articles.data)} articles")
        for article in articles.data[:5]:  # Show first 5
            print(f"- {article.title}")

asyncio.run(main())
```

**Key Features:**
- 🔄 **Complete API Coverage** - All Document360 v2.0 API endpoints
- 🏷️ **Type-Safe Operations** - Pydantic models with full validation  
- ⚡ **Async Support** - Built on aiohttp for high-performance operations
- 🔐 **Authentication Handling** - Seamless API key management
- 🤖 **Auto-Generated** - Always up-to-date with latest API specification
- 🧩 **Integration-Ready** - Designed for use in larger workflows and toolkits

---

## 📦 **What is D361API?**

D361API is the **live API integration component** of the Document360 unified toolkit. Unlike `d361` (which processes offline archives) and `vexy-help` (which converts to MkDocs), D361API provides real-time access to Document360's cloud-hosted content through official REST APIs.

**Core Purpose:**  
D361API enables developers to programmatically interact with Document360 knowledge bases for content management, real-time synchronization, automated publishing workflows, and integration with external systems. It's automatically generated from Document360's OpenAPI specification, ensuring 100% API compatibility and feature coverage.

**The D361API Advantage:**
- **Complete API Coverage** - Access every Document360 feature programmatically
- **Real-time Operations** - Live content updates, publishing, and management  
- **Type Safety** - Full Pydantic validation prevents runtime errors
- **Async Performance** - Handle high-volume operations efficiently
- **Auto-generated** - Always current with Document360's latest API features

## 🎯 **Who Uses D361API?**

**API Integration Developers:**
- **Backend Engineers** - Integrate Document360 into existing applications and services
- **DevOps Teams** - Automate content publishing and synchronization workflows
- **Data Engineers** - Build ETL pipelines for documentation content management
- **Integration Specialists** - Connect Document360 with CRM, support, and workflow systems

**Content Automation:**
- **Technical Writers** - Automate content publishing and version management
- **Documentation Teams** - Build custom editorial workflows and approval processes  
- **Product Teams** - Sync product releases with documentation updates
- **Support Teams** - Integrate knowledge base with ticketing and help desk systems

**Enterprise Applications:**
- **Customer Portals** - Embed live documentation in customer-facing applications
- **Internal Tools** - Build custom documentation management interfaces
- **Compliance Systems** - Automated documentation auditing and reporting
- **Multi-tenant Applications** - Manage documentation across multiple client instances

## 🚀 **Why Choose D361API?**

**🔧 Technical Excellence:**
- **Auto-Generated Reliability** - Generated directly from Document360's OpenAPI spec
- **Type-Safe Operations** - Comprehensive Pydantic models prevent integration errors
- **Async-First Design** - Built for high-performance concurrent operations
- **Complete Feature Parity** - Access every API endpoint and parameter

**🌐 Real-World Integration:**
- **Production-Ready** - Used in enterprise applications and automated workflows
- **Error Handling** - Comprehensive exception handling for robust integration
- **Authentication Management** - Secure API key handling and rotation support
- **Rate Limit Aware** - Designed to work within Document360's API limits

**🔄 Ecosystem Integration:**
- **Toolkit Component** - Seamlessly works with `d361` and `vexy-help` for hybrid workflows
- **Standalone Operation** - Use independently for pure API-driven applications  
- **Framework Agnostic** - Works with FastAPI, Django, Flask, and other Python frameworks
- **CI/CD Friendly** - Perfect for automated documentation deployment pipelines

---

## 📋 **API Documentation Reference**

D361API provides complete access to Document360's REST API v2.0. For detailed API documentation, see the [official Document360 API documentation](https://apidocs.document360.io/docs).

**Core API Categories:**
- **Articles** - Create, read, update, delete, and publish documentation articles
- **Categories** - Manage documentation structure and organization  
- **Project Versions** - Handle multiple documentation versions and languages
- **Teams & Users** - User management and access control
- **API References** - Import and manage API documentation
- **Drive & Media** - File and media asset management
- **Search** - Advanced content search and AI-powered assistance
- **Import/Export** - Bulk content operations and data migration

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project from Document360's official API specification:

- **API version:** 2.0
- **Package version:** 1.0.0  
- **Generator version:** 7.11.0
- **Build package:** `org.openapitools.codegen.languages.PythonClientCodegen`

For support and additional information, visit [Document360 Support](https://document360.io/contact-us/).

## 📋 **Requirements**

- **Python 3.8+** (Python 3.9+ recommended)
- **aiohttp** - For async HTTP operations
- **pydantic** - For data validation and serialization
- **typing-extensions** - For enhanced type hints

## ⚡ **Installation & Usage**

### Quick Installation

**Via pip:**
```bash
pip install d361api
```

**Via uv (recommended for faster installs):**
```bash
uv pip install d361api
```

**From source:**
```bash
uv pip install git+https://github.com/twardoch/d361api
```

### Basic Setup

```python
import d361api
import os
import asyncio

# Configure the client
configuration = d361api.Configuration(
    host="https://apihub.document360.io"
)

# Set API authentication
configuration.api_key['api_token'] = os.environ["DOCUMENT360_API_TOKEN"]

# Optionally set API key prefix (usually not needed)
# configuration.api_key_prefix['api_token'] = 'Bearer'

# Basic usage example
async def main():
    async with d361api.ApiClient(configuration) as api_client:
        # Create API instances
        project_api = d361api.ProjectVersionsApi(api_client)
        articles_api = d361api.ArticlesApi(api_client)
        
        # Get project versions
        project_versions = await project_api.v2_project_versions_get()
        print(f"Available project versions: {len(project_versions.data)}")
        
        # Use first project version
        project_version_id = project_versions.data[0].id
        
        # Get articles for this project version
        articles_response = await project_api.v2_project_versions_project_version_id_articles_get(
            project_version_id=project_version_id,
            page=1,
            results_per_page=10
        )
        
        print(f"Found {len(articles_response.data)} articles")
        for article in articles_response.data:
            print(f"- {article.title} (ID: {article.id})")

asyncio.run(main())
```

## 🔧 **Core Features & Capabilities**

### 📝 **Article Management**
Complete CRUD operations for documentation articles:

```python
import d361api
from d361api.models import CreateArticleRequest, UpdateArticleRequest
import asyncio

async def article_management_example():
    configuration = d361api.Configuration(host="https://apihub.document360.io")
    configuration.api_key['api_token'] = os.environ["DOCUMENT360_API_TOKEN"]
    
    async with d361api.ApiClient(configuration) as api_client:
        articles_api = d361api.ArticlesApi(api_client)
        
        # Create a new article
        new_article = CreateArticleRequest(
            title="Getting Started Guide",
            content="<h1>Welcome to our documentation</h1><p>This guide will help you get started...</p>",
            category_id="12345",  # Replace with your category ID
            article_type="public",  # public, private, or internal
        )
        
        created_article = await articles_api.v2_articles_post(new_article)
        article_id = created_article.data.id
        print(f"Created article: {created_article.data.title} (ID: {article_id})")
        
        # Get article details
        article_details = await articles_api.v2_articles_article_id_lang_code_get(
            article_id=article_id,
            lang_code="en"
        )
        print(f"Article content length: {len(article_details.data.html_content)}")
        
        # Update the article
        update_request = UpdateArticleRequest(
            title="Updated Getting Started Guide",
            content="<h1>Welcome to our updated documentation</h1><p>This updated guide...</p>",
        )
        
        updated_article = await articles_api.v2_articles_article_id_lang_code_put(
            article_id=article_id,
            lang_code="en",
            update_article_request=update_request
        )
        print(f"Updated article: {updated_article.data.title}")
        
        # Publish the article
        from d361api.models import PublishArticleRequest
        publish_request = PublishArticleRequest(
            version_number=1
        )
        
        await articles_api.v2_articles_article_id_lang_code_publish_post(
            article_id=article_id,
            lang_code="en",
            publish_article_request=publish_request
        )
        print(f"Published article {article_id}")

asyncio.run(article_management_example())
```

### 🗂️ **Category Management** 
Organize documentation with hierarchical categories:

```python
async def category_management_example():
    configuration = d361api.Configuration(host="https://apihub.document360.io")
    configuration.api_key['api_token'] = os.environ["DOCUMENT360_API_TOKEN"]
    
    async with d361api.ApiClient(configuration) as api_client:
        categories_api = d361api.CategoriesApi(api_client)
        project_api = d361api.ProjectVersionsApi(api_client)
        
        # Get project version
        versions = await project_api.v2_project_versions_get()
        project_version_id = versions.data[0].id
        
        # Get all categories
        categories = await project_api.v2_project_versions_project_version_id_categories_get(
            project_version_id=project_version_id
        )
        
        print(f"Found {len(categories.data)} categories:")
        for category in categories.data:
            print(f"- {category.title} (Level: {category.level}, ID: {category.id})")
        
        # Create a new category
        from d361api.models import AddCategoryRequest
        new_category = AddCategoryRequest(
            title="API Documentation",
            description="Complete API reference and guides",
            parent_category_id=None,  # Root level category
            project_version_id=project_version_id
        )
        
        created_category = await categories_api.v2_categories_post(new_category)
        category_id = created_category.data.id
        print(f"Created category: {created_category.data.title} (ID: {category_id})")
        
        # Create subcategory
        subcategory = AddCategoryRequest(
            title="REST API Reference",
            description="REST API endpoints and examples",
            parent_category_id=category_id,
            project_version_id=project_version_id
        )
        
        created_subcategory = await categories_api.v2_categories_post(subcategory)
        print(f"Created subcategory: {created_subcategory.data.title}")

asyncio.run(category_management_example())
```

### 🔍 **Search & Discovery**
Advanced search capabilities including AI-powered assistance:

```python
async def search_and_discovery_example():
    configuration = d361api.Configuration(host="https://apihub.document360.io")
    configuration.api_key['api_token'] = os.environ["DOCUMENT360_API_TOKEN"]
    
    async with d361api.ApiClient(configuration) as api_client:
        project_api = d361api.ProjectVersionsApi(api_client)
        
        # Get project version
        versions = await project_api.v2_project_versions_get()
        project_version_id = versions.data[0].id
        
        # Perform text search
        search_results = await project_api.v2_project_versions_project_version_id_lang_code_get(
            project_version_id=project_version_id,
            lang_code="en",
            query="API authentication",  # Search query
            page=1,
            results_per_page=5
        )
        
        print(f"Search found {len(search_results.data.articles)} articles:")
        for article in search_results.data.articles:
            print(f"- {article.title}")
            if hasattr(article, 'snippet'):
                print(f"  Snippet: {article.snippet[:100]}...")
        
        # AI-powered search (Ask Eddy)
        from d361api.models import AIAssistiveSearchRequest
        ai_search_request = AIAssistiveSearchRequest(
            query="How do I authenticate API requests?",
            project_version_id=project_version_id,
            lang_code="en"
        )
        
        ai_results = await project_api.v2_project_versions_ask_eddy_post(
            ai_assistive_search_request=ai_search_request
        )
        
        print(f"\nAI Search Results:")
        print(f"Answer: {ai_results.data.answer}")
        if ai_results.data.reference_articles:
            print("Referenced articles:")
            for ref in ai_results.data.reference_articles:
                print(f"- {ref.title}")

asyncio.run(search_and_discovery_example())
```

### 📊 **Bulk Operations**
Efficient bulk processing for large-scale operations:

```python
async def bulk_operations_example():
    configuration = d361api.Configuration(host="https://apihub.document360.io")
    configuration.api_key['api_token'] = os.environ["DOCUMENT360_API_TOKEN"]
    
    async with d361api.ApiClient(configuration) as api_client:
        articles_api = d361api.ArticlesApi(api_client)
        
        # Bulk create articles
        from d361api.models import CreateArticleRequest
        
        articles_to_create = [
            CreateArticleRequest(
                title=f"Article {i}",
                content=f"<h1>Article {i}</h1><p>Content for article {i}</p>",
                category_id="12345"  # Replace with your category ID
            )
            for i in range(1, 6)  # Create 5 articles
        ]
        
        bulk_create_result = await articles_api.v2_articles_bulkcreate_post(
            articles_to_create
        )
        
        print(f"Bulk created {len(bulk_create_result.data.successful_articles)} articles")
        created_article_ids = [article.id for article in bulk_create_result.data.successful_articles]
        
        # Bulk publish articles
        from d361api.models import BulkPublishArticle
        
        articles_to_publish = [
            BulkPublishArticle(
                article_id=article_id,
                version_number=1
            )
            for article_id in created_article_ids
        ]
        
        bulk_publish_result = await articles_api.v2_articles_bulkpublish_lang_code_post(
            lang_code="en",
            bulk_publish_articles=articles_to_publish
        )
        
        print(f"Bulk published {len(bulk_publish_result.data.successful_articles)} articles")
        
        # Bulk update articles
        from d361api.models import BulkUpdateArticle
        
        articles_to_update = [
            BulkUpdateArticle(
                article_id=article_id,
                title=f"Updated Article {i+1}",
                content=f"<h1>Updated Article {i+1}</h1><p>Updated content...</p>"
            )
            for i, article_id in enumerate(created_article_ids)
        ]
        
        bulk_update_result = await articles_api.v2_articles_bulkupdate_put(
            articles_to_update
        )
        
        print(f"Bulk updated {len(bulk_update_result.data.successful_articles)} articles")

asyncio.run(bulk_operations_example())
```

### 👥 **Team & User Management**
Manage users, roles, and permissions:

```python
async def team_management_example():
    configuration = d361api.Configuration(host="https://apihub.document360.io")
    configuration.api_key['api_token'] = os.environ["DOCUMENT360_API_TOKEN"]
    
    async with d361api.ApiClient(configuration) as api_client:
        teams_api = d361api.TeamsApi(api_client)
        
        # Get all team members
        team_members = await teams_api.v2_teams_get()
        print(f"Team has {len(team_members.data)} members:")
        
        for member in team_members.data[:5]:  # Show first 5
            print(f"- {member.email} ({member.role_name})")
        
        # Get available roles
        roles = await teams_api.v2_teams_roles_get()
        print(f"\nAvailable roles:")
        for role in roles.data:
            print(f"- {role.role_name}: {role.description}")
        
        # Add a new team member
        from d361api.models import AddTeamAccountCustomer
        
        new_member = AddTeamAccountCustomer(
            email="new-member@company.com",
            first_name="New",
            last_name="Member",
            role_id=roles.data[0].role_id,  # Use first available role
            send_invitation=True
        )
        
        try:
            added_member = await teams_api.v2_teams_post(new_member)
            print(f"Added team member: {added_member.data.email}")
        except d361api.ApiException as e:
            print(f"Failed to add member: {e.reason}")
        
        # Get user groups
        groups = await teams_api.v2_teams_groups_get()
        print(f"\nUser groups:")
        for group in groups.data:
            print(f"- {group.group_name} ({len(group.users)} users)")

asyncio.run(team_management_example())
```

### 📁 **Drive & Media Management**
Handle file uploads and media organization:

```python
async def drive_management_example():
    configuration = d361api.Configuration(host="https://apihub.document360.io")
    configuration.api_key['api_token'] = os.environ["DOCUMENT360_API_TOKEN"]
    
    async with d361api.ApiClient(configuration) as api_client:
        drive_api = d361api.DriveApi(api_client)
        
        # Get all folders
        folders = await drive_api.v2_drive_folders_get()
        print(f"Drive has {len(folders.data.folders)} folders:")
        
        for folder in folders.data.folders[:3]:  # Show first 3
            print(f"- {folder.folder_name} (ID: {folder.folder_id})")
            print(f"  Files: {folder.total_files}, Size: {folder.folder_size}")
        
        # Create a new folder
        from d361api.models import AddMediaFolderRequestCustomer
        
        new_folder = AddMediaFolderRequestCustomer(
            folder_name="API Documentation Images",
            parent_folder_id=None  # Root level folder
        )
        
        created_folder = await drive_api.v2_drive_folders_post(new_folder)
        folder_id = created_folder.data.folder_id
        print(f"Created folder: {created_folder.data.folder_name} (ID: {folder_id})")
        
        # Get folder contents
        folder_contents = await drive_api.v2_drive_folders_folder_id_get(
            folder_id=folder_id
        )
        
        print(f"Folder '{folder_contents.data.folder_name}' contains {len(folder_contents.data.files)} files")
        
        # Search drive
        search_results = await drive_api.v2_drive_search_get(
            query="screenshot",
            page=1,
            results_per_page=5
        )
        
        print(f"Drive search found {len(search_results.data.files)} files:")
        for file in search_results.data.files:
            print(f"- {file.file_name} ({file.file_size} bytes)")

asyncio.run(drive_management_example())
```


### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import d361api
from d361api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://apihub.document360.io
# See configuration.py for a list of all supported configuration parameters.
configuration = d361api.Configuration(
    host = "https://apihub.document360.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_token
configuration.api_key['api_token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_token'] = 'Bearer'

# Enter a context with an instance of the API client
async with d361api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = d361api.APIReferencesApi(api_client)
    api_reference_id = 'api_reference_id_example' # str | The ID of the API reference
    page = 1 # int | Page number (optional) (default to 1)
    results_per_page = 5 # int | Total logs per page (optional) (default to 5)

    try:
        # Get all API reference logs
        api_response = await api_instance.v2_api_references_api_reference_id_logs_get(api_reference_id, page=page, results_per_page=results_per_page)
        print("The response of APIReferencesApi->v2_api_references_api_reference_id_logs_get:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling APIReferencesApi->v2_api_references_api_reference_id_logs_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://apihub.document360.io*

| Class | Method | HTTP request | Description |
| --- | --- | --- | --- |
| _APIReferencesApi_ | [**v2_api_references_api_reference_id_logs_get**](docs/APIReferencesApi.md#v2_api_references_api_reference_id_logs_get) | **GET** /v2/APIReferences/{apiReferenceId}/Logs | Get all API reference logs |
| _APIReferencesApi_ | [**v2_api_references_api_reference_id_logs_log_id_get**](docs/APIReferencesApi.md#v2_api_references_api_reference_id_logs_log_id_get) | **GET** /v2/APIReferences/{apiReferenceId}/Logs/{logId} | Get errors and alerts of a log |
| _APIReferencesApi_ | [**v2_api_references_delete**](docs/APIReferencesApi.md#v2_api_references_delete) | **DELETE** /v2/APIReferences | Deletes an API reference |
| _APIReferencesApi_ | [**v2_api_references_post**](docs/APIReferencesApi.md#v2_api_references_post) | **POST** /v2/APIReferences | Import the API reference spec file |
| _APIReferencesApi_ | [**v2_api_references_publish_post**](docs/APIReferencesApi.md#v2_api_references_publish_post) | **POST** /v2/APIReferences/publish | Publishes an API reference |
| _APIReferencesApi_ | [**v2_api_references_put**](docs/APIReferencesApi.md#v2_api_references_put) | **PUT** /v2/APIReferences | Resync the API reference spec file |
| _ArticlesApi_ | [**v2_articles_article_id_delete**](docs/ArticlesApi.md#v2_articles_article_id_delete) | **DELETE** /v2/Articles/{articleId} | Deletes an article with an ID |
| _ArticlesApi_ | [**v2_articles_article_id_fork_put**](docs/ArticlesApi.md#v2_articles_article_id_fork_put) | **PUT** /v2/Articles/{articleId}/fork | Forks an article with an id |
| _ArticlesApi_ | [**v2_articles_article_id_lang_code_get**](docs/ArticlesApi.md#v2_articles_article_id_lang_code_get) | **GET** /v2/Articles/{articleId}/{langCode} | Gets an article |
| _ArticlesApi_ | [**v2_articles_article_id_lang_code_publish_post**](docs/ArticlesApi.md#v2_articles_article_id_lang_code_publish_post) | **POST** /v2/Articles/{articleId}/{langCode}/publish | Publishes an article with an id |
| _ArticlesApi_ | [**v2_articles_article_id_lang_code_put**](docs/ArticlesApi.md#v2_articles_article_id_lang_code_put) | **PUT** /v2/Articles/{articleId}/{langCode} | Updates an article with the ID |
| _ArticlesApi_ | [**v2_articles_article_id_lang_code_settings_get**](docs/ArticlesApi.md#v2_articles_article_id_lang_code_settings_get) | **GET** /v2/Articles/{articleId}/{langCode}/settings | Gets settings for the article |
| _ArticlesApi_ | [**v2_articles_article_id_lang_code_settings_put**](docs/ArticlesApi.md#v2_articles_article_id_lang_code_settings_put) | **PUT** /v2/Articles/{articleId}/{langCode}/settings | Updates settings for the article |
| _ArticlesApi_ | [**v2_articles_article_id_lang_code_update_description_put**](docs/ArticlesApi.md#v2_articles_article_id_lang_code_update_description_put) | **PUT** /v2/Articles/{articleId}/{langCode}/updateDescription | Update the Article Description |
| _ArticlesApi_ | [**v2_articles_article_id_lang_code_version_version_number_delete**](docs/ArticlesApi.md#v2_articles_article_id_lang_code_version_version_number_delete) | **DELETE** /v2/Articles/{articleId}/{langCode}/version/{versionNumber} | Deletes an article version |
| _ArticlesApi_ | [**v2_articles_article_id_lang_code_versions_get**](docs/ArticlesApi.md#v2_articles_article_id_lang_code_versions_get) | **GET** /v2/Articles/{articleId}/{langCode}/versions | Gets all article versions |
| _ArticlesApi_ | [**v2_articles_article_id_lang_code_versions_version_number_get**](docs/ArticlesApi.md#v2_articles_article_id_lang_code_versions_version_number_get) | **GET** /v2/Articles/{articleId}/{langCode}/versions/{versionNumber} | Gets article by a version number |
| _ArticlesApi_ | [**v2_articles_article_id_publish_post**](docs/ArticlesApi.md#v2_articles_article_id_publish_post) | **POST** /v2/Articles/{articleId}/publish | Publishes an article with an id |
| _ArticlesApi_ | [**v2_articles_article_id_settings_get**](docs/ArticlesApi.md#v2_articles_article_id_settings_get) | **GET** /v2/Articles/{articleId}/settings | Gets settings for the article |
| _ArticlesApi_ | [**v2_articles_article_id_settings_put**](docs/ArticlesApi.md#v2_articles_article_id_settings_put) | **PUT** /v2/Articles/{articleId}/settings | Updates settings for the article |
| _ArticlesApi_ | [**v2_articles_article_id_update_description_put**](docs/ArticlesApi.md#v2_articles_article_id_update_description_put) | **PUT** /v2/Articles/{articleId}/updateDescription | Update the Article Description |
| _ArticlesApi_ | [**v2_articles_article_id_version_version_number_delete**](docs/ArticlesApi.md#v2_articles_article_id_version_version_number_delete) | **DELETE** /v2/Articles/{articleId}/version/{versionNumber} | Deletes an article version |
| _ArticlesApi_ | [**v2_articles_article_id_versions_get**](docs/ArticlesApi.md#v2_articles_article_id_versions_get) | **GET** /v2/Articles/{articleId}/versions | Gets all article versions |
| _ArticlesApi_ | [**v2_articles_article_id_versions_version_number_get**](docs/ArticlesApi.md#v2_articles_article_id_versions_version_number_get) | **GET** /v2/Articles/{articleId}/versions/{versionNumber} | Gets article by a version number |
| _ArticlesApi_ | [**v2_articles_bulkcreate_post**](docs/ArticlesApi.md#v2_articles_bulkcreate_post) | **POST** /v2/Articles/bulkcreate | Adds multiple articles |
| _ArticlesApi_ | [**v2_articles_bulkdelete_article_versions_delete**](docs/ArticlesApi.md#v2_articles_bulkdelete_article_versions_delete) | **DELETE** /v2/Articles/bulkdelete-article-versions | Delete multiple article versions |
| _ArticlesApi_ | [**v2_articles_bulkdelete_delete**](docs/ArticlesApi.md#v2_articles_bulkdelete_delete) | **DELETE** /v2/Articles/bulkdelete | Deletes multiple articles |
| _ArticlesApi_ | [**v2_articles_bulkpublish_lang_code_post**](docs/ArticlesApi.md#v2_articles_bulkpublish_lang_code_post) | **POST** /v2/Articles/bulkpublish/{langCode} | Publishes multiple articles |
| _ArticlesApi_ | [**v2_articles_bulkupdate_put**](docs/ArticlesApi.md#v2_articles_bulkupdate_put) | **PUT** /v2/Articles/bulkupdate | Updates multiple articles |
| _ArticlesApi_ | [**v2_articles_post**](docs/ArticlesApi.md#v2_articles_post) | **POST** /v2/Articles | Adds an article to an existing category |
| _CategoriesApi_ | [**v2_categories_bulkcreate_post**](docs/CategoriesApi.md#v2_categories_bulkcreate_post) | **POST** /v2/Categories/bulkcreate | Adds multiple Categories |
| _CategoriesApi_ | [**v2_categories_bulkdelete_category_versions_delete**](docs/CategoriesApi.md#v2_categories_bulkdelete_category_versions_delete) | **DELETE** /v2/Categories/bulkdelete-category-versions | Delete multiple category versions |
| _CategoriesApi_ | [**v2_categories_bulkpublish_lang_code_post**](docs/CategoriesApi.md#v2_categories_bulkpublish_lang_code_post) | **POST** /v2/Categories/bulkpublish/{langCode} | Publishes multiple categories |
| _CategoriesApi_ | [**v2_categories_bulkupdate_content_put**](docs/CategoriesApi.md#v2_categories_bulkupdate_content_put) | **PUT** /v2/Categories/bulkupdateContent | Update multiple page categories |
| _CategoriesApi_ | [**v2_categories_category_id_content_lang_code_get**](docs/CategoriesApi.md#v2_categories_category_id_content_lang_code_get) | **GET** /v2/Categories/{categoryId}/content/{langCode} | Get category page with an ID |
| _CategoriesApi_ | [**v2_categories_category_id_content_lang_code_put**](docs/CategoriesApi.md#v2_categories_category_id_content_lang_code_put) | **PUT** /v2/Categories/{categoryId}/content/{langCode} | Update a category page content with the ID |
| _CategoriesApi_ | [**v2_categories_category_id_delete**](docs/CategoriesApi.md#v2_categories_category_id_delete) | **DELETE** /v2/Categories/{categoryId} | Deletes an category with an ID |
| _CategoriesApi_ | [**v2_categories_category_id_fork_put**](docs/CategoriesApi.md#v2_categories_category_id_fork_put) | **PUT** /v2/Categories/{categoryId}/fork | Fork category page with an id |
| _CategoriesApi_ | [**v2_categories_category_id_get**](docs/CategoriesApi.md#v2_categories_category_id_get) | **GET** /v2/Categories/{categoryId} | Get category with an ID |
| _CategoriesApi_ | [**v2_categories_category_id_lang_code_publish_post**](docs/CategoriesApi.md#v2_categories_category_id_lang_code_publish_post) | **POST** /v2/Categories/{categoryId}/{langCode}/publish | Publishes an category with an id |
| _CategoriesApi_ | [**v2_categories_category_id_lang_code_settings_get**](docs/CategoriesApi.md#v2_categories_category_id_lang_code_settings_get) | **GET** /v2/Categories/{categoryId}/{langCode}/settings | Get settings for the Category |
| _CategoriesApi_ | [**v2_categories_category_id_lang_code_settings_put**](docs/CategoriesApi.md#v2_categories_category_id_lang_code_settings_put) | **PUT** /v2/Categories/{categoryId}/{langCode}/settings | Update settings for the category |
| _CategoriesApi_ | [**v2_categories_category_id_lang_code_update_description_put**](docs/CategoriesApi.md#v2_categories_category_id_lang_code_update_description_put) | **PUT** /v2/Categories/{categoryId}/{langCode}/updateDescription | Update the category description |
| _CategoriesApi_ | [**v2_categories_category_id_lang_code_version_version_number_delete**](docs/CategoriesApi.md#v2_categories_category_id_lang_code_version_version_number_delete) | **DELETE** /v2/Categories/{categoryId}/{langCode}/version/{versionNumber} | Delete category Version |
| _CategoriesApi_ | [**v2_categories_category_id_lang_codeversions_get**](docs/CategoriesApi.md#v2_categories_category_id_lang_codeversions_get) | **GET** /v2/Categories/{categoryId}/{langCode}versions | Get category page versions |
| _CategoriesApi_ | [**v2_categories_category_id_publish_post**](docs/CategoriesApi.md#v2_categories_category_id_publish_post) | **POST** /v2/Categories/{categoryId}/publish | Publishes an category with an id |
| _CategoriesApi_ | [**v2_categories_category_id_put**](docs/CategoriesApi.md#v2_categories_category_id_put) | **PUT** /v2/Categories/{categoryId} | Update a category with the ID |
| _CategoriesApi_ | [**v2_categories_category_id_settings_get**](docs/CategoriesApi.md#v2_categories_category_id_settings_get) | **GET** /v2/Categories/{categoryId}/settings | Get settings for the Category |
| _CategoriesApi_ | [**v2_categories_category_id_settings_put**](docs/CategoriesApi.md#v2_categories_category_id_settings_put) | **PUT** /v2/Categories/{categoryId}/settings | Update settings for the category |
| _CategoriesApi_ | [**v2_categories_category_id_update_category_type_put**](docs/CategoriesApi.md#v2_categories_category_id_update_category_type_put) | **PUT** /v2/Categories/{categoryId}/updateCategoryType | Update the Category Type |
| _CategoriesApi_ | [**v2_categories_category_id_update_description_put**](docs/CategoriesApi.md#v2_categories_category_id_update_description_put) | **PUT** /v2/Categories/{categoryId}/updateDescription | Update the category description |
| _CategoriesApi_ | [**v2_categories_category_id_version_version_number_delete**](docs/CategoriesApi.md#v2_categories_category_id_version_version_number_delete) | **DELETE** /v2/Categories/{categoryId}/version/{versionNumber} | Delete category Version |
| _CategoriesApi_ | [**v2_categories_category_id_versions_get**](docs/CategoriesApi.md#v2_categories_category_id_versions_get) | **GET** /v2/Categories/{categoryId}/versions | Get category page versions |
| _CategoriesApi_ | [**v2_categories_category_id_versions_lang_code_version_number_get**](docs/CategoriesApi.md#v2_categories_category_id_versions_lang_code_version_number_get) | **GET** /v2/Categories/{categoryId}/versions/{langCode}/{versionNumber} | Get category page content with an ID |
| _CategoriesApi_ | [**v2_categories_category_id_versions_version_number_get**](docs/CategoriesApi.md#v2_categories_category_id_versions_version_number_get) | **GET** /v2/Categories/{categoryId}/versions/{versionNumber} | Get category page content with an ID |
| _CategoriesApi_ | [**v2_categories_post**](docs/CategoriesApi.md#v2_categories_post) | **POST** /v2/Categories | Adds a new category |
| _DriveApi_ | [**v2_drive_folders_delete_file_status_task_id_get**](docs/DriveApi.md#v2_drive_folders_delete_file_status_task_id_get) | **GET** /v2/Drive/Folders/DeleteFile/Status/{taskId} | Get status of the delete file operation |
| _DriveApi_ | [**v2_drive_folders_files_post**](docs/DriveApi.md#v2_drive_folders_files_post) | **POST** /v2/Drive/Folders/Files | Add file in to drive |
| _DriveApi_ | [**v2_drive_folders_folder_id_delete**](docs/DriveApi.md#v2_drive_folders_folder_id_delete) | **DELETE** /v2/Drive/Folders/{folderId} | Delete a folder |
| _DriveApi_ | [**v2_drive_folders_folder_id_file_id_copy_post**](docs/DriveApi.md#v2_drive_folders_folder_id_file_id_copy_post) | **POST** /v2/Drive/Folders/{folderId}/{fileId}/Copy | Copy file from one folder to another |
| _DriveApi_ | [**v2_drive_folders_folder_id_file_id_delete**](docs/DriveApi.md#v2_drive_folders_folder_id_file_id_delete) | **DELETE** /v2/Drive/Folders/{folderId}/{fileId} | Delete file using file ID |
| _DriveApi_ | [**v2_drive_folders_folder_id_file_id_get**](docs/DriveApi.md#v2_drive_folders_folder_id_file_id_get) | **GET** /v2/Drive/Folders/{folderId}/{fileId} | Gets file information |
| _DriveApi_ | [**v2_drive_folders_folder_id_file_id_put**](docs/DriveApi.md#v2_drive_folders_folder_id_file_id_put) | **PUT** /v2/Drive/Folders/{folderId}/{fileId} | Move a file with file ID |
| _DriveApi_ | [**v2_drive_folders_folder_id_file_id_tags_bulkdelete_post**](docs/DriveApi.md#v2_drive_folders_folder_id_file_id_tags_bulkdelete_post) | **POST** /v2/Drive/Folders/{folderId}/{fileId}/Tags/Bulkdelete | Delete tags from files |
| _DriveApi_ | [**v2_drive_folders_folder_id_file_id_tags_post**](docs/DriveApi.md#v2_drive_folders_folder_id_file_id_tags_post) | **POST** /v2/Drive/Folders/{folderId}/{fileId}/Tags | Add tags in a file using file ID |
| _DriveApi_ | [**v2_drive_folders_folder_id_get**](docs/DriveApi.md#v2_drive_folders_folder_id_get) | **GET** /v2/Drive/Folders/{folderId} | Gets folder information by folder ID |
| _DriveApi_ | [**v2_drive_folders_get**](docs/DriveApi.md#v2_drive_folders_get) | **GET** /v2/Drive/Folders | Gets folders information |
| _DriveApi_ | [**v2_drive_folders_post**](docs/DriveApi.md#v2_drive_folders_post) | **POST** /v2/Drive/Folders | Add new folder in drive |
| _DriveApi_ | [**v2_drive_folders_put**](docs/DriveApi.md#v2_drive_folders_put) | **PUT** /v2/Drive/Folders | Update a folder with ID |
| _DriveApi_ | [**v2_drive_media_files_project_version_id_article_id_lang_code_get**](docs/DriveApi.md#v2_drive_media_files_project_version_id_article_id_lang_code_get) | **GET** /v2/Drive/MediaFiles/{projectVersionId}/{articleId}/{langCode} | Get all media files inserted in the article |
| _DriveApi_ | [**v2_drive_search_get**](docs/DriveApi.md#v2_drive_search_get) | **GET** /v2/Drive/Search | Drive search - files and folders |
| _LanguageApi_ | [**v2_language_project_version_id_get**](docs/LanguageApi.md#v2_language_project_version_id_get) | **GET** /v2/Language/{projectVersionId} | Gets all version languages in the project |
| _ProjectApi_ | [**v2_project_export_export_id_get**](docs/ProjectApi.md#v2_project_export_export_id_get) | **GET** /v2/Project/Export/{exportId} | Get the status of export |
| _ProjectApi_ | [**v2_project_export_post**](docs/ProjectApi.md#v2_project_export_post) | **POST** /v2/Project/Export | Start a new export |
| _ProjectApi_ | [**v2_project_import_import_id_get**](docs/ProjectApi.md#v2_project_import_import_id_get) | **GET** /v2/Project/Import/{importId} | Get the status of import |
| _ProjectApi_ | [**v2_project_import_post**](docs/ProjectApi.md#v2_project_import_post) | **POST** /v2/Project/Import | Import documentation |
| _ProjectApi_ | [**v2_project_schemes_get**](docs/ProjectApi.md#v2_project_schemes_get) | **GET** /v2/Project/Schemes | Get all the schemes for the project |
| _ProjectVersionsApi_ | [**v2_project_versions_ask_eddy_post**](docs/ProjectVersionsApi.md#v2_project_versions_ask_eddy_post) | **POST** /v2/ProjectVersions/ask-eddy | Perform AI assistive search within project version |
| _ProjectVersionsApi_ | [**v2_project_versions_get**](docs/ProjectVersionsApi.md#v2_project_versions_get) | **GET** /v2/ProjectVersions | Gets list of project versions |
| _ProjectVersionsApi_ | [**v2_project_versions_project_version_id_apireferences_get**](docs/ProjectVersionsApi.md#v2_project_versions_project_version_id_apireferences_get) | **GET** /v2/ProjectVersions/{projectVersionId}/apireferences | Gets list of api reference within project version |
| _ProjectVersionsApi_ | [**v2_project_versions_project_version_id_articles_get**](docs/ProjectVersionsApi.md#v2_project_versions_project_version_id_articles_get) | **GET** /v2/ProjectVersions/{projectVersionId}/articles | Gets list of articles within project version |
| _ProjectVersionsApi_ | [**v2_project_versions_project_version_id_categories_get**](docs/ProjectVersionsApi.md#v2_project_versions_project_version_id_categories_get) | **GET** /v2/ProjectVersions/{projectVersionId}/categories | Gets list of categories within project version |
| _ProjectVersionsApi_ | [**v2_project_versions_project_version_id_lang_code_get**](docs/ProjectVersionsApi.md#v2_project_versions_project_version_id_lang_code_get) | **GET** /v2/ProjectVersions/{projectVersionId}/{langCode} | Searches for a phrase inside project version |
| _ReadersApi_ | [**v2_readers_get**](docs/ReadersApi.md#v2_readers_get) | **GET** /v2/Readers | Get all available readers from the project |
| _ReadersApi_ | [**v2_readers_groups_get**](docs/ReadersApi.md#v2_readers_groups_get) | **GET** /v2/Readers/groups | Get all reader groups |
| _ReadersApi_ | [**v2_readers_groups_group_id_delete**](docs/ReadersApi.md#v2_readers_groups_group_id_delete) | **DELETE** /v2/Readers/groups/{groupId} | Deletes a reader group |
| _ReadersApi_ | [**v2_readers_groups_group_id_get**](docs/ReadersApi.md#v2_readers_groups_group_id_get) | **GET** /v2/Readers/groups/{groupId} | Get a reader group via group id |
| _ReadersApi_ | [**v2_readers_groups_group_id_put**](docs/ReadersApi.md#v2_readers_groups_group_id_put) | **PUT** /v2/Readers/groups/{groupId} | Updates a reader group |
| _ReadersApi_ | [**v2_readers_groups_post**](docs/ReadersApi.md#v2_readers_groups_post) | **POST** /v2/Readers/groups | Add a new reader group |
| _ReadersApi_ | [**v2_readers_jwt_delete**](docs/ReadersApi.md#v2_readers_jwt_delete) | **DELETE** /v2/Readers/JWT | Deletes JWT readers from the project |
| _ReadersApi_ | [**v2_readers_post**](docs/ReadersApi.md#v2_readers_post) | **POST** /v2/Readers | Add a new reader |
| _ReadersApi_ | [**v2_readers_reader_id_delete**](docs/ReadersApi.md#v2_readers_reader_id_delete) | **DELETE** /v2/Readers/{readerId} | Deletes a reader from the project |
| _ReadersApi_ | [**v2_readers_reader_id_put**](docs/ReadersApi.md#v2_readers_reader_id_put) | **PUT** /v2/Readers/{readerId} | Updates a reader |
| _TeamsApi_ | [**v2_teams_email_exists_get**](docs/TeamsApi.md#v2_teams_email_exists_get) | **GET** /v2/Teams/email-exists | Checks if email already exists in the project |
| _TeamsApi_ | [**v2_teams_get**](docs/TeamsApi.md#v2_teams_get) | **GET** /v2/Teams | Get all team accounts |
| _TeamsApi_ | [**v2_teams_groups_get**](docs/TeamsApi.md#v2_teams_groups_get) | **GET** /v2/Teams/groups | Get all user groups |
| _TeamsApi_ | [**v2_teams_post**](docs/TeamsApi.md#v2_teams_post) | **POST** /v2/Teams | Adds a new Team Account |
| _TeamsApi_ | [**v2_teams_roles_get**](docs/TeamsApi.md#v2_teams_roles_get) | **GET** /v2/Teams/roles | Get all available roles including default as well as custom roles |
| _TeamsApi_ | [**v2_teams_user_id_content_put**](docs/TeamsApi.md#v2_teams_user_id_content_put) | **PUT** /v2/Teams/{userId}/content | Update the content roles of an individual user |
| _TeamsApi_ | [**v2_teams_user_id_delete**](docs/TeamsApi.md#v2_teams_user_id_delete) | **DELETE** /v2/Teams/{userId} | Deletes a user with an ID |
| _TeamsApi_ | [**v2_teams_user_id_get**](docs/TeamsApi.md#v2_teams_user_id_get) | **GET** /v2/Teams/{userId} | Get complete user details by id |
| _TeamsApi_ | [**v2_teams_user_id_groups_put**](docs/TeamsApi.md#v2_teams_user_id_groups_put) | **PUT** /v2/Teams/{userId}/groups | Modify the groups associated with the user |
| _TeamsApi_ | [**v2_teams_user_id_portal_put**](docs/TeamsApi.md#v2_teams_user_id_portal_put) | **PUT** /v2/Teams/{userId}/portal | Update the portal role of a individual user |
| _TranslationsApi_ | [**v2_translations_project_version_id_lang_code_get**](docs/TranslationsApi.md#v2_translations_project_version_id_lang_code_get) | **GET** /v2/Translations/{projectVersionId}/{langCode} | Gets articles by translation status |

## Documentation For Models

- [AIAssistiveSearch](docs/AIAssistiveSearch.md)
- [AIAssistiveSearchRequest](docs/AIAssistiveSearchRequest.md)
- [AccessScopeCustomerV2](docs/AccessScopeCustomerV2.md)
- [AccessScopeLevel](docs/AccessScopeLevel.md)
- [AddCategoryRequest](docs/AddCategoryRequest.md)
- [AddCategoryResponse](docs/AddCategoryResponse.md)
- [AddMediaFileResponseCustomer](docs/AddMediaFileResponseCustomer.md)
- [AddMediaFolderRequestCustomer](docs/AddMediaFolderRequestCustomer.md)
- [AddReaderGroupRequestV2](docs/AddReaderGroupRequestV2.md)
- [AddReaderRequestV2](docs/AddReaderRequestV2.md)
- [AddTeamAccountCustomer](docs/AddTeamAccountCustomer.md)
- [AddUpdateAccessScopeCustomerV2](docs/AddUpdateAccessScopeCustomerV2.md)
- [AddUserData](docs/AddUserData.md)
- [AddUserDataCustomerApiResponse](docs/AddUserDataCustomerApiResponse.md)
- [AllFilesWithCountCustomer](docs/AllFilesWithCountCustomer.md)
- [AllFilesWithCountResponseCustomer](docs/AllFilesWithCountResponseCustomer.md)
- [ApiDefinitionInforamtionCustomer](docs/ApiDefinitionInforamtionCustomer.md)
- [ApiDocsImportDataCustomer](docs/ApiDocsImportDataCustomer.md)
- [ApiDocsResyncDataCustomer](docs/ApiDocsResyncDataCustomer.md)
- [ApiDocumentationImportResponseCustomer](docs/ApiDocumentationImportResponseCustomer.md)
- [ApiDocumentationResyncResponseCustomer](docs/ApiDocumentationResyncResponseCustomer.md)
- [ApiErrorAndWarningsData](docs/ApiErrorAndWarningsData.md)
- [ApiLogs](docs/ApiLogs.md)
- [ApiReferenceLogsDataCustomer](docs/ApiReferenceLogsDataCustomer.md)
- [ApiReferenceLogsWrapResponseCustomer](docs/ApiReferenceLogsWrapResponseCustomer.md)
- [ApiReferencePublishRequestCustomer](docs/ApiReferencePublishRequestCustomer.md)
- [ArticleAccessInfo](docs/ArticleAccessInfo.md)
- [ArticleContentType](docs/ArticleContentType.md)
- [ArticleMatchedData](docs/ArticleMatchedData.md)
- [ArticleSettingCustomer](docs/ArticleSettingCustomer.md)
- [ArticleSettingCustomerResponse](docs/ArticleSettingCustomerResponse.md)
- [ArticleSimpleDataCustomer](docs/ArticleSimpleDataCustomer.md)
- [ArticleSimpleDataCustomerResponse](docs/ArticleSimpleDataCustomerResponse.md)
- [ArticleSimpleVersionCustomer](docs/ArticleSimpleVersionCustomer.md)
- [ArticleStaleStatus](docs/ArticleStaleStatus.md)
- [ArticleStatusCustomer](docs/ArticleStatusCustomer.md)
- [ArticleStatusIndicator](docs/ArticleStatusIndicator.md)
- [ArticleType](docs/ArticleType.md)
- [ArticleVersionDataCustomerResponse](docs/ArticleVersionDataCustomerResponse.md)
- [ArticleVersionInfoCustomerResponse](docs/ArticleVersionInfoCustomerResponse.md)
- [BackgroundTaskStatus](docs/BackgroundTaskStatus.md)
- [BaseError](docs/BaseError.md)
- [BaseInformation](docs/BaseInformation.md)
- [BaseResponseContext](docs/BaseResponseContext.md)
- [BaseWarning](docs/BaseWarning.md)
- [BooleanCustomerApiResponse](docs/BooleanCustomerApiResponse.md)
- [BulkArticleResultCustomer](docs/BulkArticleResultCustomer.md)
- [BulkCategoryResult](docs/BulkCategoryResult.md)
- [BulkCreateArticleResponseCustomer](docs/BulkCreateArticleResponseCustomer.md)
- [BulkCreateCategoryResponse](docs/BulkCreateCategoryResponse.md)
- [BulkDeleteArticleResponse](docs/BulkDeleteArticleResponse.md)
- [BulkDeleteArticleVersionResonse](docs/BulkDeleteArticleVersionResonse.md)
- [BulkDeleteCategoryVersionResponse](docs/BulkDeleteCategoryVersionResponse.md)
- [BulkPublishArticle](docs/BulkPublishArticle.md)
- [BulkPublishCategory](docs/BulkPublishCategory.md)
- [BulkPublishCategoryResponse](docs/BulkPublishCategoryResponse.md)
- [BulkUpdateArticle](docs/BulkUpdateArticle.md)
- [BulkUpdateArticleResponse](docs/BulkUpdateArticleResponse.md)
- [BulkUpdateCategoryContentResponse](docs/BulkUpdateCategoryContentResponse.md)
- [CategoryAccessInfo](docs/CategoryAccessInfo.md)
- [CategoryDataCustomer](docs/CategoryDataCustomer.md)
- [CategoryMeta](docs/CategoryMeta.md)
- [CategoryScopeCustomer](docs/CategoryScopeCustomer.md)
- [CategorySettingsCustomer](docs/CategorySettingsCustomer.md)
- [CategorySimpleData](docs/CategorySimpleData.md)
- [CategorySimpleVersionCustomer](docs/CategorySimpleVersionCustomer.md)
- [CategorySummaryCustomerV2](docs/CategorySummaryCustomerV2.md)
- [CategoryType](docs/CategoryType.md)
- [CategoryVersionData](docs/CategoryVersionData.md)
- [CategoryVersionDataCustomer](docs/CategoryVersionDataCustomer.md)
- [CompleteUserInfoCustomer](docs/CompleteUserInfoCustomer.md)
- [CompleteUserInfoCustomerCustomerApiResponse](docs/CompleteUserInfoCustomerCustomerApiResponse.md)
- [Content](docs/Content.md)
- [ContentPermissionCustomer](docs/ContentPermissionCustomer.md)
- [ContentRoleInfo](docs/ContentRoleInfo.md)
- [ContentRoleSummaryCustomer](docs/ContentRoleSummaryCustomer.md)
- [CreateArticleRequest](docs/CreateArticleRequest.md)
- [CreateArticleResponse](docs/CreateArticleResponse.md)
- [CustomerApiBaseResponse](docs/CustomerApiBaseResponse.md)
- [DataSourceType](docs/DataSourceType.md)
- [DateRange](docs/DateRange.md)
- [DeleteApiDefinitionCustomer](docs/DeleteApiDefinitionCustomer.md)
- [DeleteApiReferenceResponseCustomer](docs/DeleteApiReferenceResponseCustomer.md)
- [DeleteMediaFileResponseCustomer](docs/DeleteMediaFileResponseCustomer.md)
- [DeletedandStarredMetaDataCustomer](docs/DeletedandStarredMetaDataCustomer.md)
- [DriveTaskStatus](docs/DriveTaskStatus.md)
- [EditContentRoleCustomer](docs/EditContentRoleCustomer.md)
- [EditPortalRoleCustomer](docs/EditPortalRoleCustomer.md)
- [EditUserGroupsCustomer](docs/EditUserGroupsCustomer.md)
- [EditableElementTypes](docs/EditableElementTypes.md)
- [EmailExists](docs/EmailExists.md)
- [EmailExistsResponse](docs/EmailExistsResponse.md)
- [ExportDocumentationRequest](docs/ExportDocumentationRequest.md)
- [ExportDocumentationResponse](docs/ExportDocumentationResponse.md)
- [ExportDocumentationStatusResponse](docs/ExportDocumentationStatusResponse.md)
- [FeatureAnalytics](docs/FeatureAnalytics.md)
- [FeatureExplorerStatus](docs/FeatureExplorerStatus.md)
- [FeatureExplorerUserAnalyticsEntity](docs/FeatureExplorerUserAnalyticsEntity.md)
- [FeatureExplorerUserRoleEnum](docs/FeatureExplorerUserRoleEnum.md)
- [FeatureListEnum](docs/FeatureListEnum.md)
- [ForkArticleVersionRequest](docs/ForkArticleVersionRequest.md)
- [ForkArticleVersionResponse](docs/ForkArticleVersionResponse.md)
- [ForkCategoryVersionRequest](docs/ForkCategoryVersionRequest.md)
- [ForkCategoryVersionResponse](docs/ForkCategoryVersionResponse.md)
- [FormEditableProperties](docs/FormEditableProperties.md)
- [GetApiReferenceDataResponseCustomer](docs/GetApiReferenceDataResponseCustomer.md)
- [GetArticleNotTranslatedResponse](docs/GetArticleNotTranslatedResponse.md)
- [GetArticleResponseCustomer](docs/GetArticleResponseCustomer.md)
- [GetArticleSettingsResponse](docs/GetArticleSettingsResponse.md)
- [GetArticleVersionResponse](docs/GetArticleVersionResponse.md)
- [GetArticleVersionsResponse](docs/GetArticleVersionsResponse.md)
- [GetArticlesResponseCustomer](docs/GetArticlesResponseCustomer.md)
- [GetCategoriesResponse](docs/GetCategoriesResponse.md)
- [GetCategoryContentResponse](docs/GetCategoryContentResponse.md)
- [GetCategoryResponse](docs/GetCategoryResponse.md)
- [GetCategorySettingsResponse](docs/GetCategorySettingsResponse.md)
- [GetCategoryVersionsResponse](docs/GetCategoryVersionsResponse.md)
- [GetCustomerTaskStatusResponse](docs/GetCustomerTaskStatusResponse.md)
- [GetDriveFilesInArticleDataCustomer](docs/GetDriveFilesInArticleDataCustomer.md)
- [GetLanguageFromProjectVersion](docs/GetLanguageFromProjectVersion.md)
- [GetLogsDetailsResponseCustomer](docs/GetLogsDetailsResponseCustomer.md)
- [GetMediaFolderResponseCustomer](docs/GetMediaFolderResponseCustomer.md)
- [GetMediaFolderWithIdCustomer](docs/GetMediaFolderWithIdCustomer.md)
- [GetProjectVersionsResponse](docs/GetProjectVersionsResponse.md)
- [GetReaderResponseCustomer](docs/GetReaderResponseCustomer.md)
- [GroupInfo](docs/GroupInfo.md)
- [Highlightresult](docs/Highlightresult.md)
- [Hit](docs/Hit.md)
- [ImportAPILog](docs/ImportAPILog.md)
- [ImportDocumemtationLogMessageType](docs/ImportDocumemtationLogMessageType.md)
- [ImportDocumentationLogAction](docs/ImportDocumentationLogAction.md)
- [ImportDocumentationRequest](docs/ImportDocumentationRequest.md)
- [ImportDocumentationResponse](docs/ImportDocumentationResponse.md)
- [ImportDocumentationStatusResponse](docs/ImportDocumentationStatusResponse.md)
- [Language](docs/Language.md)
- [LanguageAccessInfo](docs/LanguageAccessInfo.md)
- [LanguageMeta](docs/LanguageMeta.md)
- [LanguageScopeCustomer](docs/LanguageScopeCustomer.md)
- [LanguageSummaryCustomer](docs/LanguageSummaryCustomer.md)
- [LanguageTranslationOption](docs/LanguageTranslationOption.md)
- [MediaFileAndTagsMetaDataCustomer](docs/MediaFileAndTagsMetaDataCustomer.md)
- [MediaFileAndTagsMetaDataResponseCustomer](docs/MediaFileAndTagsMetaDataResponseCustomer.md)
- [MediaFileDataResponseCustomer](docs/MediaFileDataResponseCustomer.md)
- [MediaFileMetaDataCustomer](docs/MediaFileMetaDataCustomer.md)
- [MediaFilesMetaDataCustomer](docs/MediaFilesMetaDataCustomer.md)
- [MediaFolderMetaDataCustomer](docs/MediaFolderMetaDataCustomer.md)
- [MediaFolderMetaDataResponseCustomer](docs/MediaFolderMetaDataResponseCustomer.md)
- [MediaFolderViewMetaDataCustomer](docs/MediaFolderViewMetaDataCustomer.md)
- [MediaFoldersDataCustomer](docs/MediaFoldersDataCustomer.md)
- [NeedTranslationArticleData](docs/NeedTranslationArticleData.md)
- [ProjectLanguage](docs/ProjectLanguage.md)
- [ProjectProtection](docs/ProjectProtection.md)
- [ProjectVersionCustomer](docs/ProjectVersionCustomer.md)
- [ProjectVersionTypeCustomer](docs/ProjectVersionTypeCustomer.md)
- [PublishArticleRequest](docs/PublishArticleRequest.md)
- [PublishCategoryRequest](docs/PublishCategoryRequest.md)
- [ReaderGroupCustomerV2](docs/ReaderGroupCustomerV2.md)
- [ReaderGroupCustomerV2CustomerApiResponse](docs/ReaderGroupCustomerV2CustomerApiResponse.md)
- [ReaderGroupCustomerV2ListCustomerApiResponse](docs/ReaderGroupCustomerV2ListCustomerApiResponse.md)
- [RelatedArticleData](docs/RelatedArticleData.md)
- [RoleMetaData](docs/RoleMetaData.md)
- [RoleMetaDataListCustomerApiResponse](docs/RoleMetaDataListCustomerApiResponse.md)
- [RoleSummaryCustomer](docs/RoleSummaryCustomer.md)
- [RoleType](docs/RoleType.md)
- [SSOSchemeDetails](docs/SSOSchemeDetails.md)
- [SSOSchemeReponse](docs/SSOSchemeReponse.md)
- [SSOUserTypes](docs/SSOUserTypes.md)
- [SearchProjectVersionResponseCustomerApi](docs/SearchProjectVersionResponseCustomerApi.md)
- [SectionTypeEnum](docs/SectionTypeEnum.md)
- [Snippetresult](docs/Snippetresult.md)
- [StaleStatus](docs/StaleStatus.md)
- [StringCustomerApiResponse](docs/StringCustomerApiResponse.md)
- [TagsMetaDataCustomer](docs/TagsMetaDataCustomer.md)
- [TeamAccountGroupSummaryCustomer](docs/TeamAccountGroupSummaryCustomer.md)
- [TeamAccountGroupSummaryCustomerListCustomerApiResponse](docs/TeamAccountGroupSummaryCustomerListCustomerApiResponse.md)
- [TeamAccountSummaryCustomer](docs/TeamAccountSummaryCustomer.md)
- [TeamAccountSummaryCustomerListCustomerApiResponse](docs/TeamAccountSummaryCustomerListCustomerApiResponse.md)
- [Title](docs/Title.md)
- [TrophyStatus](docs/TrophyStatus.md)
- [UIElement](docs/UIElement.md)
- [UIElementType](docs/UIElementType.md)
- [UpdateArticleRequest](docs/UpdateArticleRequest.md)
- [UpdateArticleSettingsRequest](docs/UpdateArticleSettingsRequest.md)
- [UpdateArticleSettingsResponseCustomer](docs/UpdateArticleSettingsResponseCustomer.md)
- [UpdateCategoryContentCustomerRequest](docs/UpdateCategoryContentCustomerRequest.md)
- [UpdateCategoryContentCustomerResponse](docs/UpdateCategoryContentCustomerResponse.md)
- [UpdateCategoryContentRequest](docs/UpdateCategoryContentRequest.md)
- [UpdateCategoryRequest](docs/UpdateCategoryRequest.md)
- [UpdateCategoryResponse](docs/UpdateCategoryResponse.md)
- [UpdateMediaFolderRequestCustomer](docs/UpdateMediaFolderRequestCustomer.md)
- [UpdateReaderGroupRequestV2](docs/UpdateReaderGroupRequestV2.md)
- [UpdateReaderRequestV2](docs/UpdateReaderRequestV2.md)
- [UserAccess](docs/UserAccess.md)
- [UserDetailsCustomer](docs/UserDetailsCustomer.md)
- [UserProfileCustomer](docs/UserProfileCustomer.md)
- [VectorSearchReferenceArticles](docs/VectorSearchReferenceArticles.md)
- [VersionAccessInfo](docs/VersionAccessInfo.md)
- [ViewFormControl](docs/ViewFormControl.md)

<a id="documentation-for-authorization"></a>

## Documentation For Authorization

Authentication schemes defined for the API: <a id="api_token"></a>

### api_token

- **Type**: API key
- **API key parameter name**: api_token
- **Location**: HTTP header

## Author

support@document360.com
