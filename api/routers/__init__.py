"""
TD
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
