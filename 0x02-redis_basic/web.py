#!/usr/bin/env python3
"""
Caching request module
"""
import redis
import requests
from functools import wraps
from typing import Callable


def track_get_page(fn: Callable) -> Callable:
    """Decorator for get_page to cache responses and track access count"""
    @wraps(fn)
    def wrapper(url: str) -> str:
        """
        Wrapper that:
        - Checks whether a URL's data is cached
        - Tracks how many times get_page is called
        """
        client = redis.Redis()
        # Increment the call count for the URL
        client.incr(f'count:{url}')
        # Check if the page is cached
        cached_page = client.get(f'{url}')
        if cached_page:
            return cached_page.decode('utf-8')
        # If not cached, fetch the page and cache it with a 10-second expiration
        response = fn(url)
        client.setex(f'{url}', 10, response)
        return response
    return wrapper


@track_get_page
def get_page(url: str) -> str:
    """Makes an HTTP request to a given URL and returns the response content"""
    response = requests.get(url)
    return response.text
