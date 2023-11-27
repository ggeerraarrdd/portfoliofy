from moviepy.editor import ImageClip, CompositeVideoClip
from PIL import Image
from cairosvg import svg2png
from textwrap import dedent
from helpers import get_output_padded, cleanup


def process_request_video(blueprint_user, blueprint_system, directory_main, directory_screenshots):

    # Open image    
    image = Image.open(f"{directory_screenshots}/screenshot_full_large.png")

    # Calculate dimensions
    aspect_ratio = image.height / image.width 
    new_height = int(blueprint_system["width_large"] * aspect_ratio)

    # Set max height limit to 10,000 [TBD]
    if new_height >= 10000:
        return 0
    
    else:
        # Resize full-page screenshot
        filename_output_video_clip = "output_video_clip.png"
        resized_image = image.resize((blueprint_system["width_large"], new_height))
        resized_image.save(f"{directory_main}/{filename_output_video_clip}")

        # Get video base
        svg_filename = "output_video_base_temp.svg"
        png_filename = "output_video_base_temp.png"
        get_movie_base(blueprint_user, directory_main, svg_filename, png_filename)

        # Add padding
        right = blueprint_user["doc_pad_h"]
        left = blueprint_user["doc_pad_h"]
        top = blueprint_user["doc_pad_v"]
        bottom = blueprint_user["doc_pad_v"]
        color = blueprint_user["doc_fill_color"]
        filename_output_video_base_final = "output_video_base_final.png"
        get_output_padded(directory_main, png_filename, filename_output_video_base_final, right, left, top, bottom, color)

        # Create video
        filename_output_video = "output_video.mp4"

        clip = ImageClip(f"{directory_main}/{filename_output_video_clip}")

        bg_clip = ImageClip(f"{directory_main}/{filename_output_video_base_final}")

        scroll_speed = 180
        total_duration = (clip.h - 720)/scroll_speed

        fl = lambda gf,t : gf(t)[int(scroll_speed*t):int(scroll_speed*t)+720,:]
        clip = clip.fl(fl, apply_to=['mask'])

        video = CompositeVideoClip([bg_clip, clip.set_pos("center")])
        video.duration = total_duration
        if not filename_output_video.endswith('.mp4'):
            output += '.mp4'
        video.write_videofile(f"{directory_main}/{filename_output_video}", fps=26)

        cleanup(directory_main, filename_output_video_clip)
        cleanup(directory_main, png_filename)
        cleanup(directory_main, filename_output_video_base_final)

        return 1


def get_movie_base(blueprint, directory_main, svg_filename, png_filename):

    svg = dedent(dedent(dedent(f'''\
        <?xml version="1.0" encoding="UTF-8"?>
        <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
        <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" width="1288px"
            height="808px" viewBox="-0.5 -0.5 1288 808" style="background-color: rgb(255, 255, 255);">
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
