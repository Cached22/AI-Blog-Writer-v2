```python
import requests
from bs4 import BeautifulSoup

def scrape_github_readme(repo_url):
    """
    Scrapes the README.md file from a given GitHub repository URL.

    Parameters:
    repo_url (str): The URL of the GitHub repository.

    Returns:
    str: The content of the README.md file or an error message.
    """
    # Check if the URL is a valid GitHub repository
    if not repo_url.startswith("https://github.com/"):
        return "Invalid GitHub repository URL."

    # Convert the GitHub repository URL to the raw README.md URL
    raw_url = repo_url.replace("https://github.com/", "https://raw.githubusercontent.com/") + "/master/README.md"

    try:
        # Send a GET request to the raw README.md URL
        response = requests.get(raw_url)
        response.raise_for_status()  # Raise an HTTPError if the HTTP request returned an unsuccessful status code

        # Parse the README.md content using BeautifulSoup if the content type is text/markdown
        if 'text/markdown' in response.headers.get('content-type', ''):
            soup = BeautifulSoup(response.content, 'html.parser')
            return soup.get_text()
        else:
            return "README.md not found or is not in markdown format."

    except requests.exceptions.HTTPError as http_err:
        # Handle HTTP errors
        return f"HTTP error occurred: {http_err}"
    except requests.exceptions.RequestException as err:
        # Handle other requests exceptions
        return f"An error occurred: {err}"

# Example usage:
# readme_content = scrape_github_readme("https://github.com/username/repository")
# print(readme_content)
```