from PIL import Image
from cairosvg import svg2png
from textwrap import dedent
from helpers import get_screenshot_resized, get_screenshot_resized_overlaid, get_output_padded, cleanup


def process_request_main(blueprint_user, blueprint_system, directory_main, directory_screenshots):

    desktop = blueprint_system.get("desktop")
    laptop = blueprint_system.get("laptop")
    tablet = blueprint_system.get("tablet")
    smartphone = blueprint_system.get("smartphone")


    # ################################################## #
    # Handle OUTPUT_MAIN - desktop
    # ################################################## #

    # Create base - desktop
    filename_output_main_desktop_base_svg = "output_main_desktop_base.svg"
    filename_output_main_desktop_base_png = "output_main_desktop_base.png"
    get_main_desktop_final(blueprint_user, directory_main, filename_output_main_desktop_base_svg, filename_output_main_desktop_base_png)
    # print("OUTPUT_MAIN - desktop - base - generated.")

    # Create overlay - desktop
    filename_input = desktop["filename_large"]
    filename_output = filename_output_main_desktop_overlay_png = "output_main_desktop_overlay.png"
    new_width = desktop["width_small"]
    height_crop = desktop["small_height_crop"]
    get_screenshot_resized(directory_main, directory_screenshots, filename_input, filename_output, new_width, height_crop)
    # print("OUTPUT_MAIN - desktop - overlay - generated.")

    # Combine base and overlay - desktop
    base = f"{directory_main}/{filename_output_main_desktop_base_png}"
    overlay = f"{directory_main}/{filename_output_main_desktop_overlay_png}"
    lat = 74
    lng = 74
    filename_output_main_desktop_final = "output_main_desktop_final.png"
    get_screenshot_resized_overlaid(base, overlay, lat, lng, directory_main, filename_output_main_desktop_final)
    # print("OUTPUT_MAIN - desktop - final - generated.")

    # Delete temp files - desktop
    cleanup(directory_main, filename_output_main_desktop_base_png)
    cleanup(directory_main, filename_output_main_desktop_overlay_png)


    # ################################################## #
    # Handle OUTPUT_MAIN - laptop
    # ################################################## #

    # Create base - laptop
    filename_output_main_laptop_base_svg = "output_main_laptop_base.svg"
    filename_output_main_laptop_base_png = "output_main_laptop_base.png"
    get_main_laptop_final(blueprint_user, directory_main, filename_output_main_laptop_base_svg, filename_output_main_laptop_base_png)
    # print("OUTPUT_MAIN - laptop - base - generated.")

    # Create overlay - laptop
    filename_input = laptop["filename_large"]
    filename_output = filename_output_main_laptop_overlay_png = "output_main_laptop_overlay.png"
    new_width = laptop["width_small"]
    height_crop = laptop["small_height_crop"]
    get_screenshot_resized(directory_main, directory_screenshots, filename_input, filename_output, new_width, height_crop)
    # print("OUTPUT_MAIN - laptop - overlay - generated.")

    # Combine base and overlay - laptop
    base = f"{directory_main}/{filename_output_main_laptop_base_png}"
    overlay = f"{directory_main}/{filename_output_main_laptop_overlay_png}"
    lat = 34
    lng = 34
    filename_output_main_laptop_final = "output_main_laptop_final.png"
    get_screenshot_resized_overlaid(base, overlay, lat, lng, directory_main, filename_output_main_laptop_final)
    # print("OUTPUT_MAIN - laptop - final - generated.")

    # Delete temp files - laptop
    cleanup(directory_main, filename_output_main_laptop_base_png)
    cleanup(directory_main, filename_output_main_laptop_overlay_png)


    # ################################################## #
    # Handle MAIN_OUTPUT - tablet
    # ################################################## #

    # Create base - tablet
    filename_output_main_tablet_base_svg = "output_main_tablet_base.svg"
    filename_output_main_tablet_base_png = "output_main_tablet_base.png"
    get_main_tablet_final(blueprint_user, directory_main, filename_output_main_tablet_base_svg, filename_output_main_tablet_base_png)
    # print("OUTPUT_MAIN - tablet - base - generated.")

    # Create overlay - tablet
    filename_input = tablet["filename_large"]
    filename_output = filename_output_main_tablet_overlay_png = "output_main_tablet_overlay.png"
    new_width = tablet["width_small"]
    height_crop = tablet["small_height_crop"]
    get_screenshot_resized(directory_main, directory_screenshots, filename_input, filename_output, new_width, height_crop)
    # print("OUTPUT_MAIN - tablet - overlay - generated.")

    # Combine base and overlay - tablet
    base = f"{directory_main}/{filename_output_main_tablet_base_png}"
    overlay = f"{directory_main}/{filename_output_main_tablet_overlay_png}"
    lat = 34
    lng = 34
    filename_output_main_tablet_final = "output_main_tablet_final.png"
    get_screenshot_resized_overlaid(base, overlay, lat, lng, directory_main, filename_output_main_tablet_final)
    # print("OUTPUT_MAIN - tablet - final - generated.")

    # Delete temp files - tablet
    cleanup(directory_main, filename_output_main_tablet_base_png)
    cleanup(directory_main, filename_output_main_tablet_overlay_png)


    # ################################################## #
    # Handle OUTPUT_MAIN - smartphone
    # ################################################## #    

    # Create base - smartphone
    filename_output_main_smartphone_base_svg = "output_main_smartphone_base.svg"
    filename_output_main_smartphone_base_png = "output_main_smartphone_base.png"
    get_main_smartphone_final(blueprint_user, directory_main, filename_output_main_smartphone_base_svg, filename_output_main_smartphone_base_png)
    # print("OUTPUT_MAIN - smartphone - base - generated.")

    # Create overlay - smartphone
    filename_input = smartphone["filename_large"]
    filename_output = filename_output_main_smartphone_overlay_png = "output_main_smartphone_overlay.png"
    new_width = smartphone["width_small"]
    height_crop = smartphone["small_height_crop"]
    get_screenshot_resized(directory_main, directory_screenshots, filename_input, filename_output, new_width, height_crop)
    # print("OUTPUT_MAIN - smartphone - overlay - generated.")

    # Combine base and overlay - smartphone
    base = f"{directory_main}/{filename_output_main_smartphone_base_png}"
    overlay = f"{directory_main}/{filename_output_main_smartphone_overlay_png}"
    lat = 24
    lng = 24
    filename_output_main_smartphone_final = "output_main_smartphone_final.png"
    get_screenshot_resized_overlaid(base, overlay, lat, lng, directory_main, filename_output_main_smartphone_final)
    # print("OUTPUT_MAIN - smartphone - final - generated.")

    # Delete temp files - smartphone
    cleanup(directory_main, filename_output_main_smartphone_base_png)
    cleanup(directory_main, filename_output_main_smartphone_overlay_png)


    # ################################################## #
    # Handle OUTPUT_MAIN - all temp
    # ################################################## #   

    width = 3176
    height = 1515

    output_main_all_base = Image.new("RGB", (width, height), (255, 255, 255))

    output_main_desktop = Image.open(f"{directory_main}/{filename_output_main_desktop_final}")
    output_main_laptop = Image.open(f"{directory_main}/{filename_output_main_laptop_final}")
    output_main_tablet = Image.open(f"{directory_main}/{filename_output_main_tablet_final}")
    output_main_smartphone = Image.open(f"{directory_main}/{filename_output_main_smartphone_final}")

    output_main_desktop_box = (750, 0)
    output_main_all_base.paste(output_main_desktop, output_main_desktop_box)

    output_main_laptop_box = (0, 700)
    output_main_all_base.paste(output_main_laptop, output_main_laptop_box)

    output_main_tablet_box = (2410, 650)
    output_main_all_base.paste(output_main_tablet, output_main_tablet_box)

    output_main_smartphone_box = (2900, 980)
    output_main_all_base.paste(output_main_smartphone, output_main_smartphone_box)

    filename_output_main_all_temp = "output_main_all_temp.png"
    output_main_all_base.save(f"{directory_main}/{filename_output_main_all_temp}")

    # print("OUTPUT_MAIN - all - temp - generated.")


    # ################################################## #
    # Handle OUTPUT_MAIN - all final
    # ################################################## #  

    # Add padding
    right = blueprint_user["doc_pad_h"]
    left = blueprint_user["doc_pad_h"]
    top = blueprint_user["doc_pad_v"]
    bottom = blueprint_user["doc_pad_v"]
    color = blueprint_user["doc_fill_color"]
    filename_output_main_all_final = "output_main_final.png"
    get_output_padded(directory_main, filename_output_main_all_temp, filename_output_main_all_final, right, left, top, bottom, color)

    # print("OUTPUT_MAIN - all - final - generated.")


    # ################################################## #
    # Delete temp files
    # ################################################## #  

    cleanup(directory_main, filename_output_main_desktop_final)
    cleanup(directory_main, filename_output_main_laptop_final)
    cleanup(directory_main, filename_output_main_tablet_final)
    cleanup(directory_main, filename_output_main_smartphone_final)
    cleanup(directory_main, filename_output_main_all_temp)

    return 1
 

def get_main_desktop_final(blueprint, directory_main, svg_filename, png_filename):

    svg = dedent(dedent(f'''\
        <?xml version="1.0" encoding="UTF-8"?>
        <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
        <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" 
            width="2065px" height="1515px" viewBox="-0.5 -0.5 2065 1515" 
            style="background-color: {blueprint["doc_fill_color"]};">
            <defs />
            <g>
                <rect x="2" y="2" width="2060" height="1220" rx="24.4" ry="24.4" fill="{blueprint["base_fill_color"]}" stroke="{blueprint["base_stroke_color"]}"
                    stroke-width="5" pointer-events="all" />
                <rect x="72" y="72" width="1923" height="1083" fill="{blueprint["doc_fill_color"]}" stroke="rgb(0, 0, 0)" stroke-width="3"
                    pointer-events="all" />
                <rect x="872" y="1222" width="320" height="270" fill="{blueprint["base_fill_color"]}" stroke="{blueprint["base_stroke_color"]}" stroke-width="5"
                    pointer-events="all" />
                <rect x="872" y="1492" width="320" height="20" fill="{blueprint["base_fill_color"]}" stroke="{blueprint["base_stroke_color"]}" stroke-width="5"
                    pointer-events="all" />
            </g>
        </svg>'''
    ))

    # Create SVG file
    with open(f"{directory_main}/{svg_filename}", "w") as file:
        file.write(svg)
    
    # Convert to SVG to PNG
    svg2png(url=f"{directory_main}/{svg_filename}", write_to=f"{directory_main}/{png_filename}", background_color=blueprint["doc_fill_color"])

    # Delete SVG file
    cleanup(directory_main, svg_filename)

    return 1
    

def get_main_laptop_final(blueprint, directory_main, svg_filename, png_filename):

    svg = dedent(dedent(f'''\
        <?xml version="1.0" encoding="UTF-8"?>
        <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
        <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" 
            width="1345px" height="815px" viewBox="-0.5 -0.5 1345 815" 
            style="background-color: {blueprint["doc_fill_color"]};">
            <defs />
            <g>
                <rect x="2" y="2" width="1340" height="780" rx="15.6" ry="15.6" fill="{blueprint["base_fill_color"]}" stroke="{blueprint["base_stroke_color"]}" stroke-width="5"
                    pointer-events="all" />
                <rect x="32" y="32" width="1283" height="723" fill="rgb(255, 255, 255)" stroke="rgb(0, 0, 0)" stroke-width="3"
                    pointer-events="all" />
                <rect x="2" y="782" width="1340" height="30" rx="4.5" ry="4.5" fill="{blueprint["base_fill_color"]}" stroke="{blueprint["base_stroke_color"]}" stroke-width="5"
                    pointer-events="all" />
            </g>
        </svg>'''
    ))

    # Create SVG file
    with open(f"{directory_main}/{svg_filename}", "w") as file:
        file.write(svg)
    
    # Convert to SVG to PNG
    svg2png(url=f"{directory_main}/{svg_filename}", write_to=f"{directory_main}/{png_filename}", background_color=blueprint["doc_fill_color"])

    # Delete SVG file
    cleanup(directory_main, svg_filename)

    return 1


def get_main_tablet_final(blueprint, directory_main, svg_filename, png_filename):

    svg = dedent(dedent(f'''\
        <?xml version="1.0" encoding="UTF-8"?>
        <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
        <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" 
            width="665px" height="865px" viewBox="-0.5 -0.5 665 865">
            <defs />
            <g>
                <rect x="2" y="2" width="660" height="860" rx="13.2" ry="13.2" fill="{blueprint["base_fill_color"]}" stroke="{blueprint["base_stroke_color"]}" stroke-width="5"
                    pointer-events="all" />
                <rect x="32" y="32" width="603" height="803" fill="rgb(255, 255, 255)" stroke="rgb(0, 0, 0)" stroke-width="4"
                    pointer-events="all" />
            </g>
        </svg>'''
    ))

    # Create SVG file
    with open(f"{directory_main}/{svg_filename}", "w") as file:
        file.write(svg)
    
    # Convert to SVG to PNG
    svg2png(url=f"{directory_main}/{svg_filename}", write_to=f"{directory_main}/{png_filename}", background_color=blueprint["doc_fill_color"])

    # Delete SVG file
    cleanup(directory_main, svg_filename)

    return 1


def get_main_smartphone_final(blueprint, directory_main, svg_filename, png_filename):

    svg = dedent(dedent(f'''\
        <?xml version="1.0" encoding="UTF-8"?>
        <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
        <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" 
            width="275px" height="535px" viewBox="-0.5 -0.5 275 535">
            <defs />
            <g>
                <rect x="2" y="2" width="270" height="530" rx="10.8" ry="10.8" fill="{blueprint["base_fill_color"]}" stroke="{blueprint["base_stroke_color"]}" stroke-width="5"
                    pointer-events="all" />
                <rect x="22" y="22" width="233" height="493" fill="rgb(255, 255, 255)" stroke="rgb(0, 0, 0)" stroke-width="3"
                    pointer-events="all" />
            </g>
        </svg>'''
    ))

    # Create SVG file
    with open(f"{directory_main}/{svg_filename}", "w") as file:
        file.write(svg)
    
    # Convert to SVG to PNG
    svg2png(url=f"{directory_main}/{svg_filename}", write_to=f"{directory_main}/{png_filename}", background_color=blueprint["doc_fill_color"])

    # Delete SVG file
    cleanup(directory_main, svg_filename)

    return 1
