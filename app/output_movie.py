import os
from datetime import datetime
from moviepy.editor import ImageClip, CompositeVideoClip
from PIL import Image
from cairosvg import svg2png
from textwrap import dedent
from app.settings import settings_devices
from app.helpers import get_screenshot_full, get_base, get_overlay, get_final_temp, get_final, cleanup


def process_request_movie(post):

    # ################################################## #
    # Get system settings for full
    # ################################################## #
    full = settings_devices.get("full")
    movie = settings_devices.get("movie")

    # ################################################## #
    # Create directory
    # ################################################## #
    now = datetime.now()
    directory = now.strftime('%y%m%d_%H%M%S_%f')[:-3]
    directory = f"app/output/{directory}_movie"
    os.makedirs(directory)

    # ################################################## #
    # Get screenshot
    # ################################################## #
    get_screenshot_full(str(post["remote_url"]), 
                   post["wait"], 
                   directory, 
                   full)
    
    # ################################################## #
    # Create movie - start validation
    # ################################################## #

    # Open image    
    image = Image.open(f"{directory}/screenshot_full_large.png")

    # Calculate dimensions
    aspect_ratio = image.height / image.width 
    new_height = int(movie["width_large"] * aspect_ratio)

    # Set max height limit to 10,000 [TBD]
    if new_height >= 20000:
        return 0
    
    else:
        # ################################################## #
        # Create movie - base
        # ################################################## #
        svg = dedent(dedent(dedent(f'''\
            <?xml version="1.0" encoding="UTF-8"?>
            <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
            <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" width="1288px"
                height="808px" viewBox="-0.5 -0.5 1288 808" style="background-color: {post["doc_fill_color"]};">
                <defs />
                <g>
                    <rect x="2" y="2" width="1284" height="50" rx="7.5" ry="7.5" fill="{post["base_fill_color"]}" stroke="{post["base_stroke_color"]}"
                        stroke-width="4" pointer-events="all" />
                    <rect x="0" y="40" width="1288" height="728" fill="{post["base_stroke_color"]}" stroke="none" pointer-events="all" />
                    <ellipse cx="65" cy="22" rx="6" ry="6" fill="{post["doc_fill_color"]}" stroke="{post["base_stroke_color"]}" stroke-width="2"
                        pointer-events="all" />
                    <ellipse cx="45" cy="22" rx="6" ry="6" fill="{post["doc_fill_color"]}" stroke="{post["base_stroke_color"]}" stroke-width="2"
                        pointer-events="all" />
                    <ellipse cx="25" cy="22" rx="6" ry="6" fill="{post["doc_fill_color"]}" stroke="{post["base_stroke_color"]}" stroke-width="2"
                        pointer-events="all" />
                    <rect x="0" y="768" width="1288" height="40" fill="{post["doc_fill_color"]}" stroke="none" pointer-events="all" />
                </g>
            </svg>'''
        )))

        fname_out_movie_base_svg = "out_movie_base.svg"
        fname_out_movie_base_png = "out_movie_base.png"
        get_base(post, 
                 directory, 
                 svg,
                 fname_out_movie_base_svg, 
                 fname_out_movie_base_png)

        fname_out_movie_base_final = "out_movie_base_final.png"
        get_final(directory, 
                  fname_out_movie_base_png, 
                  fname_out_movie_base_final, 
                  post)

        # ################################################## #
        # Create movie - clip
        # ################################################## #
        fname_out_movie_clip_final = "out_movie_clip_final.png"
        resized_image = image.resize((movie["width_large"], new_height))
        resized_image.save(f"{directory}/{fname_out_movie_clip_final}")

        # ################################################## #
        # Create movie - clip
        # ################################################## #
        filename_output_video = "output_video.mp4"

        clip = ImageClip(f"{directory}/{fname_out_movie_clip_final}")

        bg_clip = ImageClip(f"{directory}/{fname_out_movie_base_final}")

        scroll_speed = 180
        total_duration = (clip.h - 720)/scroll_speed

        fl = lambda gf,t : gf(t)[int(scroll_speed*t):int(scroll_speed*t)+720,:]
        clip = clip.fl(fl, apply_to=['mask'])

        video = CompositeVideoClip([bg_clip, clip.set_pos("center")])
        video.duration = total_duration
        if not filename_output_video.endswith('.mp4'):
            output += '.mp4'
        video.write_videofile(f"{directory}/{filename_output_video}", fps=26)

        # ################################################## #
        # Clean up
        # ################################################## #
        cleanup(directory, full["filename_large"])
        cleanup(directory, fname_out_movie_base_png)
        cleanup(directory, fname_out_movie_base_final)
        cleanup(directory, fname_out_movie_clip_final)
        
        return f"{directory}/{filename_output_video}"


def get_movie_base(blueprint, directory_main, svg_filename, png_filename):

    svg = dedent(dedent(dedent(f'''\
        <?xml version="1.0" encoding="UTF-8"?>
        <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
        <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" width="1288px"
            height="808px" viewBox="-0.5 -0.5 1288 808" style="background-color: {blueprint["doc_fill_color"]};">
            <defs />
            <g>
                <rect x="2" y="2" width="1284" height="50" rx="7.5" ry="7.5" fill="{blueprint["base_fill_color"]}" stroke="{blueprint["base_stroke_color"]}"
                    stroke-width="4" pointer-events="all" />
                <rect x="0" y="40" width="1288" height="728" fill="{blueprint["base_stroke_color"]}" stroke="none" pointer-events="all" />
                <ellipse cx="65" cy="22" rx="6" ry="6" fill="{blueprint["doc_fill_color"]}" stroke="{blueprint["base_stroke_color"]}" stroke-width="2"
                    pointer-events="all" />
                <ellipse cx="45" cy="22" rx="6" ry="6" fill="{blueprint["doc_fill_color"]}" stroke="{blueprint["base_stroke_color"]}" stroke-width="2"
                    pointer-events="all" />
                <ellipse cx="25" cy="22" rx="6" ry="6" fill="{blueprint["doc_fill_color"]}" stroke="{blueprint["base_stroke_color"]}" stroke-width="2"
                    pointer-events="all" />
                <rect x="0" y="768" width="1288" height="40" fill="{blueprint["doc_fill_color"]}" stroke="none" pointer-events="all" />
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
