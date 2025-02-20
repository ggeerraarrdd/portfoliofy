"""
TD
"""

# Local
from api.core.config import settings_devices
from api.core.utils import get_screenshot
from api.core.utils import get_screenshot_full










def process_request_screenshots(post, request_type):
    """
    TD
    """
    # Get system settings for desktop
    device = settings_devices.get(request_type)

    if request_type == "full":

        # Get screenshot
        screenshot_full = get_screenshot_full(str(post["remote_url"]),
                                              post["wait"])

        return screenshot_full

    else:

        # Get screenshot
        screenshot = get_screenshot(str(post["remote_url"]),
                                    post["wait"],
                                    device)

        return screenshot
