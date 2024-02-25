```python
import requests
from bs4 import BeautifulSoup
from transformers import pipeline

def summarize_web_content(url):
    """
    Fetches web content from the given URL and summarizes it using a language model.

    Parameters:
    url (str): The URL of the web content to summarize.

    Returns:
    str: A summary of the web content.
    """
    # Fetch the content from the URL
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    html_content = response.text

    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')
    # Extract the main content from the page, you might need to adjust the selector
    main_content = soup.find('main')

    # Check if main content is found, otherwise use the whole HTML body
    text_content = main_content.get_text(strip=True) if main_content else soup.get_text(strip=True)

    # Initialize the HuggingFace summarization pipeline
    summarizer = pipeline("summarization")

    # Summarize the extracted text content
    summary = summarizer(text_content, max_length=130, min_length=30, do_sample=False)

    # Return the first summary (there might be multiple paragraphs)
    return summary[0]['summary_text']

# Example usage:
# summary = summarize_web_content("https://example.com/article")
# print(summary)
```