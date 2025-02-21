"""
Process requests for OUTPUT_BROWSER.
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
from api.domain.schemas import PortfoliofyRequest # Pydantic model for request validation










def process_request_browser(post: PortfoliofyRequest) -> bytes:
    """
    Process requests for OUTPUT_BROWSER.

    Captures webpage screenshot at desktop viewport dimensions, overlays it 
    on a browser mockup diagram with custom styling, and returns the 
    composite as a PNG image data.

    Args:
        post (PortfoliofyRequest): Request containing URL and styling parameters
            Request data is pre-validated via Pydantic PortfoliofyRequest model.
            
    Returns:
        bytes: Final processed PNG image data
    """
    # ################################################## #
    # GET CONFIG
    # ################################################## #
    browser_config = settings_devices.get('desktop')


    # ################################################## #
    # GET SCREENSHOT
    # ################################################## #
    browser_screenshot = get_screenshot(str(post['remote_url']),
                                        post['wait'],
                                        browser_config)


    # ################################################## #
    # GET BASE LAYER (MOCKUP DIAGRAM)
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
    browser_base = get_base(post, svg)


    # ################################################## #
    # GET OVERLAY (SCREENSHOT)
    # ################################################## #
    # browser_new_width = browser_config['width_medium']
    # browser_height_crop = browser_config['medium_height_crop']
    browser_overlay = get_overlay(browser_screenshot,
                                  browser_config['width_medium'],
                                  browser_config['medium_height_crop'])


    # ################################################## #
    # GET OUTPUT FINAL (temp)
    # ################################################## #
    # browser_lat = 4
    # browser_lng = 64
    browser_output_temp = get_final_temp(browser_base,
                                         browser_overlay,
                                         4,
                                         64)


    # ################################################## #
    # GET OUTPUT FINAL
    # ################################################## #
    browser_output_final = get_final(browser_output_temp, post)


    return browser_output_final
