```python
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs

def summarize_web_content(url):
    """
    Fetches the content from the provided URL and summarizes it into key points.

    Parameters:
    url (str): The URL of the web page to summarize.

    Returns:
    dict: A dictionary containing the original content and the summarized points.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code

        # Assuming the content is HTML, use BeautifulSoup to parse and extract text
        soup = BeautifulSoup(response.content, 'html.parser')
        text_content = ' '.join(soup.stripped_strings)

        # Placeholder for actual summarization logic
        # In a real scenario, this would involve NLP techniques to summarize the text
        summarized_content = text_content[:500] + '...'  # Mock summary

        return {
            'original_content': text_content,
            'summarized_content': summarized_content
        }

    except requests.RequestException as e:
        # Log the error and return an empty dictionary or raise an exception
        # depending on how you want to handle errors in your application
        print(f"An error occurred while fetching the web page: {e}")
        return {}

def generate_web_research_report(query):
    """
    Generates a web research report based on the specified query by summarizing content from the web.

    Parameters:
    query (str): The search query to perform web research on.

    Returns:
    list of dict: A list of dictionaries, each containing a URL and its summarized content.
    """
    # Placeholder for actual web search logic
    # In a real scenario, this would involve using an API or a web scraping technique
    # to search the web based on the query and retrieve relevant URLs
    search_results = ['https://example.com/article1', 'https://example.com/article2']  # Mock search results

    report = []
    for url in search_results:
        summary = summarize_web_content(url)
        report.append({
            'url': url,
            'summary': summary.get('summarized_content', 'Summary not available')
        })

    return report

# Example usage:
if __name__ == "__main__":
    query = "latest tech trends"
    research_report = generate_web_research_report(query)
    for item in research_report:
        print(f"URL: {item['url']}\nSummary: {item['summary']}\n")
```