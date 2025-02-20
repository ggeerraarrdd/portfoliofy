"""
TD
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








def process_request_mobiles(post):
    """
    TD
    """
    # ################################################## #
    # Get system settings for desktop
    # ################################################## #
    tablet = settings_devices.get("tablet")
    smartphone = settings_devices.get("smartphone")

    # ################################################## #
    # Get screenshot
    # ################################################## #
    screenshot_tablet = get_screenshot(str(post["remote_url"]),
                                       post["wait"],
                                       tablet)

    screenshot_smartphone = get_screenshot(str(post["remote_url"]),
                                           post["wait"],
                                           smartphone)

    # ################################################## #
    # Handle OUTPUT_MOBILES - tablet
    # ################################################## #

    # Create base - tablet
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
    base_tablet = get_base(post, svg)

    # Create overlay - tablet
    new_width = tablet["width_medium"]
    height_crop = tablet["medium_height_crop"]
    overlay_tablet = get_overlay(screenshot_tablet,
                                 new_width,
                                 height_crop)

    # Combine base and overlay - tablet
    lat = 34
    lng = 34
    output_main_tablet = get_final_temp(base_tablet,
                                        overlay_tablet,
                                        lat,
                                        lng)


    # ################################################## #
    # Handle OUTPUT_MOBILES - smartphone
    # ################################################## #

    # Create base - smartphone
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
    base_smartphone = get_base(post, svg)

    # Create overlay - smartphone
    new_width = smartphone["width_medium"]
    height_crop = smartphone["medium_height_crop"]
    overlay_smartphone = get_overlay(screenshot_smartphone,
                                     new_width,
                                     height_crop)

    # # Combine base and overlay - smartphone
    # fname_input = fname_overlay_temp_smartphone
    # fname_output = fname_overlay_final_smartphone = "out_mobiles_overlay_final_smartphone.png"
    # get_overlay_final(directory,
    #                   fname_input,
    #                   fname_output)

    # Combine base and overlay - smartphone
    lat = 24
    lng = 24
    output_main_smartphone = get_final_temp(base_smartphone,
                                            overlay_smartphone,
                                            lat,
                                            lng)

    # ################################################## #
    # Handle OUTPUT_MOBILES - final temp
    # ################################################## #
    width = 1605
    height = 1406

    # Convert bytes to PIL Image objects
    output_main_tablet_img = Image.open(BytesIO(output_main_tablet))
    output_main_smartphone_img = Image.open(BytesIO(output_main_smartphone))

    output_mobiles_image = Image.new(mode="RGB", size=(width, height), color=f"{post['doc_fill_color']}")

    output_mobiles_tablet_box = (520, 0, 520 + output_main_tablet_img.width, output_main_tablet_img.height)
    output_mobiles_image.paste(output_main_tablet_img, output_mobiles_tablet_box)

    output_mobiles_smartphone_box = (0, 600, output_main_smartphone_img.width, 600 + output_main_smartphone_img.height)
    output_mobiles_image.paste(output_main_smartphone_img, output_mobiles_smartphone_box)

    with BytesIO() as output:
        output_mobiles_image.save(output, format='PNG')
        output_mobiles_temp = output.getvalue()

    # ################################################## #
    # Handle OUTPUT_MOBILES - final
    # ################################################## #
    output_mobiles_final = get_final(output_mobiles_temp,
                                  post)


    return output_mobiles_final


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
