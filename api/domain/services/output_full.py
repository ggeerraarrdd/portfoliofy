"""
Process requests for OUTPUT_FULL.
"""

# Python Standard Libraries
from io import BytesIO
from textwrap import dedent

# Third Party Libraries
from PIL import Image, ImageOps

# Local
from api.core.config import settings_devices
from api.core.utils import get_screenshot_full
from api.core.utils import get_base
from api.core.utils import get_final










def process_request_full(post: dict) -> bytes:
    """
    Process requests for OUTPUT_FULL.

    Captures a full-page screenshot of the entire webpage content from top 
    to bottom, overlays it on a browser mockup diagram with custom styling, 
    and returns the composite as a PNG image data.

    Args:
        post (dict): Request parameters including (pre-validated with Pydantic):
            remote_url (str): URL to capture screenshot from
            wait (int): Wait time in seconds before capture
            format (str): Output image format
            doc_pad_h (int): Horizontal padding in pixels
            doc_pad_v (int): Vertical padding in pixels 
            doc_fill_color (str): Background color as hex
            base_stroke_color (str): Border color as hex
            base_fill_color (str): Base fill color as hex
            
    Returns:
        bytes: Final processed PNG image data
    """
    # ################################################## #
    # GET CONFIG
    # ################################################## #
    full_config = settings_devices.get('full')


    # ################################################## #
    # GET SCREENSHOT
    # ################################################## #
    full_screenshot = get_screenshot_full(str(post['remote_url']),
                                          post['wait'])


    # ################################################## #
    # GET BASE LAYER (MOCKUP DIAGRAM)
    # ################################################## #
    svg = dedent(dedent(dedent('''\
        <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" width="776px"
            height="121px" viewBox="-0.5 -0.5 776 121" style="background-color: rgb(255, 255, 255);">
            <defs />
            <g>
                <rect x="2" y="2" width="772" height="117" rx="17.55" ry="17.55" fill="#bac8d3" stroke="#23445d"
                    stroke-width="4" pointer-events="all" />
                <ellipse cx="41" cy="31" rx="9" ry="9" fill="#ffffff" stroke="#23445d" stroke-width="2" pointer-events="all" />
                <ellipse cx="73" cy="31" rx="9" ry="9" fill="#ffffff" stroke="#23445d" stroke-width="2" pointer-events="all" />
                <ellipse cx="105" cy="31" rx="9" ry="9" fill="#ffffff" stroke="#23445d" stroke-width="2" pointer-events="all" />
            </g>
        </svg>'''
    )))
    full_base = get_base(post, svg)


    # ################################################## #
    # GET OVERLAY (SCREENSHOT)
    # ################################################## #
    full_overlay = get_overlay_full(full_screenshot, full_config)
    full_overlay = get_overlay_full_bordered(full_overlay, post)


    # ################################################## #
    # GET OUTPUT FINAL (temp)
    # ################################################## #
    full_base_img = Image.open(BytesIO(full_base))
    full_overlay_img = Image.open(BytesIO(full_overlay))

    width = 776
    height = full_overlay_img.height + 60

    full_output_temp_img = Image.new('RGB', (width, height), (255, 255, 255))

    full_output_temp_img.paste(full_base_img, (0,0))
    full_output_temp_img.paste(full_overlay_img, (0,60))

    with BytesIO() as output:
        full_output_temp_img.save(output, format='PNG')
        full_output_temp = output.getvalue()


    # ################################################## #
    # GET OUTPUT FINAL
    # ################################################## #
    full_output_final = get_final(full_output_temp, post)


    return full_output_final


def get_overlay_full(screenshot_bytes, full):
    """
    TD
    """
    with BytesIO(screenshot_bytes) as img_io, BytesIO() as output:
        image = Image.open(img_io)

        # Determine dimensions
        aspect_ratio = image.height / image.width
        new_height = int(full["width_small"] * aspect_ratio)

        # Resize
        resized = image.resize((full["width_small"], new_height))

        # Save to bytes
        resized.save(output, format='PNG')

        overlay_full = output.getvalue()

        return overlay_full


def get_overlay_full_bordered(screenshot_bytes, full):
    """
    TD
    """
    with BytesIO(screenshot_bytes) as img_io, BytesIO() as output:
        image = Image.open(img_io)

        # Set the border width and color
        border_width = 4
        border_color = full["base_stroke_color"]

        # Add the border to the image
        image_with_border = ImageOps.expand(image, border=border_width, fill=border_color)

        # Save to bytes
        image_with_border.save(output, format='PNG')

        overlay_full_bordered = output.getvalue()

        return overlay_full_bordered
