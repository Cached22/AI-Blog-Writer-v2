```python
import re
from textblob import TextBlob

def proofread_blog_content(blog_content):
    """
    Proofreads the blog content, checking for grammatical errors and providing suggestions for corrections.

    Parameters:
    blog_content (str): The blog content to be proofread.

    Returns:
    dict: A dictionary containing the original content, a list of grammatical errors found, and suggested corrections.
    """
    # Initialize an empty list to hold any errors found
    errors = []
    # Split the content into sentences for processing
    sentences = re.split(r'(?<=[.!?]) +', blog_content)
    
    # Check each sentence for grammatical errors
    for sentence in sentences:
        # Create a TextBlob object for grammatical analysis
        blob = TextBlob(sentence)
        # Correct the sentence using TextBlob's correct method
        corrected = str(blob.correct())
        # If the corrected sentence is different, log the error and suggestion
        if sentence != corrected:
            errors.append({'original': sentence, 'suggested': corrected})
    
    # Return the original content along with any errors and suggestions
    return {
        'original_content': blog_content,
        'errors': errors,
        'corrected_content': " ".join([e['suggested'] for e in errors])
    }

# Example usage:
# blog_content = "This is a sample blogg content with some erors."
# proofread_result = proofread_blog_content(blog_content)
# print(proofread_result)
```
