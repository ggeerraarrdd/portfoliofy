"""
Process requests for OUTPUT_MAIN.
"""

# Standard Python Libraries
from io import BytesIO
from textwrap import dedent

# Third-Party Libraries
from PIL import Image

# Local
from api.core.config import settings_devices
from api.core.utils import get_screenshot
from api.core.utils import get_base
from api.core.utils import get_overlay
from api.core.utils import get_final_temp
from api.core.utils import get_final










def process_request_main(post: dict) -> bytes:
    """
    Process requests for OUTPUT_MAIN.

    Captures webpage screenshots at multiple viewport sizes (desktop, 
    laptop, tablet, smartphone) and composites each on stylized device 
    mockups. Arranges these mockups into a eye-catching layout and returns
    the final composition as PNG image data.

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
    # Get system settings for desktop
    # ################################################## #
    desktop = settings_devices.get("desktop")
    laptop = settings_devices.get("laptop")
    tablet = settings_devices.get("tablet")
    smartphone = settings_devices.get("smartphone")

    # ################################################## #
    # Get screenshot
    # ################################################## #
    screenshot_desktop = get_screenshot(str(post["remote_url"]), post["wait"], desktop)
    screenshot_laptop = get_screenshot(str(post["remote_url"]), post["wait"], laptop)
    screenshot_tablet = get_screenshot(str(post["remote_url"]), post["wait"], tablet)
    screenshot_smartphone = get_screenshot(str(post["remote_url"]), post["wait"], smartphone)

    # ################################################## #
    # Handle OUTPUT_MAIN - desktop
    # ################################################## #

    # Create base layer - desktop
    svg = dedent(dedent(f'''\
        <?xml version="1.0" encoding="UTF-8"?>
        <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
        <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" 
            width="2065px" height="1515px" viewBox="-0.5 -0.5 2065 1515" 
            style="background-color: {post["doc_fill_color"]};">
            <defs />
            <g>
                <rect x="2" y="2" width="2060" height="1220" rx="24.4" ry="24.4" fill="{post["base_fill_color"]}" stroke="{post["base_stroke_color"]}"
                    stroke-width="5" pointer-events="all" />
                <rect x="72" y="72" width="1923" height="1083" fill="{post["doc_fill_color"]}" stroke="rgb(0, 0, 0)" stroke-width="3"
                    pointer-events="all" />
                <rect x="872" y="1222" width="320" height="270" fill="{post["base_fill_color"]}" stroke="{post["base_stroke_color"]}" stroke-width="5"
                    pointer-events="all" />
                <rect x="872" y="1492" width="320" height="20" fill="{post["base_fill_color"]}" stroke="{post["base_stroke_color"]}" stroke-width="5"
                    pointer-events="all" />
            </g>
        </svg>'''
    ))
    base_desktop = get_base(post, svg)

    # Create overlay - desktop
    new_width = desktop["width_small"]
    height_crop = desktop["small_height_crop"]
    overlay_desktop = get_overlay(screenshot_desktop, new_width, height_crop)

    # Combine base and overlay - desktop
    lat = 74
    lng = 74
    output_main_desktop = get_final_temp(base_desktop, overlay_desktop, lat, lng)


    # ################################################## #
    # Handle OUTPUT_MAIN - laptop
    # ################################################## #

    # Create base - laptop
    svg = dedent(dedent(f'''\
        <?xml version="1.0" encoding="UTF-8"?>
        <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
        <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" 
            width="1345px" height="815px" viewBox="-0.5 -0.5 1345 815" 
            style="background-color: {post["doc_fill_color"]};">
            <defs />
            <g>
                <rect x="2" y="2" width="1340" height="780" rx="15.6" ry="15.6" fill="{post["base_fill_color"]}" stroke="{post["base_stroke_color"]}" stroke-width="5"
                    pointer-events="all" />
                <rect x="32" y="32" width="1283" height="723" fill="rgb(255, 255, 255)" stroke="rgb(0, 0, 0)" stroke-width="3"
                    pointer-events="all" />
                <rect x="2" y="782" width="1340" height="30" rx="4.5" ry="4.5" fill="{post["base_fill_color"]}" stroke="{post["base_stroke_color"]}" stroke-width="5"
                    pointer-events="all" />
            </g>
        </svg>'''
    ))
    base_laptop = get_base(post, svg)

    # Create overlay - laptop
    new_width = laptop["width_small"]
    height_crop = laptop["small_height_crop"]
    overlay_laptop = get_overlay(screenshot_laptop, new_width, height_crop)

    # Combine base and overlay - laptop
    lat = 34
    lng = 34
    output_main_laptop = get_final_temp(base_laptop, overlay_laptop, lat, lng)

    # ################################################## #
    # Handle OUTPUT_MAIN - tablet
    # ################################################## #

    # Create base - tablet
    svg = dedent(dedent(f'''\
        <?xml version="1.0" encoding="UTF-8"?>
        <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
        <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" 
            width="665px" height="865px" viewBox="-0.5 -0.5 665 865">
            <defs />
            <g>
                <rect x="2" y="2" width="660" height="860" rx="13.2" ry="13.2" fill="{post["base_fill_color"]}" stroke="{post["base_stroke_color"]}" stroke-width="5"
                    pointer-events="all" />
                <rect x="32" y="32" width="603" height="803" fill="rgb(255, 255, 255)" stroke="rgb(0, 0, 0)" stroke-width="4"
                    pointer-events="all" />
            </g>
        </svg>'''
    ))
    base_tablet = get_base(post, svg)

    # Create overlay - tablet
    tablet_new_width = tablet["width_small"]
    tablet_height_crop = tablet["small_height_crop"]
    tablet_overlay = get_overlay(screenshot_tablet, tablet_new_width, tablet_height_crop)

    # Combine base and overlay - tablet
    tablet_lat = 34
    tablet_lng = 34
    output_main_tablet = get_final_temp(base_tablet, tablet_overlay, tablet_lat, tablet_lng)

    # ################################################## #
    # Handle OUTPUT_MAIN - smartphone
    # ################################################## #

    # Create base - smartphone
    svg = dedent(dedent(f'''\
        <?xml version="1.0" encoding="UTF-8"?>
        <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
        <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" 
            width="275px" height="535px" viewBox="-0.5 -0.5 275 535">
            <defs />
            <g>
                <rect x="2" y="2" width="270" height="530" rx="10.8" ry="10.8" fill="{post["base_fill_color"]}" stroke="{post["base_stroke_color"]}" stroke-width="5"
                    pointer-events="all" />
                <rect x="22" y="22" width="233" height="493" fill="rgb(255, 255, 255)" stroke="rgb(0, 0, 0)" stroke-width="3"
                    pointer-events="all" />
            </g>
        </svg>'''
    ))
    base_smartphone = get_base(post, svg)

    # Create overlay - smartphone
    new_width = smartphone["width_small"]
    height_crop = smartphone["small_height_crop"]
    overlay_smartphone = get_overlay(screenshot_smartphone, new_width, height_crop)

    # Combine base and overlay - smartphone
    lat = 24
    lng = 24
    output_main_smartphone = get_final_temp(base_smartphone, overlay_smartphone, lat, lng)

    # ################################################## #
    # Handle OUTPUT_MAIN - final temp
    # ################################################## #
    width = 3176
    height = 1515

    # Convert bytes to PIL Image objects
    output_main_desktop_img = Image.open(BytesIO(output_main_desktop))
    output_main_laptop_img = Image.open(BytesIO(output_main_laptop))
    output_main_tablet_img = Image.open(BytesIO(output_main_tablet))
    output_main_smartphone_img = Image.open(BytesIO(output_main_smartphone))

    output_main_img = Image.new(mode="RGB", size=(width, height), color=f"{post['doc_fill_color']}")

    # Now use the PIL Image objects for dimensions
    output_main_desktop_box = (750, 0, 750 + output_main_desktop_img.width, output_main_desktop_img.height)
    output_main_img.paste(output_main_desktop_img, output_main_desktop_box)

    output_main_laptop_box = (0, 700, output_main_laptop_img.width, 700 + output_main_laptop_img.height)
    output_main_img.paste(output_main_laptop_img, output_main_laptop_box)

    output_main_tablet_box = (2410, 650, 2410 + output_main_tablet_img.width, 650 + output_main_tablet_img.height)
    output_main_img.paste(output_main_tablet_img, output_main_tablet_box)

    output_main_smartphone_box = (2900, 980, 2900 + output_main_smartphone_img.width, 980 + output_main_smartphone_img.height)
    output_main_img.paste(output_main_smartphone_img, output_main_smartphone_box)

    with BytesIO() as output:
        output_main_img.save(output, format='PNG')
        output_main_temp = output.getvalue()


    # ################################################## #
    # Handle OUTPUT_MAIN - final
    # ################################################## #
    output_main_final = get_final(output_main_temp, post)


    return output_main_final
