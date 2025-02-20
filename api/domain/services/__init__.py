"""
TD
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
