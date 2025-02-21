"""
Process requests for OUTPUT_MOBILES.
"""

# Python Standard Library
from io import BytesIO
from textwrap import dedent

# Third-Party Libraries
from PIL import Image, ImageDraw, ImageOps

# Local
from api.core.config import settings_devices
from api.core.utils import get_screenshot
from api.core.utils import get_base
from api.core.utils import get_overlay
from api.core.utils import get_final_temp
from api.core.utils import get_final










def process_request_mobiles(post: dict) -> bytes:
    """
    Process requests for OUTPUT_MOBILES.

    Captures webpage screenshots at tablet and smarthphone viewport 
    sizes and composites each on stylized device mockups. Arranges 
    these mockups into a side-by-side layout and returns the final 
    composition as PNG image data.

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
        bytes: Final processed image data
    """
    # ################################################## #
    # GET CONFIG
    # ################################################## #
    mobiles_tablet_config = settings_devices.get('tablet')
    mobiles_smartphone_config = settings_devices.get('smartphone')


    # ################################################## #
    # GET SCREENSHOT
    # ################################################## #
    mobiles_tablet_screenshot = get_screenshot(str(post['remote_url']),
                                               post['wait'],
                                               mobiles_tablet_config)

    mobiles_smartphone_screenshot = get_screenshot(str(post['remote_url']),
                                                   post['wait'],
                                                   mobiles_smartphone_config)


    # ################################################## #
    # TABLET
    # ################################################## #
    # ################################################## #
    # GET BASE LAYER (MOCKUP DIAGRAM) - tablet only
    # ################################################## #
    svg = dedent(dedent(dedent(f'''\
        <?xml version="1.0" encoding="UTF-8"?>
        <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
        <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" width="1085px"
            height="1406px" viewBox="-0.5 -0.5 1085 1406" style="background-color: {post["doc_fill_color"]}">
            <defs />
            <g>
                <rect x="2" y="2" width="1080" height="1400" rx="43.2" ry="43.2" fill="{post["base_fill_color"]}" stroke="{post["base_stroke_color"]}"
                    stroke-width="5" pointer-events="all" />
                <rect x="34" y="35.5" width="1016" height="1336" rx="20.32" ry="20.32" fill="{post["doc_fill_color"]}" stroke="none"
                    pointer-events="all" />
            </g>
        </svg>'''
    )))
    mobiles_tablet_base = get_base(post, svg)

    # ################################################## #
    # GET OVERLAY (SCREENSHOT) - tablet only
    # ################################################## #
    # mobiles_tablet_new_width = mobiles_tablet_config['width_medium']
    # mobiles_tablet_height_crop = mobiles_tablet_config['medium_height_crop']
    mobiles_tablet_overlay = get_overlay(mobiles_tablet_screenshot,
                                         mobiles_tablet_config['width_medium'],
                                         mobiles_tablet_config['medium_height_crop'])

    # ################################################## #
    # GET OUTPUT FINAL (temp) - tablet only
    # ################################################## #
    # mobiles_tablet_lat = 34
    # mobiles_tablet_lng = 34
    mobiles_tablet_output_temp = get_final_temp(mobiles_tablet_base,
                                                mobiles_tablet_overlay,
                                                34,
                                                34)


    # ################################################## #
    # SMARTPHONE
    # ################################################## #
    # ################################################## #
    # GET BASE LAYER (MOCKUP DIAGRAM) - smartphone only
    # ################################################## #
    svg = dedent(dedent(dedent(f'''\
        <?xml version="1.0" encoding="UTF-8"?>
        <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
        <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" width="405px"
            height="806px" viewBox="-0.5 -0.5 405 806" style="background-color: {post["doc_fill_color"]}">
            <defs />
            <g>
                <rect x="2" y="2" width="400" height="800" rx="44" ry="44" fill="{post["base_fill_color"]}" stroke="{post["base_stroke_color"]}" stroke-width="5"
                    pointer-events="all" />
                <rect x="22" y="22" width="360" height="760" rx="28.8" ry="28.8" fill="{post["doc_fill_color"]}" stroke="none"
                    pointer-events="all" />
            </g>
        </svg>'''
    )))
    mobiles_smartphone_base = get_base(post, svg)

    # ################################################## #
    # GET OVERLAY (SCREENSHOT) - smartphone only
    # ################################################## #
    # mobiles_smartphone_new_width = mobiles_smartphone_config['width_medium']
    # mobiles_smartphone_height_crop = mobiles_smartphone_config['medium_height_crop']
    mobiles_smartphone_overlay = get_overlay(mobiles_smartphone_screenshot,
                                             mobiles_smartphone_config['width_medium'],
                                             mobiles_smartphone_config['medium_height_crop'])


    # ################################################## #
    # GET OUTPUT FINAL (temp) - smartphone only
    # ################################################## #
    # mobiles_smartphone_lat = 24
    # mobiles_smartphone_lng = 24
    mobiles_smartphone_output_temp = get_final_temp(mobiles_smartphone_base,
                                                    mobiles_smartphone_overlay,
                                                    24,
                                                    24)


    # ################################################## #
    # GET OUTPUT FINAL (temp) - mobiles
    # ################################################## #
    width = 1605
    height = 1406

    # Convert bytes to PIL Image objects
    mobiles_tablet_output_temp_img = Image.open(BytesIO(mobiles_tablet_output_temp))
    mobiles_smartphone_output_img = Image.open(BytesIO(mobiles_smartphone_output_temp))

    # Create a new PIL Image object for mobiles_output
    mobiles_output_temp_image = Image.new(mode='RGB', size=(width, height), color=f"{post['doc_fill_color']}")

    # Paste tablet final to mobiles_output_temp
    mobiles_tablet_box = (520, 0, 520 + mobiles_tablet_output_temp_img.width, mobiles_tablet_output_temp_img.height)
    mobiles_output_temp_image.paste(mobiles_tablet_output_temp_img, mobiles_tablet_box)

    # Paste smartphone final to mobiles_output_temp
    mobiles_smartphone_box = (0, 600, mobiles_smartphone_output_img.width, 600 + mobiles_smartphone_output_img.height)
    mobiles_output_temp_image.paste(mobiles_smartphone_output_img, mobiles_smartphone_box)

    # Convert mobile_output_temp PIL Image object to bytes
    with BytesIO() as output:
        mobiles_output_temp_image.save(output, format='PNG')
        mobiles_output_temp = output.getvalue()


    # ################################################## #
    # GET OUTPUT FINAL
    # ################################################## #
    mobiles_output_final = get_final(mobiles_output_temp, post)


    return mobiles_output_final


def get_overlay_final(directory, fname_input, fname_output):
    """
    TD
    """
    # Open the image
    image = Image.open(f"{directory}/{fname_input}")

    # Create a border with rounded corners
    border_radius = 20.32
    border_width = 0
    border_color = (255, 0, 0)  # Red color

    # Create a mask with rounded corners
    mask = Image.new("L", image.size, 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.rounded_rectangle((0, 0, image.width, image.height), border_radius, fill=255)

    # Apply the mask to the image
    image_with_border = ImageOps.fit(image, mask.size)
    image_with_border.putalpha(mask)

    # Draw the border
    border_draw = ImageDraw.Draw(image_with_border)
    border_draw.rounded_rectangle((0, 0, image.width, image.height), border_radius, outline=border_color, width=border_width)

    image_with_border.save(f"{directory}/{fname_output}")

    return 1


def get_subfinal_mobiles(base, overlay, lat, lng, directory_main, filename_output):
    """
    TD
    """
    # Open the base image
    base_image = Image.open(base)

    # Open the overlay image
    overlay_image = Image.open(overlay)

    # Set coordinates of top-left corner
    box = (lat, lng)

    # Overlay the images
    base_image.paste(overlay_image, box, mask=overlay_image)

    # Save the final image
    base_image.save(f"{directory_main}/{filename_output}")

    return 1
