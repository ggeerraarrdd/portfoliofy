from cairosvg import svg2png
from textwrap import dedent
from helpers import get_screenshot_resized, get_screenshot_resized_overlaid, get_output_padded, cleanup


def process_request_browser(blueprint_user, blueprint_system, directory_main, directory_screenshots):

    # Create PNG base layer
    filename_output_browser_base_svg = "output_browser_base.svg"
    filename_output_browser_base_png = "output_browser_base.png"
    get_browser_base(blueprint_user, directory_main, filename_output_browser_base_svg, filename_output_browser_base_png)
    print("OUTPUT_BROWSER - base - generated.")

    # Create PNG overlay
    filename_input = blueprint_system["filename_large"]
    filename_output = filename_output_browser_overlay_png = "output_browser_overlay.png"
    new_width = blueprint_system["width_medium"]
    height_crop = blueprint_system["medium_height_crop"]
    get_screenshot_resized(directory_main, directory_screenshots, filename_input, filename_output, new_width, height_crop)
    print("OUTPUT_BROWSER - overlay - generated.")

    # Combine base layer and overlay
    base = f"{directory_main}/{filename_output_browser_base_png}"
    overlay = f"{directory_main}/{filename_output_browser_overlay_png}"
    lat = 4
    lng = 64
    filename_output_browser_final_temp = "output_browser_temp.png"
    get_screenshot_resized_overlaid(base, overlay, lat, lng, directory_main, filename_output_browser_final_temp)
    print("OUTPUT_BROWSER - temp - generated.")

    # Add padding
    right = blueprint_user["doc_pad_h"]
    left = blueprint_user["doc_pad_h"]
    top = blueprint_user["doc_pad_v"]
    bottom = blueprint_user["doc_pad_v"]
    color = blueprint_user["doc_fill_color"]
    filename_output_browser_final = "output_browser_final.png"
    get_output_padded(directory_main, filename_output_browser_final_temp, filename_output_browser_final, right, left, top, bottom, color)
    print("OUTPUT_BROWSER - final - generated.")

    # Delete temp files
    cleanup(directory_main, filename_output_browser_base_png)
    cleanup(directory_main, filename_output_browser_overlay_png)
    cleanup(directory_main, filename_output_browser_final_temp)

    return 1

 
def get_browser_base(blueprint, directory_main, svg_filename, png_filename):

    svg = dedent(dedent(dedent(f'''\
        <?xml version="1.0" encoding="UTF-8"?>
        <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
        <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" 
            width="2056px" height="1220px" viewBox="-0.5 -0.5 2056 1220"
            style="background-color: {blueprint["doc_fill_color"]};">
            <defs />
            <g>
                <rect x="2" y="1" width="2052" height="130" rx="19.5" ry="19.5" fill="{blueprint["base_fill_color"]}" stroke="{blueprint["base_stroke_color"]}" stroke-width="4"
                    pointer-events="all" />
                <rect x="2" y="61" width="2052" height="1156" fill="{blueprint["doc_fill_color"]}" stroke="{blueprint["base_stroke_color"]}" stroke-width="4"
                    pointer-events="all" />
                <ellipse cx="44" cy="33" rx="12" ry="12" fill="{blueprint["doc_fill_color"]}" stroke="{blueprint["base_stroke_color"]}" stroke-width="2"
                    pointer-events="all" />
                <ellipse cx="84" cy="33" rx="12" ry="12" fill="{blueprint["doc_fill_color"]}" stroke="{blueprint["base_stroke_color"]}" stroke-width="2"
                    pointer-events="all" />
                <ellipse cx="124" cy="33" rx="12" ry="12" fill="{blueprint["doc_fill_color"]}" stroke="{blueprint["base_stroke_color"]}" stroke-width="2"
                    pointer-events="all" />
            </g>
        </svg>'''
    )))

    # Create SVG file
    with open(f"{directory_main}/{svg_filename}", "w") as file:
        file.write(svg)
    
    # Convert to SVG to PNG
    svg2png(url=f"{directory_main}/{svg_filename}", write_to=f"{directory_main}/{png_filename}", background_color=blueprint["doc_fill_color"])

    # Delete SVG file
    cleanup(directory_main, svg_filename)

    return 1
