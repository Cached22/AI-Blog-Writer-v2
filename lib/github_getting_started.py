```python
import requests
from bs4 import BeautifulSoup

def scrape_github_readme(repo_url):
    """
    Scrapes the README file from a given GitHub repository URL.

    Parameters:
    repo_url (str): The URL of the GitHub repository.

    Returns:
    str: The content of the README file or an error message.
    """
    # Check if the URL is a valid GitHub repository
    if not repo_url.startswith("https://github.com/"):
        return "Invalid GitHub repository URL."

    # Construct the raw content URL
    raw_url = repo_url.replace("https://github.com/", "https://raw.githubusercontent.com/") + "/master/README.md"

    try:
        # Send a GET request to the raw content URL
        response = requests.get(raw_url)
        response.raise_for_status()  # Raise an HTTPError if the HTTP request returned an unsuccessful status code

        # Parse the README content using BeautifulSoup if the content is markdown
        if 'text/markdown' in response.headers.get('Content-Type', ''):
            soup = BeautifulSoup(response.text, 'html.parser')
            return soup.get_text()
        else:
            return "README content is not in markdown format."

    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"
    except Exception as err:
        return f"An error occurred: {err}"

def generate_blog_from_readme(repo_url):
    """
    Generates a blog post draft from a GitHub repository's README file.

    Parameters:
    repo_url (str): The URL of the GitHub repository.

    Returns:
    str: The generated blog content or an error message.
    """
    # Scrape the README content
    readme_content = scrape_github_readme(repo_url)

    # Check for errors in the scraping process
    if readme_content.startswith("Error"):
        return readme_content

    # Placeholder for further processing of the README content into a blog post
    # This can include formatting, adding additional sections, etc.
    blog_post_content = readme_content  # This would be replaced with actual processing logic

    return blog_post_content

# Example usage:
# blog_post = generate_blog_from_readme("https://github.com/username/repository")
# print(blog_post)
```