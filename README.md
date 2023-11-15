# Portfoliofy

Assemble screenshots of web projects for your portfolio

## Description

Once a web project is done, it's time to document your hard work and show it off. _Portfoliofy_ makes that process easier by doing all the screenshots for you and assembling them together into portfolio-ready files.

As of v2.0.0, the following files can be generated:

* `SCREENSHOTS`
  * Four image files of screenshots taken in different viewports (desktop - 2160x1360, laptop - 1440x900, tablet - 768x1024, smartphone - 230x490).
* `MAIN`
  * An image file of those screenshots overlaid on top schematic diagrams and then collaged together. (See below for an example ouput.)
* `BROWSER`
  * A image file of the desktop screenshot overlaid on top of a schematic diagram. (Scroll to the bottom for an example ouput.)

More coming soon!

![Portfoliofy](/images/portfoliofy1.png)

More screenshots below.

## Disclaimer

ALL CONTENTS IN THIS REPO ARE FOR EDUCATIONAL PURPOSES ONLY.

## Getting Started

### Dependencies

* CairoSVG==2.7.1
* Pillow==10.1.0
* Requests==2.31.0
* selenium==4.15.2

### Usage

Clone it!

```bash
git clone https://github.com/ggeerraarrdd/portfoliofy.git
```

Open `local_settings.py` and change the value of `url` to the one you want to portfoliofy.

Then run the following command:

```bash
python portfoliofy.py
```

The output files are stored in a subdirectory of the `output` directory.

## Parameters

| Parameter         | Type   | Default value          | Value range  | Description |
| ----------------- | ------ | ---------------------- | ------------ | ----------- |
| url               | string | 'https://www.nps.gov/' | ''           | The URL to portfoliofy. |
| wait              | int    | 2                      | 0-60         | Time in seconds to allow URL to load before taking screenshot. |
| screenshots       | bool   | True                   | True, False  | If TRUE, all screenshots are saved. |

The `MAIN` and `BROWSER` output files are generated by default but you can change this default behavior by editing the value of `request`. You can also customize the output files.

| Parameter         | Type   | Default value | Value range  | Description |
| ----------------- | ------ | ------------- | ------------ | ----------- |
| request           | bool   | True          | True, False  | If TRUE, requested output is processed. |
| format            | string | png           | png          | Format of the final output. |
| doc_pad_h         | int    | 300           | 0 - 1000     | Left and right padding in pixels of final output. |
| doc_pad_v         | int    | 200           | 0 - 1000     | Top and bottom padding in pixels of final output. |
| doc_fill_color    | string | #FFFFFF       | ''           | Background color of final output in 6-digit hex. |
| base_stroke_color | string | #23445D       | ''           | Stroke color of diagram in 6-digit hex. |
| base_fill_color   | string | #BAC8D3       | ''           | Fill color of diagram in 6-digit hex. |

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
* More options

## License

* [MIT License](https://github.com/ggeerraarrdd/large-parks/blob/main/LICENSE)

## Acknowledgments

* The [tutorial](https://pillow.readthedocs.io/en/stable/handbook/tutorial.html) at Pillow's website.

## Screenshots

![Portfoliofy](/images/portfoliofy2.png)
