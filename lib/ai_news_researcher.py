```python
import requests
from bs4 import BeautifulSoup

def fetch_news_articles(query):
    """
    Fetches news articles related to the given query using web scraping.

    Parameters:
    query (str): The search query to find related news articles.

    Returns:
    list of dict: A list of dictionaries containing news articles, including title and link.
    """
    # Replace 'your_news_api_endpoint' with the actual news API endpoint you're using
    NEWS_API_ENDPOINT = 'https://your_news_api_endpoint'
    # Replace 'your_api_key' with your actual API key for the news service
    API_KEY = 'your_api_key'
    
    # Prepare the headers with the API key
    headers = {
        'Authorization': f'Bearer {API_KEY}'
    }
    
    # Prepare the search parameters
    params = {
        'q': query,
        'language': 'en',
        'sortBy': 'relevancy'
    }
    
    # Make the GET request to the news API
    response = requests.get(NEWS_API_ENDPOINT, headers=headers, params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response JSON
        articles = response.json().get('articles', [])
        # Extract the title and link of each article
        news_data = [{'title': article['title'], 'link': article['url']} for article in articles]
        return news_data
    else:
        # If the request failed, return an empty list
        return []

def summarize_article(url):
    """
    Summarizes the article content from the given URL using BeautifulSoup for scraping.

    Parameters:
    url (str): The URL of the article to summarize.

    Returns:
    str: A summary of the article.
    """
    # Send a GET request to the article URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')
        # Find all paragraph tags and concatenate their text
        paragraphs = soup.find_all('p')
        article_content = ' '.join([p.get_text() for p in paragraphs])
        # Here you would implement your summarization logic (e.g., using GPT-3 or another model)
        # For now, we'll just return the first 500 characters as a placeholder summary
        summary = article_content[:500]
        return summary
    else:
        # If the request failed, return an empty string
        return ""

# Example usage:
# news_articles = fetch_news_articles('latest tech news')
# for article in news_articles:
#     print(article['title'])
#     print(summarize_article(article['link']))
#     print('---')
```