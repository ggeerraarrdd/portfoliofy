from PIL import Image, ImageDraw, ImageOps
from cairosvg import svg2png
from textwrap import dedent
from helpers import get_screenshot_resized, get_screenshot_resized_overlaid, get_output_padded, cleanup


def process_request_mobiles(blueprint_user, blueprint_system, directory_main, directory_screenshots):

    tablet = blueprint_system.get("tablet")
    smartphone = blueprint_system.get("smartphone")

    # ################################################## #
    # Handle OUTPUT_MOBILES - tablet
    # ################################################## #

    # Set svg for tablet
    svg_tablet = dedent(dedent(dedent(f'''\
        <?xml version="1.0" encoding="UTF-8"?>
        <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
        <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" width="1085px"
            height="1406px" viewBox="-0.5 -0.5 1085 1406" style="background-color: {blueprint_user["doc_fill_color"]}">
            <defs />
            <g>
                <rect x="2" y="2" width="1080" height="1400" rx="43.2" ry="43.2" fill="{blueprint_user["base_fill_color"]}" stroke="{blueprint_user["base_stroke_color"]}"
                    stroke-width="5" pointer-events="all" />
                <rect x="34" y="35.5" width="1016" height="1336" rx="20.32" ry="20.32" fill="{blueprint_user["doc_fill_color"]}" stroke="none"
                    pointer-events="all" />
            </g>
        </svg>'''
    )))

    # Create base - tablet
    filename_output_mobiles_tablet_base_svg = "output_mobiles_tablet_base.svg"
    filename_output_mobiles_tablet_base_png = "output_mobiles_tablet_base.png"
    get_output_mobiles_base(blueprint_user, directory_main, svg_tablet, filename_output_mobiles_tablet_base_svg, filename_output_mobiles_tablet_base_png)
    # print("OUTPUT_MOBILES - tablet - base - generated.")

    # Create overlay - tablet - temp
    filename_input = tablet["filename_large"]
    filename_output_temp = filename_output_mobiles_tablet_overlay_temp_png = "output_mobiles_tablet_overlay_temp.png"
    new_width = tablet["width_medium"]
    height_crop = tablet["medium_height_crop"]
    get_screenshot_resized(directory_main, directory_screenshots, filename_input, filename_output_temp, new_width, height_crop)
    # print("OUTPUT_MOBILES - tablet - overlay - generated.")

    # Create overlay - tablet - final
    filename_output_final = filename_output_mobiles_tablet_overlay_final_png = "output_mobiles_tablet_overlay_final.png"
    get_output_mobiles_overlay_temp(directory_main, filename_output_mobiles_tablet_overlay_temp_png, filename_output_final)

    # Combine base layer and overlay
    base = f"{directory_main}/{filename_output_mobiles_tablet_base_png}"
    overlay = f"{directory_main}/{filename_output_mobiles_tablet_overlay_final_png}"
    lat = 34
    lng = 36
    filename_output_mobiles_tablet_final = "output_mobiles_tablet_final.png"
    get_output_mobiles_overlay_final(base, overlay, lat, lng, directory_main, filename_output_mobiles_tablet_final)
    # print("OUTPUT_BROWSER - tablet - temp - generated.")


    # ################################################## #
    # Handle OUTPUT_MOBILES - smartphone
    # ################################################## #

    # Set svg for smartphone
    svg_smartphone = dedent(dedent(dedent(f'''\
        <?xml version="1.0" encoding="UTF-8"?>
        <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
        <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" width="405px"
            height="806px" viewBox="-0.5 -0.5 405 806" style="background-color: {blueprint_user["doc_fill_color"]}">
            <defs />
            <g>
                <rect x="2" y="2" width="400" height="800" rx="44" ry="44" fill="{blueprint_user["base_fill_color"]}" stroke="{blueprint_user["base_stroke_color"]}" stroke-width="5"
                    pointer-events="all" />
                <rect x="22" y="22" width="360" height="760" rx="28.8" ry="28.8" fill="{blueprint_user["doc_fill_color"]}" stroke="none"
                    pointer-events="all" />
            </g>
        </svg>'''
    )))

    # Create base - smartphone
    filename_output_mobiles_smartphone_base_svg = "output_mobiles_smartphone_base.svg"
    filename_output_mobiles_smartphone_base_png = "output_mobiles_smartphone_base.png"
    get_output_mobiles_base(blueprint_user, directory_main, svg_smartphone, filename_output_mobiles_smartphone_base_svg, filename_output_mobiles_smartphone_base_png)
    # print("OUTPUT_MOBILES - smartphone - base - generated.")

    # Create overlay - smartphone - temp
    filename_input = smartphone["filename_large"]
    filename_output_temp = filename_output_mobiles_smartphone_overlay_temp_png = "output_mobiles_smartphone_overlay_temp.png"
    new_width = smartphone["width_medium"]
    height_crop = smartphone["medium_height_crop"]
    get_screenshot_resized(directory_main, directory_screenshots, filename_input, filename_output_temp, new_width, height_crop)
    # print("OUTPUT_MOBILES - smartphone - overlay - generated.")

    # Create overlay - smartphone - final
    filename_output_final = filename_output_mobiles_smartphone_overlay_final_png = "output_mobiles_smartphone_overlay_final.png"
    get_output_mobiles_overlay_temp(directory_main, filename_output_mobiles_smartphone_overlay_temp_png, filename_output_final)

    # Combine base layer and overlay
    base = f"{directory_main}/{filename_output_mobiles_smartphone_base_png}"
    overlay = f"{directory_main}/{filename_output_mobiles_smartphone_overlay_final_png}"
    lat = 22
    lng = 23
    filename_output_mobiles_smartphone_final = "output_mobiles_smartphone_final.png"
    get_output_mobiles_overlay_final(base, overlay, lat, lng, directory_main, filename_output_mobiles_smartphone_final)
    # print("OUTPUT_BROWSER - smartphone - temp - generated.")


    # ################################################## #
    # Handle OUTPUT_MOBILES - all temp
    # ################################################## #

    width = 1605
    height = 1406

    output_mobiles_all_base = Image.new(mode="RGB", size=(width, height), color=f"{blueprint_user['doc_fill_color']}")

    output_mobiles_tablet = Image.open(f"{directory_main}/{filename_output_mobiles_tablet_final}")
    output_mobiles_smartphone = Image.open(f"{directory_main}/{filename_output_mobiles_smartphone_final}")

    output_mobiles_tablet_box = (520, 0)
    output_mobiles_all_base.paste(output_mobiles_tablet, output_mobiles_tablet_box)

    output_mobiles_smartphone_box = (0, 600)
    output_mobiles_all_base.paste(output_mobiles_smartphone, output_mobiles_smartphone_box)

    filename_output_mobiles_all_temp = "output_mobiles_all_temp.png"
    output_mobiles_all_base.save(f"{directory_main}/{filename_output_mobiles_all_temp}")

    # print("OUTPUT_MOBILES - all - temp - generated.")


    # ################################################## #
    # Handle OUTPUT_MOBILES - all final
    # ################################################## #

    # Add padding
    right = blueprint_user["doc_pad_h"]
    left = blueprint_user["doc_pad_h"]
    top = blueprint_user["doc_pad_v"]
    bottom = blueprint_user["doc_pad_v"]
    color = blueprint_user["doc_fill_color"]
    filename_output_mobiles_final = "output_mobiles.png"
    get_output_padded(directory_main, filename_output_mobiles_all_temp, filename_output_mobiles_final, right, left, top, bottom, color)
    # print("OUTPUT_MOBILES - final - generated.")


    # ################################################## #
    # Delete temp files
    # ################################################## #

    cleanup(directory_main, filename_output_mobiles_tablet_base_svg)
    cleanup(directory_main, filename_output_mobiles_tablet_base_png)
    cleanup(directory_main, filename_output_mobiles_tablet_overlay_temp_png)
    cleanup(directory_main, filename_output_mobiles_tablet_overlay_final_png)

    cleanup(directory_main, filename_output_mobiles_smartphone_base_svg)
    cleanup(directory_main, filename_output_mobiles_smartphone_base_png)
    cleanup(directory_main, filename_output_mobiles_smartphone_overlay_temp_png)
    cleanup(directory_main, filename_output_mobiles_smartphone_overlay_final_png)

    cleanup(directory_main, filename_output_mobiles_tablet_final)
    cleanup(directory_main, filename_output_mobiles_smartphone_final)
    cleanup(directory_main, filename_output_mobiles_all_temp)

    return 1


def get_output_mobiles_base(blueprint, directory_main, svg, svg_filename, png_filename):

    # Create SVG file
    with open(f"{directory_main}/{svg_filename}", "w") as file:
        file.write(svg)

    # Convert to SVG to PNG
    svg2png(url=f"{directory_main}/{svg_filename}", write_to=f"{directory_main}/{png_filename}", background_color=blueprint["doc_fill_color"])

    return 1


def get_output_mobiles_overlay_temp(directory_path, filename_input, filename_output):

    # Open the image
    image = Image.open(f"{directory_path}/{filename_input}")

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

    image_with_border.save(f"{directory_path}/{filename_output}")

    return 1


def get_output_mobiles_overlay_final(base, overlay, lat, lng, directory_main, filename_output):

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
    