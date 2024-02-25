```python
import pytrends
from pytrends.request import TrendReq
import pandas as pd

def fetch_google_trends(keywords, timeframe='today 5-y', geo='', language='en-US'):
    """
    Fetches Google Trends data for the specified keywords.

    Parameters:
    keywords (list of str): Keywords to search for trends.
    timeframe (str): Timeframe for fetching trends data, defaults to 'today 5-y'.
    geo (str): Geographical area for trends data, defaults to empty (worldwide).
    language (str): Language for trends data, defaults to 'en-US'.

    Returns:
    DataFrame: A pandas DataFrame containing the trends data.
    """

    # Initialize pytrends request
    pytrends = TrendReq(hl=language, tz=360)

    # Build the payload with the provided parameters
    pytrends.build_payload(keywords, timeframe=timeframe, geo=geo)

    # Fetch interest over time
    trends_data = pytrends.interest_over_time()

    # Remove the 'isPartial' column
    if 'isPartial' in trends_data.columns:
        trends_data = trends_data.drop(columns='isPartial')

    return trends_data

def get_related_queries(keywords, language='en-US'):
    """
    Fetches related queries from Google Trends for the specified keywords.

    Parameters:
    keywords (list of str): Keywords to search for related queries.
    language (str): Language for trends data, defaults to 'en-US'.

    Returns:
    dict: A dictionary containing related queries for each provided keyword.
    """

    # Initialize pytrends request
    pytrends = TrendReq(hl=language, tz=360)

    # Build the payload with the provided parameters
    pytrends.build_payload(keywords)

    # Fetch related queries
    related_queries = pytrends.related_queries()

    return related_queries

def get_trending_searches(language='en-US'):
    """
    Fetches currently trending searches from Google Trends.

    Parameters:
    language (str): Language for trends data, defaults to 'en-US'.

    Returns:
    DataFrame: A pandas DataFrame containing currently trending searches.
    """

    # Initialize pytrends request
    pytrends = TrendReq(hl=language, tz=360)

    # Fetch trending searches
    trending_searches = pytrends.trending_searches()

    return trending_searches
```