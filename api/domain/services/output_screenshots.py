"""
Process request for OUTPUT_SCREENSHOTS.
"""

# Local
from api.core.config import settings_devices
from api.core.utils import get_screenshot
from api.core.utils import get_screenshot_full
from api.domain.schemas import PortfoliofyRequest # Pydantic model for request validation










def process_request_screenshots(post: PortfoliofyRequest, request_type: str) -> bytes:
    """
    Process requests for OUTPUT_SCREENSHOTS.

    Captures webpage screenshot based on request type. For full-page requests, captures 
    entire scrollable content. For device requests, captures at device-specific viewport 
    dimensions.

    Args:
        post (PortfoliofyRequest): PortfoliofyRequest containing validated URL and timing params
            Request data is pre-validated via Pydantic PortfoliofyRequest model.
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
