```python
import os
from datetime import datetime

def save_blog_to_file(blog_content, metadata, directory="blogs"):
    """
    Saves the generated blog content to a file, with an optional metadata header.

    Parameters:
    blog_content (str): The content of the blog post to be saved.
    metadata (dict): A dictionary containing metadata for the blog post.
    directory (str): The directory where the blog post will be saved.

    Returns:
    str: The path to the saved file.
    """

    # Ensure the directory exists
    os.makedirs(directory, exist_ok=True)

    # Create a filename based on the blog title or current timestamp
    filename = metadata.get("title", f"blog_post_{datetime.now().strftime('%Y%m%d%H%M%S')}.md")

    # Replace spaces with underscores and remove special characters from filename
    filename = "".join(char for char in filename if char.isalnum() or char in (' ', '_')).replace(' ', '_')

    # Define the full path
    file_path = os.path.join(directory, filename)

    # Write the blog content to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        # Optionally write metadata at the top of the file
        if metadata:
            for key, value in metadata.items():
                file.write(f"{key}: {value}\n")
            file.write("\n---\n\n")  # Markdown separator between metadata and content

        # Write the actual blog content
        file.write(blog_content)

    return file_path
```