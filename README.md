# Portfoliofy

A REST API to generate portfolio-ready screenshots of your awesome web projects

## Description

> [!NOTE]
> ALL CONTENTS IN THIS REPO ARE FOR EDUCATIONAL PURPOSES ONLY.

Once a web project is done, it's time to document your hard work and show it off. _Portfoliofy_ makes that process easier by doing all the screenshots for you and assembling them together into portfolio-ready files.

![Portfoliofy](/docs/portfoliofy1.png)

More screenshots below.

## Table of Contents

* [Description](#description)
* [Features](#features)
* [Project Structure](#project-structure)
* [Prerequisites](#prerequisites)
* [Getting Started](#getting-started)
  * [Dependencies](#dependencies)
  * [Installation](#installation)
  * [Configuration](#configuration)
  * [Usage](#usage)
* [Author(s)](#authors)
* [Version History](#version-history)
  * [Release Notes](#release-notes)
  * [Initial Release](#initial-release)
* [Future Work](#future-work)
* [License](#license)
* [Contributing](#contributing)
* [Acknowledgments](#acknowledgments)
* [Screenshots](#screenshots)

## Features

_Portfoliofy_ v3.0.0-beta.2 offers the following `OUTPUT` types requested from exposed endpoints (see [Usage](#usage)):

### `OUTPUT_MAIN`

* Collage of screenshots taken from desktop, laptop, tablet, and smartphone views
* Each screenshot overlaid on a device mockup diagram
* PNG format

### `OUTPUT_BROWSER`

* Screenshot from desktop view overlaid on a browser mockup diagram
* PNG format

### `OUTPUT_MOBILES`

* Collage of screenshots taken from tablet and smartphone views
* Each screenshot overlaid on a device mockup diagram
* PNG format

### `OUTPUT_FULL`

* A full-page screenshot overlaid on a browser mockup diagram
* PNG format

### `OUTPUT_MOVIE`

* A scroll animation video of the full webpage
* MP4 format

### `OUTPUT_SCREENSHOTS`

* Plain screenshots (no mockup diagrams) at various viewport sizes:
  * Desktop (2160x1360)
  * Laptop (1440x900)
  * Tablet (768x1024)
  * Smartphone (230x490)
* Includes separate full-page screenshot option
* All in PNG format

_More features coming soon!_

## Project Structure

```text
portfoliofy/
│
├── api/
│   │ 
│   ├── core/
│   │   ├── config/
│   │   │   └── __init__.py
│   │   └── utils/
│   │       └── __init__.py
│   │ 
│   ├── domain/
│   │   └── schemas/
│   │   │   └── __init__.py
│   │   └── services/
│   │       └── __init__.py
│   │
│   ├── routers/
│   │   ├── __init__.py
│   │   └── endpoints/
│   │       └── __init__.py
│   │
│   └── portfoliofy.py
│  
├── docs/
├── requirements.txt
├── .gitignore
├── .pylintrc
└── README.md
```

## Prerequisites

* TBD

## Getting Started

### Dependencies

* See `requirements.txt`

### Installation

1. **Clone the repository**

    ```bash
    git clone https://github.com/ggeerraarrdd/portfoliofy.git
    ```

2. **Navigate into the project directory**

    ```bash
    cd portfoliofy # For example
    ```

3. **Create and activate a virtual environment**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. **Install the dependencies**

    ```bash
    pip install -r requirements.txt
    ```

### Configuration

* TBD

### Usage

1. **Start the live server**

    ```bash
    uvicorn api.portfoliofy:app --reload
    ```

2. **Access the documentation user interfaces**

    The _Portfoliofy_ REST API was built using FastAPI, which comes with two documentation user interfaces:

    * [Swagger UI](https://swagger.io/tools/swagger-ui/): served at `/docs`.
    * [ReDoc](https://redocly.github.io/redoc/): served at `/redoc`.

    ![Portfoliofy](/docs/portfoliofy6.png)
    _The Swagger UI for Portfoliofy served at `/docs`_

3. **Choose an endpoint for your needs**

    `POST /main` - handles requests for `OUTPUT_MAIN`.

    `POST /browser` - handles requests for `OUTPUT_BROWSER`.

    `POST /mobiles` - handles requests for `OUTPUT_MOBILES`.

    `POST /full` - handles requests for `OUTPUT_FULL`.

    `POST /movie` - handles requests for `OUTPUT_MOVIE`.

    `POST /screenshots/desktop` - handles requests for screenshots from a desktop viewport (2160x1360).

    `POST /screenshots/laptop` - handles requests for screenshots from a laptop viewport (1440x900).

    `POST /screenshots/tablet` - handles requests for screenshots from a tablet viewport (768x1024).

    `POST /screenshots/smartphone` - handles requests for screenshots from a smartphone viewport (230x490).

    `POST /screenshots/full` - handles requests for a full-page screenshot.

4. **Configure your request parameters**

    This is the request body schema for all endpoints.

    | Parameter         | Type   | Default value                        | Value range  | Description |
    | ----------------- | ------ | ------------------------------------ | ------------ | ----------- |
    | request           | bool   | False                                | True, False  | If TRUE, requested output is processed. |
    | remote_url        | string | "<https://ggeerraarrdd.github.io/>"  | ...          | URL to portfoliofy. |
    | wait              | int    | 2                                    | 1 - 100      | Time in seconds to allow URL to load before taking screenshot. |
    | format            | string | "png"                                | "png"        | File format of the final output. |
    | doc_pad_h         | int    | 300                                  | 1 - 1000     | Left and right padding in pixels of final output. |
    | doc_pad_v         | int    | 200                                  | 1 - 1000     | Top and bottom padding in pixels of final output. |
    | doc_fill_color    | string | "#FFFFFF"                            | ...          | Background color of final output in 6-digit hex. |
    | base_stroke_color | string | "#23445D"                            | ...          | Stroke color of diagram in 6-digit hex. |
    | base_fill_color   | string | "#BAC8D3"                            | ...          | Fill color of diagram in 6-digit hex. |

    **Example Request:**

    ```json
    {
      "request": true,
      "remote_url": "https://ggeerraarrdd.github.io/",
      "wait": 2,
      "format": "png",
      "doc_pad_h": 300,
      "doc_pad_v": 200,
      "doc_fill_color": "#ffffff",
      "base_stroke_color": "#23445d",
      "base_fill_color": "#bac8d3"
    }
    ```

    **Additional Notes**

    * `POST /movie` will return `204 NO CONTENT` if the height of the full-page screenshot is >= 20,000px after it is resized to a width of 1280px.
    * `POST /movie` currently only accepts the default `png` file format but will return an `mp4` file.

## Author(s)

* [@ggeerraarrdd](https://github.com/ggeerraarrdd/)

## Version History

### Release Notes

* See [https://github.com/ggeerraarrdd/portfoliofy/releases](https://github.com/ggeerraarrdd/portfoliofy/releases)

### Initial Release

The [initial realease](https://github.com/ggeerraarrdd/portfoliofy/releases/tag/v1.0.0) of _Portfoliofy_ was submitted as a final project for [CS50P: Introduction to Programming with Python](https://cs50.harvard.edu/python/2022/) (HarvardX, 2023). Read the [project brief](https://cs50.harvard.edu/python/2022/project/) as of November 2023.

## Future Work

Improvements and new features development are ongoing.

* Develop a user-friendly web interface powered by the REST API
* More `OUTPUT` types
* More customizations
* Support for `jpg` and `pdf` file format requests

## License

* [MIT License](https://github.com/ggeerraarrdd/large-parks/blob/main/LICENSE)

## Contributing

* TBD

## Acknowledgments

* [Sanjeev Thiyagarajan](https://www.linkedin.com/in/sanjeev-thiyagarajan-690001163/)'s massive, 19-hour Python API Development [course](https://www.youtube.com/playlist?list=PL8VzFQ8k4U1IiGUWdBI7s9Y7dm-4tgCXJ) is `the` best online tutorial video I have watched not just on APIs but on any IT topic.

## Screenshots

![Portfoliofy](/docs/portfoliofy2.png)

![Portfoliofy](/docs/portfoliofy3.png)

![Portfoliofy](/docs/portfoliofy4.png)

<https://github.com/ggeerraarrdd/portfoliofy/assets/50889794/c93ae299-1e76-42c1-b297-713a923eab79>

## Frontispiece

* TBD
