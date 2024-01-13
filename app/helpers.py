import os
import json
import base64
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from PIL import Image
from cairosvg import svg2png


def get_screenshot(url, wait, directory, settings_devices):

    # Set options
    options = Options()
    options.add_argument(f"--window-size={settings_devices['width_large']},{settings_devices['height_large']}")
    options.add_argument(f"--no-sandbox")
    options.add_argument(f"--headless")
    options.add_argument(f"--hide-scrollbars")

    try:
        # Set Chromedriver path
        service = Service(executable_path="/usr/bin/chromedriver")

        # Open Chrome webdriver
        driver = webdriver.Chrome(service=service, options=options)
    except:
        # Open Chrome webdriver
        driver = webdriver.Chrome(options=options)

    # Open Chrome webdriver
    driver = webdriver.Chrome(options=options)
    
    # Take screenshot
    driver.get(url)
    sleep(wait)
    driver.save_screenshot(f"{directory}/{settings_devices['filename_large']}")

    # Retrieve screenshot
    screenshot = driver.get_screenshot_as_png()

    # Take screenshot
    driver.close()

    return screenshot


def get_screenshot_full(url, wait, directory, settings_devices):

    options = Options()
    options.add_argument(f"--no-sandbox")
    options.add_argument(f"--headless=new")
    options.add_argument(f"--hide-scrollbars")

    try:
        # Set Chromedriver path
        service = Service(executable_path="/usr/bin/chromedriver")

        # Open Chrome webdriver
        driver = webdriver.Chrome(service=service, options=options)
    except:
        # Open Chrome webdriver
        driver = webdriver.Chrome(options=options)

    # Open Chrome webdriver
    driver = webdriver.Chrome(options=options)

    driver.get(url)

    sleep(wait)

    fname_out_full_screenshot_png = settings_devices["filename_large"]
    
    png = get_screenshot_full_chrome(driver)
    with open(f"{directory}/{fname_out_full_screenshot_png}", 'wb') as f:
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


def get_base(post, directory, svg, svg_fname, png_fname):

    # Create SVG file
    with open(f"{directory}/{svg_fname}", "w") as file:
        file.write(svg)
    
    # Convert to SVG to PNG
    svg2png(url=f"{directory}/{svg_fname}", 
            write_to=f"{directory}/{png_fname}", 
            background_color=post["doc_fill_color"])

    # Delete SVG file
    cleanup(directory, svg_fname)

    return 1


def get_overlay(directory, fname_input, fname_output, new_width, height_crop):

    # Open the PNG image
    image = Image.open(f"{directory}/{fname_input}")

    # Determine aspect ratio
    aspect_ratio = image.height / image.width 

    # Set new height
    new_height = int(new_width * aspect_ratio)

    # Resize the image
    resized_image = image.resize((new_width, new_height))

    # Crop image
    width, height = resized_image.size
    cropped_image = resized_image.crop((0, 0, width, abs(height - (height - height_crop))))

    # Save the cropped image
    cropped_image.save(f"{directory}/{fname_output}")

    return 1


def get_final_temp(base, overlay, lat, lng, directory_path, new_file_name):

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


def get_final(directory, filename_input, filename_output, post):

    right = post["doc_pad_h"]
    left = post["doc_pad_h"]
    top = post["doc_pad_v"]
    bottom = post["doc_pad_v"]
    color = post["doc_fill_color"]

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
    
    