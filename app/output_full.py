import os
from datetime import datetime
from textwrap import dedent
from PIL import Image, ImageOps
from cairosvg import svg2png
from textwrap import dedent
from app.settings import settings_devices
from app.helpers import get_screenshot_full, get_base, get_overlay, get_final, cleanup


def process_request_full(post):

    # ################################################## #
    # Get system settings for full
    # ################################################## #
    full = settings_devices.get("full")

    # ################################################## #
    # Create directory
    # ################################################## #
    now = datetime.now()
    directory = now.strftime('%y%m%d_%H%M%S_%f')[:-3]
    directory = f"app/output/{directory}_full"
    os.makedirs(directory)

    # ################################################## #
    # Get screenshot
    # ################################################## #
    get_screenshot_full(str(post["remote_url"]), 
                   post["wait"], 
                   directory, 
                   full)
    
    # ################################################## #
    # Create base layer
    # ################################################## #
    svg = dedent(dedent(dedent(f'''\
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

    fname_out_full_base_svg = "out_full_base.svg"
    fname_out_full_base_png = "out_full_base.png"
    get_base(post, 
             directory, 
             svg, 
             fname_out_full_base_svg, 
             fname_out_full_base_png)

    # ################################################## #
    # Create overlay
    # ################################################## #
    fname_input = full["filename_large"]
    fname_output = fname_out_full_overlay_png = "output_full_overlay.png"
    get_overlay_full(full,
                     directory, 
                     fname_input, 
                     fname_output)
    
    get_overlay_full_bordered(post, 
                              directory, 
                              fname_output) 

    # ################################################## #
    # Create final temp
    # ################################################## #
    out_full_base = Image.open(f"{directory}/{fname_out_full_base_png}")
    out_full_overlay = Image.open(f"{directory}/{fname_out_full_overlay_png}")

    width = 776
    height = out_full_overlay.height + 60

    out_full_final = Image.new("RGB", (width, height), (255, 255, 255))

    out_full_final.paste(out_full_base, (0,0))
    out_full_final.paste(out_full_overlay, (0,60))

    fname_out_full_final_temp = "output_full_final_temp.png"
    out_full_final.save(f"{directory}/{fname_out_full_final_temp}")

    # ################################################## #
    # Create final
    # ################################################## #
    fname_out_full_final = "output_full_final.png"
    get_final(directory, 
              fname_out_full_final_temp,
              fname_out_full_final, 
              post)

    # # Delete temp files
    cleanup(directory, full["filename_large"])
    cleanup(directory, fname_out_full_base_png)
    cleanup(directory, fname_out_full_overlay_png)
    cleanup(directory, fname_out_full_final_temp)

    return f"{directory}/{fname_out_full_final}"


def get_overlay_full(full, directory, fname_input, fname_output):

    # Open the PNG image
    image = Image.open(f"{directory}/{fname_input}")

    # Determine aspect ratio
    aspect_ratio = image.height / image.width 

    # Set new height
    new_height = int(full["width_small"] * aspect_ratio)

    # Resize the image
    resized_image = image.resize((full["width_small"], new_height))

    resized_image.save(f"{directory}/{fname_output}")

    return 1


def get_overlay_full_bordered(full, directory_main, filename_input):

    # Open the PNG image
    image = Image.open(f"{directory_main}/{filename_input}")

    # Set the border width and color
    border_width = 4
    border_color = full["base_stroke_color"]

    # Add the border to the image
    image_with_border = ImageOps.expand(image, border=border_width, fill=border_color)

    # Save the image with the border
    image_with_border.save(f"{directory_main}/{filename_input}")

    return 1


