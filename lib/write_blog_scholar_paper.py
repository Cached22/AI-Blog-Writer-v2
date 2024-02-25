```python
import requests
from bs4 import BeautifulSoup

def fetch_scholarly_paper(paper_url):
    """
    Fetches the content of a scholarly paper from the provided URL.

    Parameters:
    paper_url (str): The URL of the scholarly paper.

    Returns:
    str: The text content of the scholarly paper.
    """
    try:
        response = requests.get(paper_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        paper_content = soup.get_text()
        return paper_content
    except requests.RequestException as e:
        return f"An error occurred while fetching the scholarly paper: {e}"

def write_blog_scholar_paper(paper_url):
    """
    Generates a blog post based on the content of a scholarly paper.

    Parameters:
    paper_url (str): The URL of the scholarly paper to base the blog post on.

    Returns:
    str: The generated blog content.
    """
    # Fetch the scholarly paper content
    scholarly_paper_content = fetch_scholarly_paper(paper_url)
    
    # Here you would implement the logic to convert the scholarly paper content
    # into a more accessible blog post format. This could involve summarizing
    # the content, extracting key points, and writing in a more casual style.
    
    # For demonstration purposes, we'll just return the content as is.
    # In a real application, you would use NLP techniques or an AI service.
    blog_post_content = scholarly_paper_content  # This should be replaced with actual conversion logic
    
    return blog_post_content
```