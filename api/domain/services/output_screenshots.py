"""
Process request for OUTPUT_SCREENSHOTS.
"""

# Local
from api.core.config import settings_devices
from api.core.utils import get_screenshot
from api.core.utils import get_screenshot_full










def process_request_screenshots(post: dict, request_type: str) -> bytes:
    """
    Process requests for OUTPUT_SCREENSHOTS.

    Captures webpage screenshot based on request type. For full-page requests, captures 
    entire scrollable content. For device requests, captures at device-specific viewport 
    dimensions.

    Args:
        post (dict): Request parameters including (pre-validated with Pydantic):
            remote_url (str): URL to capture screenshot from
            wait (int): Wait time in seconds before capture
            format (str): Output image format
            doc_pad_h (int): Horizontal padding in pixels
            doc_pad_v (int): Vertical padding in pixels 
            doc_fill_color (str): Background color as hex
            base_stroke_color (str): Border color as hex
            base_fill_color (str): Base fill color as hex
        request_type (str): Type of screenshot to capture ('full' or device name)

    Returns:
        bytes: PNG image data of captured screenshot
    """
    device = settings_devices.get(request_type)

    if request_type == 'full':

        screenshot_full = get_screenshot_full(str(post['remote_url']), post['wait'])

        return screenshot_full

    screenshot = get_screenshot(str(post['remote_url']), post['wait'], device)

    return screenshot
