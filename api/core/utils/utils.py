"""
TD
"""

# Python Standard Libraries
import base64
from io import BytesIO
import json
import os
from time import sleep

# Third-Party Libraries
from cairosvg import svg2png
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


CHROME_PATH = os.environ.get('CHROME_INSTALL_DIR')










def get_screenshot(url, wait, settings_devices):
    """
    TD
    """
    # Set options
    options = Options()
    options.add_argument(f"--window-size={settings_devices['width_large']},{settings_devices['height_large']}")
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")
    options.add_argument("--hide-scrollbars")

    try:
        # Set Chromedriver path
        service = Service(executable_path=CHROME_PATH)

        # Open Chrome webdriver
        driver = webdriver.Chrome(service=service, options=options)

    except:
        # Open Chrome webdriver
        driver = webdriver.Chrome(options=options)

    # Open Chrome webdriver
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)
        sleep(wait)

        # Take screenshot
        screenshot = driver.get_screenshot_as_png()

        return screenshot

    finally:
        driver.quit()


def get_screenshot_full(url, wait):
    """
    TD
    """
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--headless=new")
    options.add_argument("--hide-scrollbars")

    try:
        # Set Chromedriver path
        service = Service(executable_path=CHROME_PATH)

        # Open Chrome webdriver
        driver = webdriver.Chrome(service=service, options=options)
    except:
        # Open Chrome webdriver
        driver = webdriver.Chrome(options=options)

    # Open Chrome webdriver
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)
        sleep(wait)

        # Take screenshot
        screenshot = get_screenshot_full_chrome(driver)

        return screenshot

    finally:

        driver.quit()


def get_screenshot_full_chrome(driver) :
    """
    TD
    """
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


def get_base(post, svg):
    """
    Creates base image from SVG and returns PNG bytes
    """
    with BytesIO() as svg_io, BytesIO() as png_io:

        svg_io.write(svg.encode())
        svg_io.seek(0)

        svg2png(file_obj=svg_io,
                write_to=png_io,
                background_color=post["doc_fill_color"])

        return png_io.getvalue()


def get_overlay(screenshot_bytes, new_width, height_crop):
    """
    Creates overlay image from screenshot and returns PNG bytes
    """
    with BytesIO(screenshot_bytes) as img_io, BytesIO() as output:
        image = Image.open(img_io)

        # Resize
        aspect_ratio = image.height / image.width
        new_height = int(new_width * aspect_ratio)
        resized = image.resize((new_width, new_height))

        # Crop
        width, height = resized.size
        cropped = resized.crop((0, 0, width, abs(height - (height - height_crop))))

        # Save to bytes
        cropped.save(output, format='PNG')

        overlay = output.getvalue()

        return overlay


def get_final_temp(base_bytes, overlay_bytes, lat, lng):
    """
    Combines base and overlay images and returns PNG bytes
    """
    with BytesIO(base_bytes) as base_io, \
         BytesIO(overlay_bytes) as overlay_io, \
         BytesIO() as output:

        base_img = Image.open(base_io)
        overlay_img = Image.open(overlay_io)

        base_img.paste(overlay_img, (lat, lng))
        base_img.save(output, format='PNG')

        final_temp = output.getvalue()

        return final_temp


def get_final(image_bytes, post):
    """
    Adds padding to image and returns final PNG bytes
    """
    with BytesIO(image_bytes) as img_io, BytesIO() as output:

        image = Image.open(img_io)

        width, height = image.size
        right = left = post["doc_pad_h"]
        top = bottom = post["doc_pad_v"]

        new_width = width + right + left
        new_height = height + top + bottom

        result = Image.new(image.mode, (new_width, new_height), post["doc_fill_color"])
        result.paste(image, (left, top))

        result.save(output, format='PNG')

        return output.getvalue()


def cleanup(directory_path, file):
    """
    TD
    """
    try:
        os.remove(f"{directory_path}/{file}")
        return f"{file} has been deleted"
    except FileNotFoundError:
        return f"{file} not in directory"
