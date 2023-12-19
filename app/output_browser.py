import os
from datetime import datetime
from textwrap import dedent
from app.settings import settings_devices
from app.helpers import get_screenshot, get_base, get_overlay, get_final_temp, get_final, cleanup


def process_request_browser(post):

    # ################################################## #
    # Get system settings for desktop
    # ################################################## #
    desktop = settings_devices.get("desktop")

    # ################################################## #
    # Create directory
    # ################################################## #
    now = datetime.now()
    directory = now.strftime('%y%m%d_%H%M%S_%f')[:-3]
    directory = f"app/output/{directory}_browser"
    os.makedirs(directory)

    # ################################################## #
    # Get screenshot
    # ################################################## #
    get_screenshot(str(post["remote_url"]), 
                   post["wait"], 
                   directory, 
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

    fname_out_browser_base_svg = "out_browser_base.svg"
    fname_out_browser_base_png = "out_browser_base.png"
    get_base(post, 
             directory, 
             svg,
             fname_out_browser_base_svg, 
             fname_out_browser_base_png)

    # ################################################## #
    # Create overlay
    # ################################################## #
    fname_input = desktop["filename_large"]
    fname_output = fname_out_browser_overlay_png = "out_browser_overlay.png"
    new_width = desktop["width_medium"]
    height_crop = desktop["medium_height_crop"]
    get_overlay(directory, 
                fname_input, 
                fname_output, 
                new_width, 
                height_crop)

    # ################################################## #
    # Create temp
    # ################################################## #
    base = f"{directory}/{fname_out_browser_base_png}"
    overlay = f"{directory}/{fname_out_browser_overlay_png}"
    lat = 4
    lng = 64
    fname_out_browser_final_temp = "out_browser_final_temp.png"
    get_final_temp(base, 
                   overlay, 
                   lat, 
                   lng, 
                   directory, 
                   fname_out_browser_final_temp)

    # ################################################## #
    # Create final
    # ################################################## #
    fname_out_browser_final = "out_browser_final.png"
    get_final(directory, 
              fname_out_browser_final_temp, 
              fname_out_browser_final, 
              post)

    # ################################################## #
    # Delete temp files
    # ################################################## #
    cleanup(directory, desktop["filename_large"])
    cleanup(directory, fname_out_browser_base_png)
    cleanup(directory, fname_out_browser_overlay_png)
    cleanup(directory, fname_out_browser_final_temp)
    
    return f"{directory}/{fname_out_browser_final}"

