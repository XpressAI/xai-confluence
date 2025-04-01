import os
from xai_components.base import Component, InArg, InCompArg, OutArg, xai_component
from atlassian import Confluence

@xai_component
class ConfluenceAuthorize(Component):
    """A component to initialize a Confluence client.

    ##### inPorts:
    - url (str): The URL of the Confluence instance. If from_env is True, reads from CONFLUENCE_URL.
    - username (str): The username for authentication. If from_env is True, reads from CONFLUENCE_USER.
    - password (str): The password for authentication. If from_env is True, reads from CONFLUENCE_PASSWORD.
    - from_env (bool): If True, reads credentials from environment variables instead of input ports.

    ##### outPorts:
    - client (Confluence): The initialized Confluence client.
    """
    url: InArg[str]
    username: InArg[str]
    password: InArg[str]
    from_env: InCompArg[bool]
    client: OutArg[Confluence]

    def execute(self, ctx) -> None:
        if self.from_env.value:
            url = os.environ.get('CONFLUENCE_URL')
            username = os.environ.get('CONFLUENCE_USER')
            password = os.environ.get('CONFLUENCE_PASSWORD')
            if not all([url, username, password]):
                raise ValueError("Missing required environment variables: CONFLUENCE_URL, CONFLUENCE_USER, CONFLUENCE_PASSWORD")
        else:
            url = self.url.value
            username = self.username.value
            password = self.password.value

        self.client.value = Confluence(
            url=url,
            username=username,
            password=password,
            cloud=True
        )
        ctx['confluence_client'] = self.client.value




@xai_component
class ConfluenceGetPage(Component):
    """A component to get a page from Confluence.

    ##### inPorts:
    - client (Confluence): The Confluence client.
    - page_id (str): The ID of the page to retrieve.

    ##### outPorts:
    - page (dict): The retrieved page data.
    """
    client: InArg[Confluence]
    page_id: InArg[str]
    page: OutArg[dict]

    def execute(self, ctx) -> None:
        client = self.client.value if self.client.value else ctx.get('confluence_client')
        if not client:
            raise ValueError("No Confluence client provided or found in context")
        self.page.value = client.get_page_by_id(self.page_id.value)

@xai_component
class ConfluenceSearchPages(Component):
    """A component to search for pages in Confluence.

    ##### inPorts:
    - client (Confluence): The Confluence client.
    - query (str): The search query.

    ##### outPorts:
    - results (list): The list of pages matching the search query.
    """
    client: InArg[Confluence]
    query: InArg[str]
    results: OutArg[list]

    def execute(self, ctx) -> None:
        client = self.client.value if self.client.value else ctx.get('confluence_client')
        if not client:
            raise ValueError("No Confluence client provided or found in context")
        self.results.value = client.cql(f'SELECT * FROM content WHERE type = "page" AND title ~ "{self.query.value}"')


@xai_component
class ConfluenceCQLQuery(Component):
    """A component to perform arbitrary CQL on Confluence.

    ##### inPorts:
    - client (Confluence): The Confluence client.
    - query (str): The CQL query.

    ##### outPorts:
    - results (list): The list of pages matching the search query.
    """
    client: InArg[Confluence]
    query: InArg[str]
    results: OutArg[list]

    def execute(self, ctx) -> None:
        client = self.client.value if self.client.value else ctx.get('confluence_client')
        if not client:
            raise ValueError("No Confluence client provided or found in context")
        self.results.value = client.cql(self.query.value)


@xai_component
class ConfluenceSearchByQueryAndTag(Component):
    """A component to search for pages in Confluence by both query and tags.

    ##### inPorts:
    - client (Confluence): The Confluence client.
    - query (str): The search query for page content or title.
    - tags (list): List of labels/tags that pages must have.
    - match_all_tags (bool): If True, pages must have all specified tags. If False, pages can match any of the tags.

    ##### outPorts:
    - results (list): The list of pages matching both the search query and tags.
    """
    client: InArg[Confluence]
    query: InArg[str]
    tags: InArg[list]
    match_all_tags: InArg[bool]
    results: OutArg[list]

    def execute(self, ctx) -> None:
        client = self.client.value if self.client.value else ctx.get('confluence_client')
        if not client:
            raise ValueError("No Confluence client provided or found in context")
            
        # Build the CQL query
        tag_conditions = []
        for tag in self.tags.value:
            tag_conditions.append(f'labelText = "{tag}"')

        tag_operator = " AND " if self.match_all_tags.value else " OR "
        tag_query = f"({tag_operator.join(tag_conditions)})"

        full_query = f'type = page AND title ~ "{self.query.value}"'
        if tag_conditions:
            full_query += f' AND {tag_query}'

        self.results.value = client.cql(full_query)


@xai_component
class ConfluenceCreatePage(Component):
    """A component to create a new page in Confluence.

    ##### inPorts:
    - client (Confluence): The Confluence client.
    - space (str): The space key where the page will be created.
    - title (str): The title of the new page.
    - content (str): The content of the new page.

    ##### outPorts:
    - page (dict): The created page data.
    """
    client: InArg[Confluence]
    space: InArg[str]
    title: InArg[str]
    content: InArg[str]
    page: OutArg[dict]

    def execute(self, ctx) -> None:
        client = self.client.value if self.client.value else ctx.get('confluence_client')
        if not client:
            raise ValueError("No Confluence client provided or found in context")
        self.page.value = client.create_page(
            space=self.space.value,
            title=self.title.value,
            body=self.content.value
        )
