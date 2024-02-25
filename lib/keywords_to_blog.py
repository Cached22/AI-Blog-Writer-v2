```python
import openai

def generate_blog_from_keywords(keywords):
    """
    Generates a blog post based on the specified keywords using GPT-3.

    Parameters:
    keywords (list of str): Keywords that the blog post should include.

    Returns:
    str: The generated blog content.
    """
    # Combine keywords into a prompt string
    prompt = f"Write a comprehensive blog post that includes the following keywords: {', '.join(keywords)}."

    # OpenAI API call to generate content based on the prompt
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=1500,
            temperature=0.7,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        blog_content = response.choices[0].text.strip()
        return blog_content
    except Exception as e:
        # Log the error and return an informative message
        print(f"An error occurred while generating blog content: {e}")
        return "Error: Unable to generate blog content at this time."

# Example usage:
# blog_post = generate_blog_from_keywords(["machine learning", "data science", "artificial intelligence"])
# print(blog_post)
```