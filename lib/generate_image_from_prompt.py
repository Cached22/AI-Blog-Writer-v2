```python
import openai
from flask import current_app as app

def generate_image_from_prompt(prompt, model="text-to-image-model", n=1):
    """
    Generates an image based on the specified text prompt using OpenAI's API.

    Parameters:
    prompt (str): The text prompt to generate the image from.
    model (str): The model to use for image generation. Default is "text-to-image-model".
    n (int): The number of images to generate. Default is 1.

    Returns:
    list of str: The URLs of the generated images.
    """
    try:
        # Ensure the OpenAI API key is set
        if not app.config.get('OPENAI_API_KEY'):
            raise ValueError("OpenAI API key is not configured.")

        # Set up the OpenAI API key
        openai.api_key = app.config['OPENAI_API_KEY']

        # Call the OpenAI API to generate the image
        response = openai.Image.create(prompt=prompt, n=n, model=model)

        # Extract the image URLs from the response
        image_urls = [data['url'] for data in response['data']]

        return image_urls

    except Exception as e:
        # Log the error for debugging
        app.logger.error(f"Error generating image from prompt: {str(e)}")
        # Return an empty list if there's an error
        return []
```