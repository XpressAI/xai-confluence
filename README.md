<p align="center">
  <a href="https://github.com/XpressAI/xircuits/tree/master/xai_components#xircuits-component-library-list">Component Libraries</a> •
  <a href="https://github.com/XpressAI/xircuits/tree/master/project-templates#xircuits-project-templates-list">Project Templates</a>
  <br>
  <a href="https://xircuits.io/">Docs</a> •
  <a href="https://xircuits.io/docs/Installation">Install</a> •
  <a href="https://xircuits.io/docs/category/tutorials">Tutorials</a> •
  <a href="https://xircuits.io/docs/category/developer-guide">Developer Guides</a> •
  <a href="https://github.com/XpressAI/xircuits/blob/master/CONTRIBUTING.md">Contribute</a> •
  <a href="https://www.xpress.ai/blog/">Blog</a> •
  <a href="https://discord.com/invite/vgEg2ZtxCw">Discord</a>
</p>

<p align="center"><i>Xircuits Component Library for Confluence! Seamlessly manage and interact with Confluence content.</i></p>

---

## Xircuits Component Library for Confluence

This library enables seamless integration with Atlassian Confluence in Xircuits workflows. With it, you can authenticate, retrieve pages, search content, create new pages, and manage Confluence data efficiently.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Main Xircuits Components](#main-xircuits-components)
- [Try the Examples](#try-the-examples)
- [Installation](#installation)

## Prerequisites

Before you begin, make sure you have the following:

1. Python 3.9+.
2. Xircuits.
3. A Confluence instance with API access.
4. Confluence authentication credentials (username and password) or environment variables (`CONFLUENCE_URL`, `CONFLUENCE_USER`, `CONFLUENCE_PASSWORD`).

## Main Xircuits Components

### ConfluenceAuthorize Component:  
Initializes a Confluence client with the provided credentials or from environment variables.  

<img src="https://github.com/user-attachments/assets/86bef646-8655-453c-93d5-f3922e5e0adc" alt="Image" width="200" height="150" />

### ConfluenceGetPage Component:  
Retrieves a specific page from Confluence using its page ID.  

<img src="https://github.com/user-attachments/assets/d9373f87-61aa-4eb0-9dc5-4bff0a8dfee0" alt="Image" width="200" height="100" />


### ConfluenceSearchPages Component:  
Searches for pages in Confluence based on a query string.  

### ConfluenceSearchByQueryAndTag Component:  
Searches for pages using both a query and specified tags. Supports filtering by all tags or any tag.  

### ConfluenceCreatePage Component:  
Creates a new page in a specified Confluence space with a given title and content.  


## Installation

To use this component library, ensure that you have an existing [Xircuits setup](https://xircuits.io/docs/main/Installation). You can then install the Confluence library using the [component library interface](https://xircuits.io/docs/component-library/installation#installation-using-the-xircuits-library-interface), or through the CLI using:

```
xircuits install confluence
```

You can also install it manually by cloning the repository:

```
# base Xircuits directory

git clone https://github.com/XpressAI/xai-confluence xai_components/xai_confluence
pip install -r xai_components/xai_confluence/requirements.txt
```

