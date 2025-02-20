"""
TD
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











def process_request_full(post):
    """
    TD
    """
    # ################################################## #
    # Get system settings for full
    # ################################################## #
    full = settings_devices.get("full")


    # ################################################## #
    # Get screenshot
    # ################################################## #
    screenshot_full = get_screenshot_full(str(post["remote_url"]),
                                          post["wait"])


    # ################################################## #
    # Create base layer
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
    base_full = get_base(post, svg)


    # ################################################## #
    # Create overlay
    # ################################################## #
    overlay_full = get_overlay_full(screenshot_full,
                                    full)

    overlay_full = get_overlay_full_bordered(overlay_full,
                                             post)


    # ################################################## #
    # Create final temp
    # ################################################## #
    output_full_base_img = Image.open(BytesIO(base_full))
    output_full_overlay_img = Image.open(BytesIO(overlay_full))

    width = 776
    height = output_full_overlay_img.height + 60

    output_full_img = Image.new("RGB", (width, height), (255, 255, 255))

    output_full_img.paste(output_full_base_img, (0,0))
    output_full_img.paste(output_full_overlay_img, (0,60))

    with BytesIO() as output:
        output_full_img.save(output, format='PNG')
        output_full_temp = output.getvalue()


    # ################################################## #
    # Create final
    # ################################################## #
    output_full_final = get_final(output_full_temp,
                                 post)


    return output_full_final


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
