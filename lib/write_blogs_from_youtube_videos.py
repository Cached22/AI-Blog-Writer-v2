```python
import requests
from bs4 import BeautifulSoup
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from lib.keywords_to_blog import generate_blog_from_keywords

# Function to extract video titles and descriptions from YouTube based on keywords
def get_youtube_content(api_key, keywords):
    """
    Fetches video titles and descriptions from YouTube using the provided keywords.

    Parameters:
    api_key (str): The API key for accessing the YouTube Data API.
    keywords (list of str): Keywords to search for on YouTube.

    Returns:
    list of tuples: A list of tuples containing video titles and descriptions.
    """
    youtube = build('youtube', 'v3', developerKey=api_key)
    search_response = youtube.search().list(
        q=keywords,
        part='id,snippet',
        maxResults=10
    ).execute()

    videos = []
    for search_result in search_response.get('items', []):
        if search_result['id']['kind'] == 'youtube#video':
            title = search_result['snippet']['title']
            description = search_result['snippet']['description']
            videos.append((title, description))
    
    return videos

# Function to generate blog posts from YouTube video content
def write_blogs_from_youtube_videos(api_key, keywords):
    """
    Generates blog posts based on YouTube video titles and descriptions.

    Parameters:
    api_key (str): The API key for accessing the YouTube Data API.
    keywords (list of str): Keywords to generate the blog content from.

    Returns:
    list of str: A list of generated blog posts.
    """
    try:
        video_content = get_youtube_content(api_key, keywords)
        blog_posts = []
        for title, description in video_content:
            # Combine title and description as input for the blog generation
            combined_content = f"{title}\n{description}"
            # Generate blog post from the combined content
            blog_post = generate_blog_from_keywords(combined_content)
            blog_posts.append(blog_post)
        return blog_posts
    except HttpError as e:
        print(f"An HTTP error {e.resp.status} occurred: {e.content}")
        return []

# Replace 'YOUR_API_KEY' with your actual YouTube Data API key and 'your_keywords' with your target keywords
# Example usage:
# blogs = write_blogs_from_youtube_videos('YOUR_API_KEY', ['your_keywords'])
# print(blogs)
```