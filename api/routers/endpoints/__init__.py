"""
Endpoints module for FastAPI routers handling OUTPUT requests.

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

from .main import router as router_main
from .browser import router as router_browser
from .mobiles import router as router_mobiles
from .full import router as router_full
from .movie import router as router_movie
from .screenshots import router as router_screenshots


# Define what should be available when using "from .endpoints import *"
__all__ = ['router_main',
           'router_browser',
           'router_mobiles',
           'router_full',
           'router_movie',
           'router_screenshots']
