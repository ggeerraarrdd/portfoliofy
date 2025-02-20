"""
TD
"""

# Python Standard Libraries
from datetime import datetime
from io import BytesIO
import os
from textwrap import dedent

# Third-Party Libraries
from moviepy.editor import ImageClip, CompositeVideoClip
from PIL import Image
from cairosvg import svg2png
import numpy as np

# Local
from api.core.config import settings_devices
from api.core.utils import get_screenshot_full
from api.core.utils import get_base
from api.core.utils import get_final
from api.core.utils import cleanup










def process_request_movie(post):
    """
    TD
    """
    # ################################################## #
    # Get system settings for full
    # ################################################## #
    movie = settings_devices.get("movie")

    # ################################################## #
    # Get screenshot
    # ################################################## #
    screenshot_movie = get_screenshot_full(str(post["remote_url"]),
                                           post["wait"])

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
    base_movie = get_base(post, svg)

    # ################################################## #
    # Create movie - overlay
    # Create movie - final (temp)
    # ################################################## #
    # None


    # ################################################## #
    # Create movie - final
    # ################################################## #
    final_movie = get_final(base_movie, post)


    # ################################################## #
    # Create movie - clip
    # ################################################## #

    # Load and process both images in sequence using same BytesIO object
    with BytesIO() as bio:
        # Process movie clip from screenshot
        Image.open(BytesIO(screenshot_movie)).save(bio, format='PNG')
        image_for_movie_clip = Image.open(BytesIO(bio.getvalue()))
        aspect_ratio = image_for_movie_clip.height / image_for_movie_clip.width
        new_height = int(movie["width_large"] * aspect_ratio)
        image_for_movie_clip = image_for_movie_clip.resize((movie["width_large"], new_height))
        image_for_movie_clip = np.array(image_for_movie_clip)

        # Clear buffer
        bio.seek(0)
        bio.truncate()

        # Process movie bg_clip from base_movie (frame/window)
        Image.open(BytesIO(final_movie)).save(bio, format='PNG')
        image_for_movie_bg_clip = Image.open(BytesIO(bio.getvalue()))
        image_for_movie_bg_clip = np.array(image_for_movie_bg_clip)


    # Set max height limit to 10,000 [TBD]
    if new_height >= 20000:
        return 0

    else:
        clip = ImageClip(image_for_movie_clip)
        bg_clip = ImageClip(image_for_movie_bg_clip)

        scroll_speed = 180
        total_duration = (clip.h - 720)/scroll_speed

        fl = lambda gf,t : gf(t)[int(scroll_speed*t):int(scroll_speed*t)+720,:]
        clip = clip.fl(fl, apply_to=['mask'])

        video = CompositeVideoClip([bg_clip, clip.set_pos("center")])

        video.duration = total_duration

        # ################################################## #
        # Create directory
        # ################################################## #
        now = datetime.now()
        directory = now.strftime('%y%m%d_%H%M%S_%f')[:-3]
        directory = f"api/output/{directory}_movie"
        os.makedirs(directory)

        filename_output_video = "output_video.mp4"

        video.write_videofile(f"{directory}/{filename_output_video}", fps=26)

        # TD
        # Ensure accepted file extension
        # if not filename_output_video.endswith('.mp4'):
        #     output += '.mp4'


        return f"{directory}/{filename_output_video}"


def get_movie_base(blueprint, directory_main, svg_filename, png_filename):
    """
    TD
    """
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
    with open(f"{directory_main}/{svg_filename}", "w", encoding="utf-8") as file:
        file.write(svg)

    # Convert to SVG to PNG
    svg2png(url=f"{directory_main}/{svg_filename}", write_to=f"{directory_main}/{png_filename}", background_color=blueprint["doc_fill_color"])

    # Delete SVG file
    cleanup(directory_main, svg_filename)

    return 1
