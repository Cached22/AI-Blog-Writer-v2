```python
import requests
from bs4 import BeautifulSoup

def perform_online_research(query):
    """
    Performs online research by querying search engines and scraping content.

    Parameters:
    query (str): The search query for conducting online research.

    Returns:
    dict: A dictionary containing the summarized results and detailed content.
    """
    # Define the search URL
    search_url = f"https://www.google.com/search?q={query}"
    
    # Send a request to the search engine
    response = requests.get(search_url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract relevant information from the search results
        # This is a simplified example, actual implementation may require more complex parsing
        results = soup.find_all('div', class_='result')
        summarized_results = [result.text for result in results]
        
        # Detailed content can be extracted and processed further if needed
        detailed_content = '...'

        # Return the summarized results and detailed content
        return {
            'summarized_results': summarized_results,
            'detailed_content': detailed_content
        }
    else:
        # Handle request errors
        return {
            'error': f"Failed to retrieve search results, status code: {response.status_code}"
        }

# Example usage:
# research_data = perform_online_research("latest tech trends")
# print(research_data['summarized_results'])
```