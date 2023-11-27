import os
import shutil
from datetime import datetime
from local_settings import user_input, system_input
from helpers import get_validation, get_screenshot, get_screenshot_full
from output_browser import process_request_browser
from output_main import process_request_main
from output_mobiles import process_request_mobiles
from output_full import process_request_full
from output_video import process_request_video


def main():

    # ################################################## #
    # Validate parameters
    # ################################################## #

    print("PORTFOLIOFY - START")
    print("Validating parameters...")

    message = get_validation(user_input)

    if len(message) > 0:
        print("¦— Failed")
        print(message.rstrip("\n"))
        print("¦— See documentation at https://github.com/ggeerraarrdd/portfoliofy")

    else:
        print("¦— Passed")

        remote_url = user_input.get("url")
        wait = user_input.get("wait")

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
        full = system_input.get("full")

        print("Taking screenshots...")
        
        result = get_screenshot(remote_url, wait, directory_screenshots, desktop)
        if result == 1:
            print("¦— Desktop created")

        result = get_screenshot(remote_url, wait, directory_screenshots, laptop)
        if result == 1:
            print("¦— Laptop created")

        result = get_screenshot(remote_url, wait, directory_screenshots, tablet)
        if result == 1:
            print("¦— Tablet created")

        result = get_screenshot(remote_url, wait, directory_screenshots, smartphone)
        if result == 1:
            print("¦— Smarthphone created")

        result = get_screenshot_full(remote_url, wait, directory_screenshots, full)
        if result == 1:
            print("¦— Full-page created")

        print("¦— Done")

        # ################################################## #
        # Process Request - OUTPUT_MAIN
        # ################################################## #
        print("output_main")
        print("¦— Processing...")

        output_main = user_input.get("output_main")

        if output_main["request"] == True:
            result = process_request_main(output_main, system_input, directory_main, directory_screenshots)

            if result == 1:
                print("¦— Done")

        else:
            print("¦— Not requested")
            print("¦— Canceled")

        # ################################################## #
        # Process Request - OUPUT_BROWSER
        # ################################################## #
        print("output_browser")
        print("¦— Processing...")
        
        output_browser = user_input.get("output_browser")

        if output_browser["request"] == True:
            result = process_request_browser(output_browser, desktop, directory_main, directory_screenshots)

            if result == 1:
                print("¦— Done")

        else:
            print("¦— Not requested")
            print("¦— Canceled")

        # ################################################## #
        # Process Request - OUPUT_MOBILES
        # ################################################## #
        print("output_mobiles")
        print("¦— Processing...")
        
        output_mobiles = user_input.get("output_mobiles")

        if output_mobiles["request"] == True:
            result = process_request_mobiles(output_mobiles, system_input, directory_main, directory_screenshots)

            if result == 1:
                print("¦— Done")

        else:
            print("¦— Not requested")
            print("¦— Canceled")

        # ################################################## #
        # Process Request - OUPUT_FULL
        # ################################################## #
        print("output_full")
        print("¦— Processing...")
        
        output_full = user_input.get("output_full")

        if output_full["request"] == True:
            result = process_request_full(output_full, full, directory_main, directory_screenshots)

            if result == 1:
                print("¦— Done")

        else:
            print("¦— Not requested")
            print("¦— Canceled")

        # ################################################## #
        # Process Request - OUPUT_VIDEO
        # ################################################## #
        print("output_video")
        print("¦— Processing...")
        
        output_video = user_input.get("output_video")
        video = system_input.get("video")
            
        if output_video["request"] == True:
            result = process_request_video(output_video, video, directory_main, directory_screenshots)

            if result == 1:
                print("¦— Done")

        else:
            print("¦— Not requested")
            print("¦— Canceled")

        # ################################################## #
        # Process Request - OUPUT_SCREENSHOTS
        # ################################################## #
        print("output_screenshots")
        print("¦— Processing...")

        screenshots = user_input.get("screenshots")

        if screenshots == False:
            shutil.rmtree(directory_screenshots)
            print("¦— Not requested")
            print("¦— Canceled")

        else:
            print("¦— Done")
    
    print("PORTFOLIOFY - END")


if __name__ == "__main__":
    main()
