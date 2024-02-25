```python
import re
import nltk
from nltk.corpus import stopwords
from collections import Counter

# Ensure that NLTK resources are downloaded
nltk.download('stopwords')

def get_tags(blog_content):
    """
    Extracts tags from the given blog content based on keyword frequency.

    Parameters:
    blog_content (str): The content of the blog post from which to extract tags.

    Returns:
    list of str: A list of suggested tags for the blog post.
    """

    # Remove punctuation and numbers
    text = re.sub(r'[^\w\s]', '', blog_content)
    text = re.sub(r'\d+', '', text)

    # Convert text to lowercase
    text = text.lower()

    # Tokenize the text
    words = text.split()

    # Remove stopwords
    words = [word for word in words if word not in stopwords.words('english')]

    # Get the frequency distribution of the remaining words
    word_freq = Counter(words)

    # Get the most common words as tags
    tags = [word for word, freq in word_freq.most_common(10)]

    return tags
```