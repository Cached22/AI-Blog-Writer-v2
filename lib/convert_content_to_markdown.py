```python
import markdown
import os

def convert_content_to_markdown(content, output_file='output.md'):
    """
    Converts the provided content to Markdown format and saves it to a file.

    Parameters:
    content (str): The content to be converted to Markdown.
    output_file (str): The filename for the output Markdown file.

    Returns:
    bool: True if the file was saved successfully, False otherwise.
    """
    try:
        # Convert the content to Markdown
        md_content = markdown.markdown(content)

        # Ensure the output directory exists
        os.makedirs(os.path.dirname(output_file), exist_ok=True)

        # Write the Markdown content to the file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(md_content)

        return True
    except Exception as e:
        # Log the exception if any
        print(f"An error occurred while converting content to Markdown: {e}")
        return False
```