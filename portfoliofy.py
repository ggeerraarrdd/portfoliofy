import os
import shutil
from datetime import datetime
import requests
from local_settings import user_input, system_input
from helpers import get_screenshot
from output_browser import process_request_browser
from output_main import process_request_main
from output_mobiles import process_request_mobiles


def main():

    # ################################################## #
    # Validate parameters
    # ################################################## #
    remote_url = user_input.get("url")
    wait = user_input.get("wait")
    screenshots = user_input.get("screenshots")
    output_main = user_input.get("output_main")
    output_browser = user_input.get("output_browser")
    output_mobiles = user_input.get("output_mobiles")

    status_code = get_url(remote_url)

    if status_code not in (200, 301, 302):

        print("Invalid URL or URL is not accessible. Check 'url' parameter in local_settings.py.")

    else:

        print("Valid parameters.")

        # ################################################## #
        # Create directories
        # ################################################## #
        now = datetime.now()
        directory = now.strftime('%y%m%d_%H%M%S_%f')[:-3]
        directory_main = f"output/{directory}_portfolio"
        os.makedirs(directory_main)

        directory_screenshots = f"{directory_main}/screenshots"
        os.makedirs(directory_screenshots)

        # ################################################## #
        # Create screenshots
        # ################################################## #
        desktop = system_input.get("desktop")
        laptop = system_input.get("laptop")
        tablet = system_input.get("tablet")
        smartphone = system_input.get("smartphone")

        print(get_screenshot(remote_url, wait, directory_screenshots, desktop))
        print(get_screenshot(remote_url, wait, directory_screenshots, laptop))
        print(get_screenshot(remote_url, wait, directory_screenshots, tablet))
        print(get_screenshot(remote_url, wait, directory_screenshots, smartphone))

        # ################################################## #
        # Process Request - OUTPUT_MAIN
        # ################################################## #
        if output_main["request"] == True:

            result = process_request_main(
                output_main, system_input, directory_main, directory_screenshots)

            if result == 1:
                print("OUTPUT_MAIN request processed.")

        else:

            print("OUTPUT_MAIN not requested.")

        # ################################################## #
        # Process Request - OUPUT_BROWSER
        # ################################################## #
        if output_browser["request"] == True:

            result = process_request_browser(
                output_browser, desktop, directory_main, directory_screenshots)

            if result == 1:
                print("OUTPUT_BROWSER request processed.")

        else:

            print("OUTPUT_BROWSER not requested.")

        # ################################################## #
        # Process Request - OUPUT_MOBILES
        # ################################################## #
        if output_mobiles["request"] == True:

            result = process_request_mobiles(
                output_mobiles, system_input, directory_main, directory_screenshots)

            if result == 1:
                print("OUTPUT_MOBILES request processed.")

        else:

            print("OUTPUT_MOBILES not requested.")

        # ################################################## #
        # Process Request - OUPUT_SCREENSHOTS
        # ################################################## #
        if screenshots == False:

            shutil.rmtree(directory_screenshots)
            print("Screenshots directory deleted.")


def get_url(url):

    try:
        response = requests.head(url)
        if response.status_code == 200 or response.status_code == 302:
            return int(response.status_code)
        else:
            return 0

    except:
        return 0


if __name__ == "__main__":
    main()
