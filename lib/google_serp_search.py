```python
import requests
from bs4 import BeautifulSoup

def fetch_google_serp_results(query, num_results=10):
    """
    Fetches search results from Google SERP based on the given query.

    Parameters:
    query (str): The search query to fetch results for.
    num_results (int): The number of search results to fetch.

    Returns:
    list of dict: A list of dictionaries containing the title and link of each search result.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    encoded_query = query.replace(' ', '+')
    url = f"https://www.google.com/search?q={encoded_query}&num={num_results}"

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Error fetching search results: {response.status_code}")

    soup = BeautifulSoup(response.text, 'html.parser')
    result_block = soup.find_all('div', attrs={'class': 'g'})

    results = []
    for result in result_block:
        link = result.find('a', href=True)
        title = result.find('h3')
        if link and title:
            results.append({
                'title': title.get_text(),
                'link': link['href']
            })

    return results

if __name__ == "__main__":
    # Example usage:
    try:
        query = "Python programming blog"
        search_results = fetch_google_serp_results(query)
        for result in search_results:
            print(f"Title: {result['title']}, Link: {result['link']}")
    except Exception as e:
        print(f"An error occurred: {e}")
```