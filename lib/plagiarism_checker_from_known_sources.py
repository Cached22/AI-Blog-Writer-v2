```python
import difflib
import requests
from bs4 import BeautifulSoup

def check_for_plagiarism(content, known_sources):
    """
    Checks the provided content against a list of known sources for potential plagiarism.

    Parameters:
    content (str): The blog content to check for plagiarism.
    known_sources (list of str): URLs of known sources to check against.

    Returns:
    dict: A dictionary containing plagiarism results with 'is_plagiarized' flag and 'details'.
    """
    plagiarism_results = {
        'is_plagiarized': False,
        'details': []
    }

    for source in known_sources:
        try:
            response = requests.get(source)
            response.raise_for_status()  # Raise an HTTPError if the HTTP request returned an unsuccessful status code
            soup = BeautifulSoup(response.content, 'html.parser')
            text_from_source = soup.get_text()
            similarity = difflib.SequenceMatcher(None, content, text_from_source).ratio()

            if similarity > 0.5:  # Threshold for considering content as plagiarized
                plagiarism_results['is_plagiarized'] = True
                plagiarism_results['details'].append({
                    'source': source,
                    'similarity': similarity
                })

        except requests.RequestException as e:
            print(f"An error occurred while fetching data from {source}: {e}")

    return plagiarism_results

# Example usage:
# content_to_check = "This is a sample content to check for plagiarism."
# known_sources_list = ["http://example.com/source1", "http://example.com/source2"]
# result = check_for_plagiarism(content_to_check, known_sources_list)
# print(result)
```