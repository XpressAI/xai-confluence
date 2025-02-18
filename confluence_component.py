from xai_components.base import Component, InArg, OutArg, xai_component
from atlassian import Confluence

@xai_component
class ConfluenceAuthorize(Component):
    """A component to initialize a Confluence client.

    ##### inPorts:
    - url (str): The URL of the Confluence instance.
    - username (str): The username for authentication.
    - password (str): The password for authentication.

    ##### outPorts:
    - client (Confluence): The initialized Confluence client.
    """
    url: InArg[str]
    username: InArg[str]
    password: InArg[str]
    client: OutArg[Confluence]

    def execute(self, ctx) -> None:
        self.client.value = Confluence(
            url=self.url.value,
            username=self.username.value,
            password=self.password.value,
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
        self.page.value = self.client.value.get_page_by_id(self.page_id.value)

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
        self.results.value = self.client.value.cql(f'SELECT * FROM content WHERE type = "page" AND title ~ "{self.query.value}"')

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
        self.page.value = self.client.value.create_page(
            space=self.space.value,
            title=self.title.value,
            body=self.content.value
        )
