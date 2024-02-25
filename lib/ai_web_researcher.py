```python
import requests
from bs4 import BeautifulSoup
import re

def fetch_web_content(url):
    """
    Fetches the content of a web page given a URL.

    Parameters:
    url (str): The URL of the web page to fetch.

    Returns:
    str: The text content of the web page.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        return str(e)

def summarize_web_content(content):
    """
    Summarizes the web content using a simple algorithm to extract the main points.

    Parameters:
    content (str): The content of the web page to summarize.

    Returns:
    str: A summary of the web content.
    """
    # This is a placeholder for the actual summarization logic
    # You might integrate an NLP model here to generate a summary
    sentences = re.split(r'(?<=[.!?]) +', content)
    summary = ' '.join(sentences[:5])  # Taking the first 5 sentences as a summary
    return summary

def perform_web_research(query):
    """
    Performs web research based on a query and summarizes the findings.

    Parameters:
    query (str): The search query to perform web research on.

    Returns:
    dict: A dictionary containing the original content and its summary.
    """
    # This is a placeholder for the actual search logic
    # You might use an API or a web scraping tool to get the content based on the query
    search_url = f"https://www.google.com/search?q={query}"
    content = fetch_web_content(search_url)
    summary = summarize_web_content(content)
    return {
        'query': query,
        'content': content,
        'summary': summary
    }

# Example usage:
# research_data = perform_web_research("Python programming")
# print(research_data['summary'])
```
