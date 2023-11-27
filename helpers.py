import os
import re
import json
import base64
from selenium import webdriver
from PIL import Image
from time import sleep
import requests
from selenium.webdriver.chrome.options import Options


def get_validation(user_input):
    
    message = ""

    # Validate url
    try:
        response = requests.head(user_input["url"])
        if response.status_code not in (200, 302):
            message += f"¦— url - not valid or not accessible\n"
    except:
        message += f"¦— url - not valid or not accessible\n"

    # Validate wait
    if user_input["wait"] > 60:
        message += f"¦— wait time not valid\n"
    
    # Validate output dict
    for index, key in enumerate(list(user_input.keys())[3:], start=4):
        dictionary = user_input[key]
        # print(f"{index} — {key}: {dictionary}")
        for indx, ky in dictionary.items():
            dict = dictionary[indx]
            # print(f"{indx}: {dict}")
            # Request
            if indx == "request":
                if dict not in (True, False):
                    message += f"¦— {key} - request not valid\n"
            # Format
            elif indx == "format":
                if dict not in ("png"):
                    message += f"¦— {key} - format not valid\n"
            # doc_pad_h
            elif indx == "doc_pad_h":
                if isinstance(dict, int) and (0 < dict < 1000):
                    pass
                else:
                    message += f"¦— {key} - doc_pad_h not valid\n"
            # doc_pad_v
            elif indx == "doc_pad_v":
                if isinstance(dict, int) and (0 < dict < 1000):
                    pass
                else:
                    message += f"¦— {key} - doc_pad_v not valid\n"
            # doc_fill_color
            elif indx == "doc_fill_color":
                result = validate_hex_color(dict)
                if result == 0:
                    message += f"¦— {key} - doc_fill_color not valid\n"
            # base_stroke_color
            elif indx == "base_stroke_color":
                result = validate_hex_color(dict)
                if result == 0:
                    message += f"¦— {key} - base_stroke_color not valid\n"         
            # base_fill_color
            elif indx == "base_fill_color":
                result = validate_hex_color(dict)
                if result == 0:
                    message += f"¦— {key} - base_fill_color not valid\n"        

    return message


def validate_hex_color(color):
    pattern = r'^#([A-Fa-f0-9]{6})$'
    match = re.match(pattern, color)
    if match:
        return 1
    else:
        return 0
    

def get_screenshot(remote_url, wait, directory_path, input):

    # Set options
    options = Options()
    options.add_argument(f"--window-size={input['width_large']},{input['height_large']}")
    options.add_argument(f"--no-sandbox")
    options.add_argument(f"--headless")
    options.add_argument(f"--hide-scrollbars")

    # Open Chrome webdriver
    driver = webdriver.Chrome(options=options)
    
    # Take screenshot
    driver.get(remote_url)
    sleep(wait)
    driver.save_screenshot(f"{directory_path}/{input['filename_large']}")

    # Take screenshot
    driver.close()

    return 1


def get_screenshot_full(remote_url, wait, directory_path, input):

    options = Options()
    options.add_argument(f"--no-sandbox")
    options.add_argument(f"--headless=new")
    options.add_argument(f"--hide-scrollbars")

    driver = webdriver.Chrome(options=options)

    driver.get(remote_url)

    sleep(wait)

    filename_output_full_screenshot_png = input["filename_large"]
    
    png = get_screenshot_full_chrome(driver)
    with open(f"{directory_path}/{filename_output_full_screenshot_png}", 'wb') as f:
        f.write(png)

    driver.close()

    return 1


def get_screenshot_full_chrome(driver) :

    # Function adapted from StackOverflow answer 
    # https://stackoverflow.com/questions/45199076/take-full-page-screenshot-in-chrome-with-selenium/45201692#45201692

    def send(cmd, params):
        resource = "/session/%s/chromium/send_command_and_get_result" % \
            driver.session_id
        url = driver.command_executor._url + resource
        body = json.dumps({'cmd':cmd, 'params': params})
        response = driver.command_executor._request('POST', url, body)
        return response.get('value')

    def evaluate(script):
        response = send('Runtime.evaluate', {
            'returnByValue': True,
            'expression': script
        })
        return response['result']['value']

    metrics = evaluate( \
        "({" + \
            "width: Math.max(window.innerWidth, document.body.scrollWidth, " + \
                "document.documentElement.scrollWidth)|0," + \
            "height: Math.max(innerHeight, document.body.scrollHeight, " + \
                "document.documentElement.scrollHeight)|0," + \
            "deviceScaleFactor: window.devicePixelRatio || 1," + \
            "mobile: typeof window.orientation !== 'undefined'" + \
        "})")
    send('Emulation.setDeviceMetricsOverride', metrics)
    screenshot = send('Page.captureScreenshot', {
        'format': 'png',
        'fromSurface': True
    })
    send('Emulation.clearDeviceMetricsOverride', {})

    return base64.b64decode(screenshot['data'])


def get_screenshot_resized(directory_main, directory_screenshots, filename_input, filename_output, new_width, height_crop):

    # Open the PNG image
    image = Image.open(f"{directory_screenshots}/{filename_input}")

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
    cropped_image.save(f"{directory_main}/{filename_output}")

    return 1


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


def get_output_padded(directory, filename_input, filename_output, right, left, top, bottom, color):

    image = Image.open(f"{directory}/{filename_input}") 
    
    width, height = image.size 
    
    new_width = width + right + left 
    new_height = height + top + bottom 
    
    result = Image.new(image.mode, (new_width, new_height), color) 
    
    result.paste(image, (left, top)) 
    
    result.save(f"{directory}/{filename_output}") 

    return 1


def cleanup(directory_path, file):
    try:
        os.remove(f"{directory_path}/{file}")
        return f"{file} has been deleted"
    except FileNotFoundError:
        return f"{file} not in directory"
    