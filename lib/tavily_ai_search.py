```python
import requests
from bs4 import BeautifulSoup

def perform_web_search(query):
    """
    Perform a web search using Tavily AI search capabilities and return summarized results.

    Parameters:
    query (str): The search query string.

    Returns:
    list of dict: A list of dictionaries containing the title and summary of each search result.
    """
    # Replace 'YOUR_TAVILY_API_KEY' with your actual Tavily AI API key
    api_key = 'YOUR_TAVILY_API_KEY'
    search_url = f'https://api.tavily.com/search?q={query}&api_key={api_key}'

    try:
        response = requests.get(search_url)
        response.raise_for_status()  # Raise an HTTPError if the HTTP request returned an unsuccessful status code

        # Parse the response content to extract titles and summaries
        results = []
        soup = BeautifulSoup(response.content, 'html.parser')
        search_items = soup.find_all('div', class_='search-item')

        for item in search_items:
            title = item.find('h2', class_='search-item-title').text.strip()
            summary = item.find('p', class_='search-item-summary').text.strip()
            results.append({'title': title, 'summary': summary})

        return results

    except requests.exceptions.RequestException as e:
        # Log the error and return an empty list if an exception occurs
        print(f'An error occurred while performing the web search: {e}')
        return []

# Example usage:
# search_results = perform_web_search('latest tech trends')
# for result in search_results:
#     print(result['title'], result['summary'])
```