```python
import openai

def generate_blog_sections(prompt, max_tokens=150):
    """
    Generates structured sections for a blog post using GPT-3.

    Parameters:
    prompt (str): The prompt to send to GPT-3, usually containing the keywords or themes.
    max_tokens (int): The maximum number of tokens to generate.

    Returns:
    str: The structured sections for a blog post.
    """
    # OpenAI API key should be set in environment variables for security
    openai.api_key = os.getenv("OPENAI_API_KEY")

    try:
        # Call to OpenAI's completion endpoint with provided prompt and max tokens
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=max_tokens,
            n=1,
            stop=None,
            temperature=0.5
        )
        # Extracting the text from the response
        generated_text = response.choices[0].text.strip()
        return generated_text
    except openai.error.OpenAIError as e:
        # Log the error for debugging purposes
        print(f"An error occurred: {e}")
        return ""
    except Exception as e:
        # Catch any other exceptions and log them
        print(f"An unexpected error occurred: {e}")
        return ""
```