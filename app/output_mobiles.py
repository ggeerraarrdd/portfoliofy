import os
from datetime import datetime
from textwrap import dedent
from PIL import Image, ImageDraw, ImageOps
from app.settings import settings_devices
from app.helpers import get_screenshot, get_base, get_overlay, get_final_temp, get_final, cleanup


def process_request_mobiles(post):

    # ################################################## #
    # Get system settings for desktop
    # ################################################## #
    tablet = settings_devices.get("tablet")
    smartphone = settings_devices.get("smartphone")

    # ################################################## #
    # Create directory
    # ################################################## #
    now = datetime.now()
    directory = now.strftime('%y%m%d_%H%M%S_%f')[:-3]
    directory = f"app/output/{directory}_mobiles"
    os.makedirs(directory)

    # ################################################## #
    # Get screenshot
    # ################################################## #
    get_screenshot(str(post["remote_url"]), 
                   post["wait"],
                   directory, 
                   tablet)
    
    get_screenshot(str(post["remote_url"]), 
                   post["wait"], 
                   directory, 
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

    fname_base_tablet_svg = "out_mobiles_base_tablet.svg"
    fname_base_tablet_png = "out_mobiles_base_tablet.png"
    get_base(post, 
             directory, 
             svg,
             fname_base_tablet_svg, 
             fname_base_tablet_png)

    # Create overlay - tablet
    fname_input = tablet["filename_large"]
    fname_output = fname_overlay_temp_tablet = "out_mobiles_overlay_temp_tablet.png"
    get_overlay(directory,
                fname_input, 
                fname_output, 
                tablet["width_medium"],
                tablet["medium_height_crop"])

    # Combine base and overlay - tablet
    fname_input = fname_overlay_temp_tablet
    fname_output = fname_overlay_final_tablet = "out_mobiles_overlay_final_tablet.png"
    get_overlay_final(directory,
                      fname_input, 
                      fname_output)

    # Combine base layer and overlay
    base = f"{directory}/{fname_base_tablet_png}"
    overlay = f"{directory}/{fname_overlay_final_tablet}"
    lat = 34
    lng = 36
    fname_subfinal_tablet = "out_mobiles_subfinal_tablet.png"
    get_subfinal_mobiles(base, 
                         overlay, 
                         lat, 
                         lng, 
                         directory, 
                         fname_subfinal_tablet)

    # Delete temp files - tablet
    cleanup(directory, tablet["filename_large"])
    cleanup(directory, fname_base_tablet_png)
    cleanup(directory, fname_overlay_temp_tablet)
    cleanup(directory, fname_overlay_final_tablet)

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

    fname_base_smartphone_svg = "out_mobiles_base_smartphone.svg"
    fname_base_smartphone_png = "out_mobiles_base_smartphone.png"
    get_base(post, 
             directory, 
             svg,
             fname_base_smartphone_svg, 
             fname_base_smartphone_png)

    # Create overlay - smartphone
    fname_input = smartphone["filename_large"]
    fname_output = fname_overlay_temp_smartphone = "out_mobiles_overlay_temp_smartphone.png"
    get_overlay(directory,
                fname_input, 
                fname_output, 
                smartphone["width_medium"],
                smartphone["medium_height_crop"])

    # Combine base and overlay - smartphone
    fname_input = fname_overlay_temp_smartphone
    fname_output = fname_overlay_final_smartphone = "out_mobiles_overlay_final_smartphone.png"
    get_overlay_final(directory, 
                      fname_input, 
                      fname_output)

    # Combine base layer and overlay
    base = f"{directory}/{fname_base_smartphone_png}"
    overlay = f"{directory}/{fname_overlay_final_smartphone}"
    lat = 22
    lng = 23
    fname_subfinal_smartphone = "out_mobiles_subfinal_smartphone.png"
    get_subfinal_mobiles(base, 
                         overlay, 
                         lat, 
                         lng, 
                         directory, 
                         fname_subfinal_smartphone)

    # Delete temp files - tablet
    cleanup(directory, smartphone["filename_large"])
    cleanup(directory, fname_base_smartphone_png)
    cleanup(directory, fname_overlay_temp_smartphone)
    cleanup(directory, fname_overlay_final_smartphone)

    # ################################################## #
    # Handle OUTPUT_MOBILES - final temp
    # ################################################## #

    width = 1605
    height = 1406

    out_mobiles_base = Image.new(mode="RGB", size=(width, height), color=f"{post['doc_fill_color']}")

    out_mobiles_subfinal_tablet = Image.open(f"{directory}/{fname_subfinal_tablet}")
    out_mobiles_subfinal_smartphone = Image.open(f"{directory}/{fname_subfinal_smartphone}")

    out_mobiles_tablet_box = (520, 0)
    out_mobiles_base.paste(out_mobiles_subfinal_tablet, out_mobiles_tablet_box)

    out_mobiles_smartphone_box = (0, 600)
    out_mobiles_base.paste(out_mobiles_subfinal_smartphone, out_mobiles_smartphone_box)

    fname_out_mobiles_final_temp = "out_mobiles_final_temp.png"
    out_mobiles_base.save(f"{directory}/{fname_out_mobiles_final_temp}")

    # Delete temp files - final temp
    cleanup(directory, fname_subfinal_tablet)
    cleanup(directory, fname_subfinal_smartphone)

    # ################################################## #
    # Handle OUTPUT_MOBILES - final
    # ################################################## #
    fname_out_mobiles_final = "out_mobiles_final.png"
    get_final(directory, 
              fname_out_mobiles_final_temp, 
              fname_out_mobiles_final, 
              post)
    
    # Delete temp files - final
    cleanup(directory, fname_out_mobiles_final_temp)

    return f"{directory}/{fname_out_mobiles_final}"


def get_overlay_final(directory, fname_input, fname_output):

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

