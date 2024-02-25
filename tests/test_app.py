```python
import pytest
from app import app as flask_app

@pytest.fixture
def app():
    """
    Instance of Main Flask app for testing.
    """
    yield flask_app

@pytest.fixture
def client(app):
    """
    Setup an app client, this gets executed for each test function.
    """
    return app.test_client()

def test_homepage(client):
    """
    Test that the homepage is accessible without login.
    """
    response = client.get("/")
    assert response.status_code == 200

def test_blog_generation_page(client):
    """
    Test the blog generation page loads correctly.
    """
    response = client.get("/blog_generation")
    assert response.status_code == 200
    assert b"Keyword/Theme Input Section" in response.data

def test_research_page(client):
    """
    Test the research page loads correctly.
    """
    response = client.get("/research")
    assert response.status_code == 200
    assert b"Research Input Section" in response.data

def test_seo_analysis_page(client):
    """
    Test the SEO analysis page loads correctly.
    """
    response = client.get("/seo_analysis")
    assert response.status_code == 200
    assert b"Analysis Input Section" in response.data

def test_metadata_postprocessing_page(client):
    """
    Test the metadata and postprocessing page loads correctly.
    """
    response = client.get("/metadata_postprocessing")
    assert response.status_code == 200
    assert b"Metadata Input Section" in response.data

# Additional tests can be added to cover more functionalities
```