user_input = {
    "url": "https://www.nps.gov/",
    "wait": 2,
    "output_main": {
        "request": True,
        "format": "png",
        "doc_pad_h": 300,
        "doc_pad_v": 200,
        "doc_fill_color": "#FFFFFF",
        "base_stroke_color": "#23445D",
        "base_fill_color": "#BAC8D3",
        "screenshots": True,
    },
    "output_browser": {
        "request": True,
        "format": "png",
        "doc_pad_h": 300,
        "doc_pad_v": 200,
        "doc_fill_color": "#FFFFFF",
        "base_stroke_color": "#23445D",
        "base_fill_color": "#BAC8D3",
        "screenshots": True,
    },
}


# ################################################## #
#
# DO NOT EDIT below this comment.
#
# ################################################## #
system_input = {
    "desktop": {
        "filename_large": "screenshot_desktop_large.png",
        "width_large": 2160,
        "height_large": 1360,
        "filename_medium": "screenshot_desktop_medium.png",
        "width_medium": 2048,
        "height_medium": None,
        "medium_height_crop": 1152,
        "filename_small": "screenshot_desktop_small.png",
        "width_small": 1920,
        "height_small": None,
        "small_height_crop": 1080,
    },
    "laptop": {
        "filename_large": "screenshot_laptop_large.png",
        "width_large": 1440,
        "height_large": 900,
        "filename_medium": "screenshot_laptop_medium.png",
        "width_medium": None,
        "height_medium": None,
        "medium_height_crop": None,
        "filename_small": "screenshot_laptop_small.png",
        "width_small": 1280,
        "height_small": None,
        "small_height_crop": 720,
    },
    "tablet": {
        "filename_large": "screenshot_tablet_large.png",
        "width_large": 768,
        "height_large": 1024,
        "filename_medium": "screenshot_tablet_medium.png",
        "width_medium": None,
        "height_medium": None,
        "medium_height_crop": None,
        "filename_small": "screenshot_tablet_small.png",
        "width_small": 600,
        "height_small": None,
        "small_height_crop": 800,
    },
    "smartphone": {
        "filename_large": "screenshot_smartphone_large.png",
        "width_large": 430,
        "height_large": 932,
        "filename_medium": "screenshot_smartphone_medium.png",
        "width_medium": None,
        "height_medium": None,
        "medium_height_crop": None,
        "filename_small": "screenshot_smartphone_small.png",
        "width_small": 230,
        "height_small": None,
        "small_height_crop": 490,
    },
}