"""
Screenshot and image processing utility functions for webpage screenshots.

This module provides functions for:
1. Taking screenshots of web pages using Selenium
2. Processing and combining images with various transformations
3. Managing temporary files and cleanup operations

Functions:
    get_screenshot: Capture fixed-size screenshot of a webpage
    get_screenshot_full: Capture full-page screenshot of a webpage
    get_screenshot_full_chrome: Helper for full page screenshot
    get_base: Create base PNG image from SVG
    get_overlay: Process screenshot into overlay image
    get_final_temp: Combine base and overlay images
    get_final: Add padding to final image
    cleanup: Remove temporary files
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










def get_screenshot(url: str, wait: int, settings_devices: dict) -> bytes:
    """
    Take a screenshot of a webpage at specified dimensions.

    Args:
        url (str): Website URL to capture
        wait (int): Time to wait for page load in seconds
        settings_devices (dict): Dictionary containing width_large and height_large values

    Returns:
        PNG screenshot as bytes
    """
    width = settings_devices['width_large']
    height = settings_devices['height_large']

    # Set options
    options = Options()
    options.add_argument(f'--window-size={width},{height}')
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--hide-scrollbars')

    try:
        # Set Chromedriver path
        service = Service(executable_path=CHROME_PATH)

        # Open Chrome webdriver
        driver = webdriver.Chrome(service=service, options=options)

    except: # pylint: disable=bare-except
        # Open Chrome webdriver
        driver = webdriver.Chrome(options=options)

    # Verify viewport size
    viewport_width = driver.execute_script('return window.innerWidth;')
    viewport_height = driver.execute_script('return window.innerHeight;')

    if viewport_width != settings_devices['width_large'] or viewport_height != settings_devices['height_large']:

        # Ensure viewport set to specified dimensions
        driver.execute_cdp_cmd('Emulation.setDeviceMetricsOverride', {
            'width': width,
            'height': height,
            'deviceScaleFactor': 1,
            'mobile': False
        })

    try:
        driver.get(url)
        sleep(wait)

        # Take screenshot
        screenshot = driver.get_screenshot_as_png()

        return screenshot

    finally:
        driver.quit()


def get_screenshot_full(url: str, wait: int) -> bytes:
    """
    Take a full page screenshot of a webpage.

    Args:
        url (str): Website URL to capture
        wait (int): Time to wait for page load in seconds

    Returns:
        PNG screenshot as bytes
    """
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--headless=new')
    options.add_argument('--hide-scrollbars')

    try:
        # Set Chromedriver path
        service = Service(executable_path=CHROME_PATH)

        # Open Chrome webdriver
        driver = webdriver.Chrome(service=service, options=options)

    except: # pylint: disable=bare-except
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


def get_screenshot_full_chrome(driver: webdriver.Chrome) -> bytes:
    """
    Helper function to capture full page screenshot using Chrome DevTools Protocol.

    Args:
        driver (webdriver.Chrome): Chrome WebDriver instance

    Returns:
        PNG screenshot as bytes
    """
    # Function adapted from StackOverflow answer
    # https://stackoverflow.com/questions/45199076/take-full-page-screenshot-in-chrome-with-selenium/45201692#45201692

    def send(cmd, params):
        resource = "/session/%s/chromium/send_command_and_get_result" % \
            driver.session_id # pylint: disable=consider-using-f-string
        url = driver.command_executor._url + resource # pylint: disable=protected-access
        body = json.dumps({'cmd':cmd, 'params': params})
        response = driver.command_executor._request('POST', url, body) # pylint: disable=protected-access
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


def get_base(post: dict, svg: str) -> bytes:
    """
    Creates base image from SVG and returns PNG bytes.

    Args:
        post (dict): Dictionary containing doc_fill_color
        svg (str): SVG content as string

    Returns:
        PNG image as bytes
    """
    with BytesIO() as svg_io, BytesIO() as png_io:

        svg_io.write(svg.encode())
        svg_io.seek(0)

        svg2png(file_obj=svg_io, write_to=png_io, background_color=post['doc_fill_color'])

        return png_io.getvalue()


def get_overlay(screenshot_bytes: bytes, new_width: int, height_crop: int) -> bytes:
    """
    Creates overlay image from screenshot and returns PNG bytes.

    Args:
        screenshot_bytes (bytes): Original screenshot as bytes
        new_width (int): Target width for resize
        height_crop (int): Height to crop from bottom

    Returns:
        PNG image as bytes
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


def get_final_temp(base_bytes: bytes, overlay_bytes: bytes, lat: int, lng: int) -> bytes:
    """
    Combines base and overlay images and returns PNG bytes.

    Args:
        base_bytes (bytes): Base image as bytes
        overlay_bytes (bytes): Overlay image as bytes
        lat (int): X coordinate for overlay placement
        lng (int): Y coordinate for overlay placement

    Returns:
        PNG image as bytes
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


# def get_final(image_bytes: bytes, post: dict) -> bytes:
#     """
#     Adds padding to image and returns final PNG bytes.

#     Args:
#         image_bytes (bytes): Input image as bytes
#         post (dict): Dictionary containing doc_pad_h, doc_pad_v, and doc_fill_color

#     Returns:
#         PNG image as bytes
#     """
#     with BytesIO(image_bytes) as img_io, BytesIO() as output:

#         image = Image.open(img_io)

#         width, height = image.size
#         right = left = post['doc_pad_h']
#         top = bottom = post['doc_pad_v']

#         new_width = width + right + left
#         new_height = height + top + bottom

#         result = Image.new(image.mode, (new_width, new_height), post['doc_fill_color'])
#         result.paste(image, (left, top))

#         result.save(output, format=f'{post["format"]}')

#         return output.getvalue()


def get_final(image_bytes: bytes, post: dict) -> bytes:
    """
    Adds padding to image and returns bytes in specified format.

    Args:
        image_bytes (bytes): Input image as bytes
        post (dict): Dictionary containing doc_pad_h, doc_pad_v, doc_fill_color, and format

    Returns:
        Image bytes in requested format
    """
    request_format = post.get("format", "PNG").upper()

    if request_format == "PDF":
        return _get_final_pdf(image_bytes, post)

    return _get_final_standard(image_bytes, post, request_format)


def _get_final_pdf(image_bytes: bytes, post: dict) -> bytes:
    """
    TD
    """
    with BytesIO(image_bytes) as img_io, BytesIO() as output:
        image = Image.open(img_io)

        # Add padding
        width, height = image.size
        right = left = post['doc_pad_h']
        top = bottom = post['doc_pad_v']

        new_width = width + right + left
        new_height = height + top + bottom

        result = Image.new(image.mode, (new_width, new_height), post['doc_fill_color'])
        result.paste(image, (left, top))

        # Convert to RGB for PDF
        rgb_result = result.convert('RGB')
        rgb_result.save(output, format="PDF", resolution=100.0)
        return output.getvalue()


def _get_final_standard(image_bytes: bytes, post: dict, request_format: str) -> bytes:
    """
    TD
    """
    with BytesIO(image_bytes) as img_io, BytesIO() as output:
        image = Image.open(img_io)

        width, height = image.size
        right = left = post['doc_pad_h']
        top = bottom = post['doc_pad_v']

        new_width = width + right + left
        new_height = height + top + bottom

        result = Image.new(image.mode, (new_width, new_height), post['doc_fill_color'])
        result.paste(image, (left, top))

        if request_format in ["PNG", "JPEG", "BMP", "TIFF"]:
            result.save(output, format=request_format)
        else:
            raise ValueError(f"Unsupported format: {request_format}")

        return output.getvalue()


def cleanup(directory_path: str, file: str) -> str:
    """
    Remove a file from the specified directory.

    Args:
        directory_path (str): Path to directory containing file
        file (str): Name of file to remove

    Returns:
        Status message indicating success or failure
    """
    try:
        os.remove(f'{directory_path}/{file}')
        return f'{file} has been deleted'
    except FileNotFoundError:
        return f'{file} not in directory'


def get_mime(request_format: str) -> str:
    """
    TD
    """
    if request_format.upper() == 'PDF':
        return 'application/pdf'

    if request_format.upper() == 'MP4':
        return 'video/mp4'

    if request_format.upper() == 'SVG':
        return 'image/svg+xml'


    return f"image/{request_format}"
