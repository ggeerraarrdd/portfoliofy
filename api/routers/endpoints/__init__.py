"""
TD
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
