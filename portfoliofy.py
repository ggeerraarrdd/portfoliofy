import os

from selenium import webdriver
from PIL import Image
from time import sleep
from datetime import datetime
import requests
from selenium.webdriver.chrome.options import Options


def main():

    # Get url from user
    remote_url = get_url()

    # remote_url = "https://cs50.harvard.edu/python/2022/"
    
    # Ensure enough time for page to render
    wait = 2

    # Create new directory
    now = datetime.now()
    directory = now.strftime('%y%m%d_%H%M%S_%f')[:-3]
    directory_path = f"output/{directory}_screenshots"
    os.makedirs(directory_path)

    # ################################################## #
    # Desktop
    # ################################################## #
    
    # Desktop - Variables - Large
    file_name_large = "desktop_large.png"
    large_width = 2160
    large_height = 1360
    # Desktop - Variables - Medium
    file_name_medium = "desktop_medium.png"
    medium_width = 2048
    medium_height = None
    medium_height_crop = 1152
    # Desktop - Variables - Small
    file_name_small = "desktop_small.png"
    small_width = 1920
    small_height = None
    small_height_crop = 1080

    # Desktop - Large version - Original screenshot
    result = get_screenshot(remote_url, wait, large_width, large_height, directory_path, file_name_large)
    print(result)

    # Desktop - Medium version - Resized and cropped from original screenshot
    result = get_screenshot_resized(directory_path, file_name_large, file_name_medium, medium_width, medium_height_crop)
    print(result)

    # Desktop - Medium version - Placed on top of template image for desktop browser
    base_image_devices = "output/devices_desktop.png"
    base_image_devices_final = "devices_desktop_final.png" 
    lat = 628
    lng = 625
    desktop_browser_image = get_screenshot_resized_overlaid(base_image_devices, f"{directory_path}/{file_name_medium}", lat, lng, directory_path, base_image_devices_final)
    print(f"{base_image_devices_final} has been created")

    # Desktop - Small version - Resized and cropped from original screenshot
    result = get_screenshot_resized(directory_path, file_name_large, file_name_small, small_width, small_height_crop)
    print(result)

    # Desktop - Small version - Placed on top of template image for all devices
    base_image_devices = "output/devices_layer_1.png"
    base_image_devices_final = "devices_final.png" 
    lat = 1352
    lng = 782
    new_base_image_devices = get_screenshot_resized_overlaid(base_image_devices, f"{directory_path}/{file_name_small}", lat, lng, directory_path, base_image_devices_final)
    print(f"{new_base_image_devices} has been created")

    # Laptop - Cleanup
    print(cleanup(directory_path, file_name_large))
    print(cleanup(directory_path, file_name_medium))
    print(cleanup(directory_path, file_name_small))

    # ################################################## #
    # Laptop
    # ################################################## #

    # Laptop - Variables
    file_name_large = "laptop_large.png"
    large_width = 1440
    large_height = 900
    file_name_small = "laptop_small.png"
    small_width = 1280
    small_height = None
    small_height_crop = 720

    # Laptop - Large version - Original screenshot
    result = get_screenshot(remote_url, wait, large_width, large_height, directory_path, file_name_large)
    print(result)

    # Laptop - Small version - Resized and cropped from original screenshot
    result = get_screenshot_resized(directory_path, file_name_large, file_name_small, small_width, small_height_crop)
    print(result)

    # Laptop - Small version - Devices collage
    # Laptop - Small version - Devices collage - Add resized screenshot to base layer 2
    base_layer_laptop_small = "output/devices_layer_2.png"
    base_layer_laptop_small_temp = "base_layer_2_temp.png"
    lat = 34
    lng = 34
    new_base_layer_2 = get_screenshot_resized_overlaid(base_layer_laptop_small, f"{directory_path}/{file_name_small}", lat, lng, directory_path, base_layer_laptop_small_temp)
    # Laptop - Small version - Devices collage - Add updated base layer 2 to output/{directory_path}/devices_final.png
    base = f"{directory_path}/{base_image_devices_final}"
    lat = 530
    lng = 1410
    new_base_image_devices = get_screenshot_resized_overlaid(base, f"{directory_path}/{base_layer_laptop_small_temp}", lat, lng, directory_path, base_image_devices_final)
    # Laptop - Small version - Devices collage - Remove base_layer_2_temp.png 
    os.remove(f"{directory_path}/{base_layer_laptop_small_temp}")
    print(f"{new_base_image_devices} has been updated")

    # Laptop - Cleanup
    print(cleanup(directory_path, file_name_large))
    print(cleanup(directory_path, file_name_medium))
    print(cleanup(directory_path, file_name_small))

    # ################################################## #
    # Tablet
    # ################################################## #

    # Tablet - Variables
    file_name_large = "tablet_large.png"
    large_width = 768
    large_height = 1024
    file_name_small = "tablet_small.png"
    small_width = 600
    small_height = None
    small_height_crop = 800

    # Tablet - Large version - Original screenshot
    result = get_screenshot(remote_url, wait, large_width, large_height, directory_path, file_name_large)
    print(result)

    # Tablet - Small version - Resized and cropped from original screenshot
    result = get_screenshot_resized(directory_path, file_name_large, file_name_small, small_width, small_height_crop)
    print(result)

    # Tablet - Small version - Devices collage
    # Tablet - Small version - Devices collage - Add resized screenshot to base layer 3
    base_layer_tablet_small = "output/devices_layer_3.png"
    base_layer_tablet_small_temp = "base_layer_3_temp.png"
    lat = 34
    lng = 34
    new_base_layer_3 = get_screenshot_resized_overlaid(base_layer_tablet_small, f"{directory_path}/{file_name_small}", lat, lng, directory_path, base_layer_tablet_small_temp)
    # Tablet - Small version - Devices collage - Add updated base layer 3 to output/{directory_path}/devices_final.png
    base = f"{directory_path}/{base_image_devices_final}"
    lat = 2940
    lng = 1360
    new_base_image_devices = get_screenshot_resized_overlaid(base, f"{directory_path}/{base_layer_tablet_small_temp}", lat, lng, directory_path, base_image_devices_final)
    # Tablet - Small version - Devices collage - Remove base_layer_3_temp.png 
    os.remove(f"{directory_path}/{base_layer_tablet_small_temp}")
    print(f"{new_base_image_devices} has been updated")

    # Tablet - Cleanup
    print(cleanup(directory_path, file_name_large))
    print(cleanup(directory_path, file_name_medium))
    print(cleanup(directory_path, file_name_small))

    # ################################################## #
    # Mobile
    # ################################################## #

    # Mobile - Variables
    file_name_large = "mobie_large.png"
    large_width = 430
    large_height = 932
    file_name_small = "mobie_small.png"
    small_width = 230
    small_height = None
    small_height_crop = 490

    # Mobile - Large version - Original screenshot
    result = get_screenshot(remote_url, wait, large_width, large_height, directory_path, file_name_large)
    print(result)

    # Mobile - Small version - Resized and cropped from original screenshot
    result = get_screenshot_resized(directory_path, file_name_large, file_name_small, small_width, small_height_crop)
    print(result)

    # Mobile - Small version - Devices collage
    # Mobile - Small version - Devices collage - Add resized screenshot to base layer 4
    base_layer_mobile_small = "output/devices_layer_4.png"
    base_layer_mobile_small_temp = "base_layer_4_temp.png"
    lat = 24
    lng = 24
    new_base_layer_4 = get_screenshot_resized_overlaid(base_layer_mobile_small, f"{directory_path}/{file_name_small}", lat, lng, directory_path, base_layer_mobile_small_temp)
    # Mobile - Small version - Devices collage - Add updated base layer 4 to output/{directory_path}/devices_final.png
    base = f"{directory_path}/{base_image_devices_final}"
    lat = 3430
    lng = 1690
    new_base_image_devices = get_screenshot_resized_overlaid(base, f"{directory_path}/{base_layer_mobile_small_temp}", lat, lng, directory_path, base_image_devices_final)
    # Mobile - Small version - Devices collage - Remove base_layer_4_temp.png 
    os.remove(f"{directory_path}/{base_layer_mobile_small_temp}")
    print(f"{new_base_image_devices} has been updated")

    # Mobile - Cleanup
    print(cleanup(directory_path, file_name_large))
    print(cleanup(directory_path, file_name_medium))
    print(cleanup(directory_path, file_name_small))

    return 1


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


def get_screenshot(remote_url, wait, width, height, directory_path, file_name):

    # Set options
    options = Options()
    options.add_argument(f"--window-size={width},{height}")
    options.add_argument(f"--no-sandbox")
    options.add_argument(f"--headless")

    # Open Chrome webdriver
    driver = webdriver.Chrome(options=options)
    
    # Take screenshot
    driver.get(remote_url)
    sleep(wait)
    driver.save_screenshot(f"{directory_path}/{file_name}")

    # Take screenshot
    driver.close()

    return f"{file_name} screenshots saved"


def get_screenshot_resized(directory_path, file_name, new_file_name, new_width, height_crop):

    # Open the PNG image
    image = Image.open(f"{directory_path}/{file_name}")

    # Determine aspect ratio
    # TODO Make this as an argument
    aspect_ratio = image.height / image.width 

    # Set new height
    new_height = int(new_width * aspect_ratio)

    # Resize the image
    resized_image = image.resize((new_width, new_height))

    # Crop image
    width, height = resized_image.size
    cropped_image = resized_image.crop((0, 0, width, abs(height - (height - height_crop))))

    # Save the cropped image
    cropped_image.save(f"{directory_path}/{new_file_name}")

    return f"{new_file_name} screenshots saved"


def get_screenshot_resized_overlaid(base, overlay, lat, lng, directory_path, new_file_name):

    # Open the base image
    base_image = Image.open(base)

    # Open the overlay image
    overlay_image = Image.open(overlay)

    # Set coordinates of top-left corner
    box = (lat, lng)

    # Paste overlay image on top of base image
    base_image.paste(overlay_image, box)

    # Save image
    base_image.save(f"{directory_path}/{new_file_name}")

    return f"{directory_path}/{new_file_name}"


def cleanup(directory_path, file):
    try:
        os.remove(f"{directory_path}/{file}")
        return f"{file} has been deleted"
    except FileNotFoundError:
        return f"{file} not in directory"


if __name__ == "__main__":
    main()
