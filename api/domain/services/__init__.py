"""
Services module for processing different types of screenshot requests.

This module provides functions for processing screenshot requests through different 
output processors. Request validation is handled separately by Pydantic models at
the router/endpoint level.

Functions:
    process_request_main: Process OUTPUT_MAIN request
    process_request_browser: Process OUTPUT_BROWSER request  
    process_request_mobiles: Process OUTPUT_MOBILES request
    process_request_full: Process OUTPUT_FULL request
    process_request_movie: Process OUTPUT_MOVIE request
    process_request_screenshots: Process OUTPUT_SCREENSHOTS requests

For information about each OUTPUT type, refer to the documentation in README.md.
"""

from .output_main import process_request_main
from .output_browser import process_request_browser
from .output_mobiles import process_request_mobiles
from .output_full import process_request_full
from .output_movie import process_request_movie
from .output_screenshots import process_request_screenshots


# Define what should be available when using "from .services import *"
__all__ = ['process_request_main',
           'process_request_browser',
           'process_request_mobiles',
           'process_request_full',
           'process_request_movie',
           'process_request_screenshots']
