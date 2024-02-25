```python
import requests
from bs4 import BeautifulSoup

def generate_blog_from_google_serp(keywords):
    """
    Generates a blog post draft based on trending Google searches related to the specified keywords.

    Parameters:
    keywords (list of str): Keywords to use for generating the blog content from Google SERP.

    Returns:
    str: The generated blog content draft.
    """
    # Construct the Google search URL with the provided keywords
    search_query = '+'.join(keywords)
    url = f"https://www.google.com/search?q={search_query}&num=10"

    # Perform the Google search request
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code != 200:
        return "Failed to retrieve search results. Please try again."

    # Parse the content of the request with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all search result entries
    search_results = soup.find_all('div', class_='tF2Cxc')

    # Extract and compile the content from the search results
    blog_draft = ""
    for result in search_results:
        # Extract the title and snippet from each search result
        title = result.find('h3').text
        snippet = result.find('div', class_='IsZvec').text

        # Append the title and snippet to the blog draft
        blog_draft += f"## {title}\n{snippet}\n\n"

    return blog_draft

# Example usage:
# keywords = ["machine learning", "data science"]
# blog_content = generate_blog_from_google_serp(keywords)
# print(blog_content)
```