"""
TD
"""

# Python Standard Libraries
import os
from datetime import datetime

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

    # Create directory
    now = datetime.now()
    directory = now.strftime('%y%m%d_%H%M%S_%f')[:-3]
    directory = f"api/output/{directory}_screenshots_{request_type}"
    os.makedirs(directory)

    if request_type == "full":

        # Get screenshot
        get_screenshot_full(str(post["remote_url"]),
                            post["wait"],
                            directory,
                            device)

        return f"{directory}/{device['filename_large']}"

    else:

        # Get screenshot
        get_screenshot(str(post["remote_url"]),
                    post["wait"],
                    directory,
                    device)

        return f"{directory}/{device['filename_large']}"
