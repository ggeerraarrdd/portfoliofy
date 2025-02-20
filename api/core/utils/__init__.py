"""
Screenshot and image processing utility functions for webpage screenshots.

This module provides functions for:
1. Taking screenshots of web pages using Selenium
2. Processing and combining images with various transformations
3. Managing temporary files and cleanup operations

Functions:
    get_screenshot: Capture fixed-size screenshot of a webpage
    get_screenshot_full: Capture full-page screenshot of a webpage
    get_screenshot_full_chrome: Helper for full page screenshot
    get_base: Create base PNG image from SVG
    get_overlay: Process screenshot into overlay image
    get_final_temp: Combine base and overlay images
    get_final: Add padding to final image
    cleanup: Remove temporary files
"""

from .utils import get_screenshot
from .utils import get_screenshot_full
from .utils import get_screenshot_full_chrome
from .utils import get_base
from .utils import get_overlay
from .utils import get_final_temp
from .utils import get_final
from .utils import cleanup


# Define what should be available when using "from .utils import *"
__all__ = ['get_screenshot',
           'get_screenshot_full',
           'get_screenshot_full_chrome',
           'get_base',
           'get_overlay',
           'get_final_temp',
           'get_final',
           'cleanup']
