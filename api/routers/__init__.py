"""
FastAPI routers handling OUTPUT requests.

This module provides FastAPI routers for different types of OUTPUT requests. 
Each router validates incoming requests through Pydantic models and directs 
them to appropriate service functions for processing.

Routers:
    router_main: Handle requests for OUTPUT_MAIN
    router_browser: Handle requests for OUTPUT_BROWSER
    router_mobiles: Handle requests for OUTPUT_MOBILES
    router_full: Handle requests for OUTPUT_FULL
    router_movie: Handle requests for OUTPUT_MOVIE
    router_screenshots: Handle requests for OUTPUT_SCREENSHOTS

For information about each OUTPUT type, refer to the documentation in README.md.
"""

from .endpoints import router_main
from .endpoints import router_browser
from .endpoints import router_mobiles
from .endpoints import router_full
from .endpoints import router_movie
from .endpoints import router_screenshots


# Define what should be available when using "from .routers import *"
__all__ = ['router_main',
           'router_browser',
           'router_mobiles',
           'router_full',
           'router_movie',
           'router_screenshots']
