# Portfoliofy

A portfolio maker for your awesome web projects

## Description

Once a web project is done, it's time to document your hard work and show it off. _Portfoliofy_ makes that process easier by doing all the screenshots for you and assembling them together into portfolio-ready files.

As of v2.4.2, the following `OUTPUT` types can be generated:

* `OUTPUT_SCREENSHOTS`
  * Four image files of screenshots taken in different window sizes mimicking the viewport of a desktop (2160x1360), a laptop (1440x900), a tablet (768x1024) and a smartphone (230x490).
  * One image file of a full-page screenshot.
* `OUTPUT_MAIN`
  * An image file of those screenshots, except the full-page one, overlaid on top of a schematic diagram and then collaged together. (See below for an example ouput.)
* `OUTPUT_BROWSER`
  * An image file of the desktop screenshot overlaid on top of a schematic diagram. (Scroll to the bottom for an example ouput.)
* `OUTPUT_MOBILES`
  * An image file of the tablet and smartphone screenshots overlaid on top of a schematic diagram and paired together. (Scroll to the bottom for an example ouput.)
* `OUTPUT_FULL`
  * An image file of the full-page screenshot overlaid on top of a schematic diagram. (Scroll to the bottom for an example ouput.)
* `OUTPUT_MOVIE`
  * A scroll animation video of the full-page screenshot. (Scroll to the bottom for an example ouput.)

More coming soon!

![Portfoliofy](/images/portfoliofy1.png)

More screenshots below.

## Disclaimer

ALL CONTENTS IN THIS REPO ARE FOR EDUCATIONAL PURPOSES ONLY.

## Getting Started

### Dependencies

* CairoSVG==2.7.1
* click==8.1.3
* moviepy==1.0.3
* Pillow==10.1.0
* Requests==2.31.0
* selenium==4.15.2

### Usage

Clone it!

```bash
git clone https://github.com/ggeerraarrdd/portfoliofy.git
```

At minimum change the `url` [parameter](https://github.com/ggeerraarrdd/portfoliofy#parameters) in `local_settings.py` to the webpage you want to portfoliofy.

Then run the following command:

```bash
python portfoliofy.py
```

The output files are stored in a subdirectory of the `output` directory.

## Parameters

This is a list of parameters you can change in `local_settings.py`.

| Parameter         | Type   | Default value            | Value range  | Description |
| ----------------- | ------ | ------------------------ | ------------ | ----------- |
| url               | string | '<https://www.nps.gov/>' | ''           | The URL to portfoliofy. |
| wait              | int    | 2                        | 0-60         | Time in seconds to allow URL to load before taking screenshot. |

`OUTPUT_SCREENSHOTS`

| Parameter         | Type   | Default value            | Value range  | Description |
| ----------------- | ------ | ------------------------ | ------------ | ----------- |
| screenshots       | bool   | True                     | True, False  | If TRUE, all screenshots are saved. |

`OUTPUT_MAIN`, `OUTPUT_BROWSER`, `OUTPUT_MOBILES`, `OUTPUT_FULL` and `OUTPUT_MOVIE`

| Parameter         | Type   | Default value | Value range  | Description |
| ----------------- | ------ | ------------- | ------------ | ----------- |
| request           | bool   | True          | True, False  | If TRUE, requested output is processed. |
| format            | string | png           | png          | Format of the final output. |
| doc_pad_h         | int    | 300           | 1 - 1000     | Left and right padding in pixels of final output. |
| doc_pad_v         | int    | 200           | 1 - 1000     | Top and bottom padding in pixels of final output. |
| doc_fill_color    | string | #FFFFFF       | ''           | Background color of final output in 6-digit hex. |
| base_stroke_color | string | #23445D       | ''           | Stroke color of diagram in 6-digit hex. |
| base_fill_color   | string | #BAC8D3       | ''           | Fill color of diagram in 6-digit hex. |

### Notes

* `OUTPUT_MOVIE` currently will not be processed if the height of the full-page screenshot is >= 20,000px after it is resized to a width of 1280px.
* `OUTPUT_MOVIE` currently only accepts mp4 format.

### Example

This code will portfoliofy a webpage served on a web server running on a local computer. It only requests `OUTPUT_MAIN` and `OUTPUT_BROWSER` both in the default PNG format. `OUTPUT_MAIN`, `OUTPUT_MOBILES`, `OUTPUT_FULL` and `OUTPUT_VIDEO` will not be processed. But all `OUTPUT_SCREENSHOTS` will be saved. All other parameters remain set to their default values.

```python
user_input = {
    "url": "http://localhost:5000/",
    "wait": 2,
    "screenshots": True,
    "output_main": {
        "request": True,
        "format": "png",
        "doc_pad_h": 300,
        "doc_pad_v": 200,
        "doc_fill_color": "#FFFFFF",
        "base_stroke_color": "#23445D",
        "base_fill_color": "#BAC8D3",
    },
    "output_browser": {
        "request": True,
        "format": "png",
        "doc_pad_h": 300,
        "doc_pad_v": 200,
        "doc_fill_color": "#FFFFFF",
        "base_stroke_color": "#23445D",
        "base_fill_color": "#BAC8D3",
    },
    "output_mobiles": {
        "request": False,
        "format": "png",
        "doc_pad_h": 300,
        "doc_pad_v": 200,
        "doc_fill_color": "#FFFFFF",
        "base_stroke_color": "#23445D",
        "base_fill_color": "#BAC8D3",
    },
      "output_full": {
        "request": False,
        "format": "png",
        "doc_pad_h": 300,
        "doc_pad_v": 200,
        "doc_fill_color": "#FFFFFF",
        "base_stroke_color": "#23445D",
        "base_fill_color": "#BAC8D3",
    },
      "output_video": {
        "request": False,
        "format": "mp4",
        "doc_pad_h": 300,
        "doc_pad_v": 200,
        "doc_fill_color": "#FFFFFF",
        "base_stroke_color": "#23445D",
        "base_fill_color": "#BAC8D3",
    },    
}
```

## Author(s)

* [@ggeerraarrdd](https://github.com/ggeerraarrdd/)

## Version History

### Release Notes

* See [https://github.com/ggeerraarrdd/portfoliofy/releases](https://github.com/ggeerraarrdd/portfoliofy/releases)

### Initial Release

The [initial realease](https://github.com/ggeerraarrdd/portfoliofy/releases/tag/v1.0.0) of _Portfoliofy_ was submitted as the final project for [CS50P: Introduction to Programming with Python](https://cs50.harvard.edu/python/2022/) (HarvardX, 2023). Read the [project brief](https://cs50.harvard.edu/python/2022/project/) as of November 2023.

### Future Work

New features development is ongoing.

* Develop a user-friendly web interface
* More `OUTPUT` types
* More customizations

## License

* [MIT License](https://github.com/ggeerraarrdd/large-parks/blob/main/LICENSE)

## Acknowledgments

* The [tutorial](https://pillow.readthedocs.io/en/stable/handbook/tutorial.html) at Pillow's website.

## Screenshots

![Portfoliofy](/images/portfoliofy2.png)

![Portfoliofy](/images/portfoliofy3.png)

![Portfoliofy](/images/portfoliofy4.png)

<https://github.com/ggeerraarrdd/portfoliofy/assets/50889794/c93ae299-1e76-42c1-b297-713a923eab79>
