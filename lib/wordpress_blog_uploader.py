```python
import requests
from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo

def upload_to_wordpress(blog_content, metadata, wordpress_url, wordpress_username, wordpress_password):
    """
    Uploads a blog post to a WordPress site using the provided credentials.

    Parameters:
    blog_content (str): The content of the blog post to be uploaded.
    metadata (dict): A dictionary containing metadata for the blog post such as title and tags.
    wordpress_url (str): The URL of the WordPress site to upload the post to.
    wordpress_username (str): The username for the WordPress site.
    wordpress_password (str): The password for the WordPress site.

    Returns:
    dict: A dictionary containing the response from the WordPress site, including the ID of the new post.
    """
    
    # Create a new WordPress post object
    post = WordPressPost()
    post.title = metadata.get('title')
    post.content = blog_content
    post.terms_names = {
        'post_tag': metadata.get('tags', []),
        'category': metadata.get('categories', [])
    }
    
    # Connect to the WordPress site
    wp_client = Client(wordpress_url + '/xmlrpc.php', wordpress_username, wordpress_password)
    
    # Upload the post
    post_id = wp_client.call(NewPost(post))
    
    # Return the response
    return {'success': True, 'post_id': post_id}
```