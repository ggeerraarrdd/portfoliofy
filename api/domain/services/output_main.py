"""
TD
"""

# Standard Python Libraries
import os
from datetime import datetime
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
from api.core.utils import cleanup








def process_request_main(post):
    """
    TD
    """
    # ################################################## #
    # Get system settings for desktop
    # ################################################## #
    desktop = settings_devices.get("desktop")
    laptop = settings_devices.get("laptop")
    tablet = settings_devices.get("tablet")
    smartphone = settings_devices.get("smartphone")

    # ################################################## #
    # Create directory
    # ################################################## #
    now = datetime.now()
    directory = now.strftime('%y%m%d_%H%M%S_%f')[:-3]
    directory = f"api/output/{directory}_main"
    os.makedirs(directory)

    # ################################################## #
    # Get screenshot
    # ################################################## #
    get_screenshot(str(post["remote_url"]),
                   post["wait"],
                   directory,
                   desktop)

    get_screenshot(str(post["remote_url"]),
                   post["wait"],
                   directory,
                   laptop)

    get_screenshot(str(post["remote_url"]),
                   post["wait"],
                   directory,
                   tablet)

    get_screenshot(str(post["remote_url"]),
                   post["wait"],
                   directory,
                   smartphone)

    # ################################################## #
    # Handle OUTPUT_MAIN - desktop
    # ################################################## #

    # Create base - desktop
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

    fname_out_main_desktop_base_svg = "out_main_desktop_base.svg"
    fname_out_main_desktop_base_png = "out_main_desktop_base.png"
    get_base(post,
             directory,
             svg,
             fname_out_main_desktop_base_svg,
             fname_out_main_desktop_base_png)

    # Create overlay - desktop
    fname_input = desktop["filename_large"]
    fname_output = fname_out_main_desktop_overlay_png = "output_main_desktop_overlay.png"
    new_width = desktop["width_small"]
    height_crop = desktop["small_height_crop"]
    get_overlay(directory,
                fname_input,
                fname_output,
                new_width,
                height_crop)

    # Combine base and overlay - desktop
    base = f"{directory}/{fname_out_main_desktop_base_png}"
    overlay = f"{directory}/{fname_out_main_desktop_overlay_png}"
    lat = 74
    lng = 74
    fname_out_main_desktop_final = "output_main_desktop_final.png"
    get_final_temp(base,
                   overlay,
                   lat,
                   lng,
                   directory,
                   fname_out_main_desktop_final)

    # Delete temp files - desktop
    cleanup(directory, desktop["filename_large"])
    cleanup(directory, fname_out_main_desktop_base_png)
    cleanup(directory, fname_out_main_desktop_overlay_png)

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

    fname_out_main_laptop_base_svg = "out_main_laptop_base.svg"
    fname_out_main_laptop_base_png = "out_main_laptop_base.png"
    get_base(post,
             directory,
             svg,
             fname_out_main_laptop_base_svg,
             fname_out_main_laptop_base_png)

    # Create overlay - laptop
    fname_input = laptop["filename_large"]
    fname_output = fname_out_main_laptop_overlay_png = "output_main_laptop_overlay.png"
    new_width = laptop["width_small"]
    height_crop = laptop["small_height_crop"]
    get_overlay(directory,
                fname_input,
                fname_output,
                new_width,
                height_crop)

    # Combine base and overlay - laptop
    base = f"{directory}/{fname_out_main_laptop_base_png}"
    overlay = f"{directory}/{fname_out_main_laptop_overlay_png}"
    lat = 34
    lng = 34
    fname_out_main_laptop_final = "output_main_laptop_final.png"
    get_final_temp(base,
                   overlay,
                   lat,
                   lng,
                   directory,
                   fname_out_main_laptop_final)

    # Delete temp files - laptop
    cleanup(directory, laptop["filename_large"])
    cleanup(directory, fname_out_main_laptop_base_png)
    cleanup(directory, fname_out_main_laptop_overlay_png)

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

    fname_out_main_tablet_base_svg = "out_main_tablet_base.svg"
    fname_out_main_tablet_base_png = "out_main_tablet_base.png"
    get_base(post,
             directory,
             svg,
             fname_out_main_tablet_base_svg,
             fname_out_main_tablet_base_png)

    # Create overlay - tablet
    fname_input = tablet["filename_large"]
    fname_output = fname_out_main_tablet_overlay_png = "output_main_tablet_overlay.png"
    new_width = tablet["width_small"]
    height_crop = tablet["small_height_crop"]
    get_overlay(directory,
                fname_input,
                fname_output,
                new_width,
                height_crop)

    # Combine base and overlay - tablet
    base = f"{directory}/{fname_out_main_tablet_base_png}"
    overlay = f"{directory}/{fname_out_main_tablet_overlay_png}"
    lat = 34
    lng = 34
    fname_out_main_tablet_final = "output_main_tablet_final.png"
    get_final_temp(base,
                   overlay,
                   lat,
                   lng,
                   directory,
                   fname_out_main_tablet_final)

    # Delete temp files - tablet
    cleanup(directory, tablet["filename_large"])
    cleanup(directory, fname_out_main_tablet_base_png)
    cleanup(directory, fname_out_main_tablet_overlay_png)

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

    fname_out_main_smartphone_base_svg = "out_main_smartphone_base.svg"
    fname_out_main_smartphone_base_png = "out_main_smartphone_base.png"
    get_base(post,
             directory,
             svg,
             fname_out_main_smartphone_base_svg,
             fname_out_main_smartphone_base_png)

    # Create overlay - smartphone
    fname_input = smartphone["filename_large"]
    fname_output = fname_out_main_smartphone_overlay_png = "output_main_smartphone_overlay.png"
    new_width = smartphone["width_small"]
    height_crop = smartphone["small_height_crop"]
    get_overlay(directory,
                fname_input,
                fname_output,
                new_width,
                height_crop)

    # Combine base and overlay - smartphone
    base = f"{directory}/{fname_out_main_smartphone_base_png}"
    overlay = f"{directory}/{fname_out_main_smartphone_overlay_png}"
    lat = 24
    lng = 24
    fname_out_main_smartphone_final = "output_main_smartphone_final.png"
    get_final_temp(base,
                   overlay,
                   lat,
                   lng,
                   directory,
                   fname_out_main_smartphone_final)

    # Delete temp files - laptop
    cleanup(directory, smartphone["filename_large"])
    cleanup(directory, fname_out_main_smartphone_base_png)
    cleanup(directory, fname_out_main_smartphone_overlay_png)

    # ################################################## #
    # Handle OUTPUT_MAIN - final temp
    # ################################################## #

    width = 3176
    height = 1515

    output_main_all_base = Image.new(mode="RGB", size=(width, height), color=f"{post['doc_fill_color']}")

    output_main_desktop = Image.open(f"{directory}/{fname_out_main_desktop_final}")
    output_main_laptop = Image.open(f"{directory}/{fname_out_main_laptop_final}")
    output_main_tablet = Image.open(f"{directory}/{fname_out_main_tablet_final}")
    output_main_smartphone = Image.open(f"{directory}/{fname_out_main_smartphone_final}")

    output_main_desktop_box = (750, 0)
    output_main_all_base.paste(output_main_desktop, output_main_desktop_box)

    output_main_laptop_box = (0, 700)
    output_main_all_base.paste(output_main_laptop, output_main_laptop_box)

    output_main_tablet_box = (2410, 650)
    output_main_all_base.paste(output_main_tablet, output_main_tablet_box)

    output_main_smartphone_box = (2900, 980)
    output_main_all_base.paste(output_main_smartphone, output_main_smartphone_box)

    fname_out_main_final_temp = "output_main_final_temp.png"
    output_main_all_base.save(f"{directory}/{fname_out_main_final_temp}")

    # Delete temp files
    cleanup(directory, fname_out_main_desktop_final)
    cleanup(directory, fname_out_main_laptop_final)
    cleanup(directory, fname_out_main_tablet_final)
    cleanup(directory, fname_out_main_smartphone_final)

    # ################################################## #
    # Handle OUTPUT_MAIN - final
    # ################################################## #
    fname_out_main_final = "out_main_final.png"
    get_final(directory,
              fname_out_main_final_temp,
              fname_out_main_final,
              post)

    cleanup(directory, fname_out_main_final_temp)

    return f"{directory}/{fname_out_main_final}"
