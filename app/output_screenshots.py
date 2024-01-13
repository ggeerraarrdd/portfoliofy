import os
from datetime import datetime
from app.settings import settings_devices
from app.helpers import get_screenshot, get_screenshot_full


def process_request_screenshots(post, type):

    # Get system settings for desktop
    device = settings_devices.get(type)

    # Create directory
    now = datetime.now()
    directory = now.strftime('%y%m%d_%H%M%S_%f')[:-3]
    directory = f"app/output/{directory}_screenshots_{type}"
    os.makedirs(directory)

    if type == "full":

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

