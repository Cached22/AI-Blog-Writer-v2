```python
import markdown
from markdown.extensions.toc import TocExtension
import os

def convert_markdown_to_html(markdown_content):
    """
    Converts Markdown content to HTML.

    Parameters:
    markdown_content (str): The Markdown content to be converted.

    Returns:
    str: The converted HTML content.
    """
    # Use the markdown library to convert Markdown to HTML
    html_content = markdown.markdown(markdown_content, extensions=[TocExtension(permalink=True)])
    return html_content

def save_html_to_file(html_content, output_file='output.html'):
    """
    Saves the HTML content to a file.

    Parameters:
    html_content (str): The HTML content to be saved.
    output_file (str): The name of the file to save the HTML content to.

    Returns:
    None
    """
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    # Write the HTML content to the specified file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(html_content)

if __name__ == "__main__":
    # Example usage: Convert a Markdown file to HTML and save it
    with open('example.md', 'r', encoding='utf-8') as file:
        markdown_content = file.read()
    
    html_content = convert_markdown_to_html(markdown_content)
    save_html_to_file(html_content, 'example.html')
```