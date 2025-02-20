"""
TD
"""

# Python Standard Libraries
from textwrap import dedent

# Local
from api.core.config import settings_devices
from api.core.utils import get_screenshot
from api.core.utils import get_base
from api.core.utils import get_overlay
from api.core.utils import get_final_temp
from api.core.utils import get_final










def process_request_browser(post):
    """
    TD
    """
    # ################################################## #
    # Get system settings for desktop
    # ################################################## #
    desktop = settings_devices.get("desktop")


    # ################################################## #
    # Get screenshot
    # ################################################## #
    screenshot_browser = get_screenshot(str(post["remote_url"]),
                                        post["wait"],
                                        desktop)


    # ################################################## #
    # Create base layer
    # ################################################## #
    svg = dedent(dedent(dedent(f'''\
        <?xml version="1.0" encoding="UTF-8"?>
        <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
        <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" 
            width="2056px" height="1220px" viewBox="-0.5 -0.5 2056 1220"
            style="background-color: {post["doc_fill_color"]};">
            <defs />
            <g>
                <rect x="2" y="1" width="2052" height="130" rx="19.5" ry="19.5" fill="{post["base_fill_color"]}" stroke="{post["base_stroke_color"]}" stroke-width="4"
                    pointer-events="all" />
                <rect x="2" y="61" width="2052" height="1156" fill="{post["doc_fill_color"]}" stroke="{post["base_stroke_color"]}" stroke-width="4"
                    pointer-events="all" />
                <ellipse cx="44" cy="33" rx="12" ry="12" fill="{post["doc_fill_color"]}" stroke="{post["base_stroke_color"]}" stroke-width="2"
                    pointer-events="all" />
                <ellipse cx="84" cy="33" rx="12" ry="12" fill="{post["doc_fill_color"]}" stroke="{post["base_stroke_color"]}" stroke-width="2"
                    pointer-events="all" />
                <ellipse cx="124" cy="33" rx="12" ry="12" fill="{post["doc_fill_color"]}" stroke="{post["base_stroke_color"]}" stroke-width="2"
                    pointer-events="all" />
            </g>
        </svg>'''
    )))
    base_browser = get_base(post, svg)


    # ################################################## #
    # Create overlay
    # ################################################## #
    new_width = desktop["width_medium"]
    height_crop = desktop["medium_height_crop"]
    overlay_browser = get_overlay(screenshot_browser,
                                  new_width,
                                  height_crop)


    # ################################################## #
    # Create final (temp)
    # ################################################## #
    lat = 4
    lng = 64
    output_browser_temp = get_final_temp(base_browser,
                                         overlay_browser,
                                         lat,
                                         lng)


    # ################################################## #
    # Create final
    # ################################################## #
    output_browser_final = get_final(output_browser_temp,
                                     post)


    return output_browser_final
