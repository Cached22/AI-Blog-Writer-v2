```python
import json
from keywords_to_blog import generate_blog_from_keywords

def combine_blog_and_keywords(keywords, additional_content):
    """
    Combines generated blog content with additional user-provided content based on keywords.

    Parameters:
    keywords (list of str): Keywords to generate the blog content.
    additional_content (str): Additional content to be appended to the generated blog content.

    Returns:
    dict: A dictionary containing the combined blog content and the keywords used.
    """
    # Generate initial blog content from keywords
    generated_content = generate_blog_from_keywords(keywords)

    # Combine the generated content with the additional content
    combined_content = f"{generated_content}\n\n{additional_content}"

    # Create a dictionary to store the combined content and keywords
    result = {
        'keywords': keywords,
        'combined_content': combined_content
    }

    # Return the result as a JSON string
    return json.dumps(result)

# Example usage:
# combined_blog = combine_blog_and_keywords(['python', 'web development'], 'This is additional content.')
# print(combined_blog)
```