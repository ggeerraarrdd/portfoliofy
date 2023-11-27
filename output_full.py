from PIL import Image, ImageOps
from cairosvg import svg2png
from textwrap import dedent
from helpers import get_output_padded, cleanup


def process_request_full(blueprint_user, blueprint_system, directory_main, directory_screenshots):

    full = blueprint_system.get("full")

    # Set svg for tablet
    svg_full = dedent(dedent(dedent(f'''\
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

    # Create base - full
    filename_output_full_base_svg = "output_full_base.svg"
    filename_output_full_base_png = "output_full_base.png"
    get_output_full_base(blueprint_user, directory_main, svg_full, filename_output_full_base_svg, filename_output_full_base_png)

    # Create overlay - full - temp
    filename_input = blueprint_system["filename_large"]
    filename_output = filename_output_full_overlay_png = "output_full_overlay.png"
    get_output_full_overlay_resized(blueprint_system, directory_main, directory_screenshots, filename_input, filename_output)
    get_output_full_overlay_bordered(blueprint_user, directory_main, filename_output) 
    print("OUTPUT_FULL - overlay - generated.")

    output_full_base = Image.open(f"{directory_main}/{filename_output_full_base_png}")
    output_full_overlay = Image.open(f"{directory_main}/{filename_output_full_overlay_png}")

    width = 776
    height = output_full_overlay.height + 60

    output_full_final = Image.new("RGB", (width, height), (255, 255, 255))

    output_full_final.paste(output_full_base, (0,0))
    output_full_final.paste(output_full_overlay, (0,60))

    filename_output_full_temp = "output_full_temp.png"
    output_full_final.save(f"{directory_main}/{filename_output_full_temp}")

    # Add padding
    right = blueprint_user["doc_pad_h"]
    left = blueprint_user["doc_pad_h"]
    top = blueprint_user["doc_pad_v"]
    bottom = blueprint_user["doc_pad_v"]
    color = blueprint_user["doc_fill_color"]
    filename_output_browser_final = "output_full_final.png"
    get_output_padded(directory_main, filename_output_full_temp, filename_output_browser_final, right, left, top, bottom, color)
    print("OUTPUT_FULL - final - generated.")

    # Delete temp files
    cleanup(directory_main, filename_output_full_base_svg)
    cleanup(directory_main, filename_output_full_base_png)
    cleanup(directory_main, filename_output_full_overlay_png)
    cleanup(directory_main, filename_output_full_temp)

    return 1


def get_output_full_base(blueprint, directory_main, svg, svg_filename, png_filename):

    # Create SVG file
    with open(f"{directory_main}/{svg_filename}", "w") as file:
        file.write(svg)

    # Convert to SVG to PNG
    svg2png(url=f"{directory_main}/{svg_filename}", write_to=f"{directory_main}/{png_filename}", background_color=blueprint["doc_fill_color"])

    return 1


def get_output_full_overlay_resized(blueprint, directory_main, directory_screenshots, filename_input, filename_output):

    image = Image.open(f"{directory_screenshots}/{filename_input}")

    aspect_ratio = image.height / image.width 

    new_height = int(blueprint["width_small"] * aspect_ratio)

    # Resize the image
    resized_image = image.resize((blueprint["width_small"], new_height))

    resized_image.save(f"{directory_main}/{filename_output}")

    return 1


def get_output_full_overlay_bordered(blueprint, directory_main, filename_input):

    # Open the PNG image
    image = Image.open(f"{directory_main}/{filename_input}")

    # Set the border width and color
    border_width = 4
    border_color = blueprint["base_stroke_color"]

    # Add the border to the image
    image_with_border = ImageOps.expand(image, border=border_width, fill=border_color)

    # Save the image with the border
    image_with_border.save(f"{directory_main}/{filename_input}")

    return 1


