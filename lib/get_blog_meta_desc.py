```python
import re
from textblob import TextBlob

def get_blog_meta_desc(blog_content):
    """
    Extracts or generates a meta description for a blog post based on its content.

    Parameters:
    blog_content (str): The full text content of the blog post.

    Returns:
    str: A meta description suitable for use in HTML metadata.
    """
    # Clean the blog content to remove any HTML tags and unnecessary whitespace
    clean_content = re.sub('<[^<]+?>', '', blog_content).strip()
    
    # Use TextBlob to extract the first few sentences that can summarize the blog post
    blob = TextBlob(clean_content)
    sentences = blob.sentences
    
    # Aim for a meta description length of around 150-160 characters
    meta_desc = ''
    for sentence in sentences:
        if len(meta_desc) + len(sentence) <= 160:
            meta_desc += str(sentence) + ' '
        else:
            break
    
    # If the meta description is too short, use the first sentence regardless of length
    if len(meta_desc) < 50:
        meta_desc = str(sentences[0])
    
    return meta_desc.strip()

# Example usage:
# blog_content = "Your full blog content here..."
# print(get_blog_meta_desc(blog_content))
```