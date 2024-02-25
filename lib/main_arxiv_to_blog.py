```python
import requests
from bs4 import BeautifulSoup
from lib.gpt_blog_sections import generate_blog_sections
from lib.gpt_summarize_web_content import summarize_web_content

def fetch_arxiv_paper(paper_id):
    """
    Fetches an academic paper from arXiv given a paper ID.

    Parameters:
    paper_id (str): The arXiv ID of the paper to fetch.

    Returns:
    str: The content of the academic paper.
    """
    arxiv_url = f'http://arxiv.org/abs/{paper_id}'
    response = requests.get(arxiv_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        abstract = soup.find('blockquote', class_='abstract').text
        return abstract.strip()
    else:
        raise Exception(f"Failed to fetch arXiv paper: HTTP {response.status_code}")

def main_arxiv_to_blog(paper_id, sections=None):
    """
    Generates a blog post based on an arXiv academic paper.

    Parameters:
    paper_id (str): The arXiv ID of the paper to generate the blog post from.
    sections (list of str, optional): List of sections to include in the blog post.

    Returns:
    str: The generated blog content.
    """
    try:
        paper_content = fetch_arxiv_paper(paper_id)
        summarized_content = summarize_web_content(paper_content)
        blog_post = generate_blog_sections(summarized_content, sections)
        return blog_post
    except Exception as e:
        # Log the error for debugging purposes
        print(f"Error generating blog post from arXiv paper: {e}")
        # Re-raise the exception to be handled further up the call stack
        raise

# Example usage:
# paper_id = '2104.00068' # Replace with actual arXiv paper ID
# sections = ['Introduction', 'Main Findings', 'Conclusion']
# blog_post = main_arxiv_to_blog(paper_id, sections)
# print(blog_post)
```