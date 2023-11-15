import os
from datetime import datetime
import requests

from local_settings import user_input, system_input
from helpers import get_screenshot
from output_browser import process_request_browser
from output_main import process_request_main


def main():

    # ################################################## #
    #
    # Validate parameters
    #
    # ################################################## #

    remote_url = user_input.get("url")
    wait = user_input.get("wait")
    output_main = user_input.get("output_main")
    output_browser = user_input.get("output_browser")

    desktop = system_input.get("desktop")

    # ################################################## #
    #
    # Create directories
    #
    # ################################################## #
    now = datetime.now()
    directory = now.strftime('%y%m%d_%H%M%S_%f')[:-3]
    directory_main = f"output/{directory}_portfolio"
    os.makedirs(directory_main)

    directory_screenshots = f"{directory_main}/screenshots"
    os.makedirs(directory_screenshots)

    # ################################################## #
    # 
    # Get screenshots
    #
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
    # 
    # Process Output Request - Main
    #
    # ################################################## #

    if output_main["request"] == True:

        result = process_request_main(output_main, system_input, directory_main, directory_screenshots)

        if result == 1:
            print("OUTPUT_MAIN request processed.")
        
    else:

        print("OUTPUT_MAIN not requested.")


    # ################################################## #
    # 
    # Process Output Request - Browser
    #
    # ################################################## #

    if output_browser["request"] == True:

        result = process_request_browser(output_browser, desktop, directory_main, directory_screenshots)

        if result == 1:
            print("OUTPUT_BROWSER request processed.")
    
    else:

        print("OUTPUT_BROWSER not requested.")


def get_url():

    while True:
        url = input("Enter url: ")
        try:
            response = requests.head(url)
            if response.status_code == 200:
                return url
            else:
                print("Invalid URL or URL is not accessible. Please try again.")
        except requests.exceptions.RequestException:
            print("Invalid URL or URL is not accessible. Please try again.")


if __name__ == "__main__":
    main()
