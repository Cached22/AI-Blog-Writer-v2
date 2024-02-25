```python
import requests
from bs4 import BeautifulSoup
import scholarly

def fetch_arxiv_papers(query):
    """
    Fetches a list of papers from arXiv based on the specified query.

    Parameters:
    query (str): The search query to find relevant academic papers on arXiv.

    Returns:
    list of dict: A list of dictionaries containing paper information such as title, authors, summary, and link.
    """
    search_query = scholarly.search_pubs(query)
    papers = []
    try:
        for paper in search_query:
            paper_info = paper.bib
            papers.append({
                'title': paper_info.get('title', 'No title available'),
                'authors': paper_info.get('author', 'No authors available'),
                'summary': paper_info.get('abstract', 'No summary available'),
                'link': paper_info.get('eprint', 'No link available')
            })
            if len(papers) >= 10:  # Limit to top 10 results
                break
    except Exception as e:
        print(f"An error occurred while fetching papers: {e}")
    return papers

def get_paper_details(url):
    """
    Retrieves the details of a paper given its arXiv URL.

    Parameters:
    url (str): The URL of the arXiv paper.

    Returns:
    dict: A dictionary containing detailed information about the paper.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find('h1', class_='title').text.replace('Title:', '').strip()
        authors = soup.find('div', class_='authors').text.replace('Authors:', '').strip()
        summary = soup.find('blockquote', class_='abstract').text.replace('Abstract:', '').strip()
        return {
            'title': title,
            'authors': authors,
            'summary': summary,
            'link': url
        }
    except requests.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as e:
        print(f"An error occurred while getting paper details: {e}")
    return {}

# Example usage:
# papers = fetch_arxiv_papers('deep learning')
# for paper in papers:
#     print(paper)
# detailed_paper = get_paper_details(papers[0]['link'])
# print(detailed_paper)
```