<!-- markdownlint-disable MD041 -->
[![GitHub release](https://img.shields.io/github/v/release/ggeerraarrdd/portfoliofy)](https://github.com/ggeerraarrdd/portfoliofy/releases)
[![Maintenance](https://img.shields.io/badge/maintained-yes-green.svg)](https://github.com/ggeerraarrdd/portfoliofy/graphs/commit-activity)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/4f79ef9284bc4b6287ac2e003708e3d4)](https://app.codacy.com/gh/ggeerraarrdd/portfoliofy/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
[![codecov](https://codecov.io/gh/ggeerraarrdd/portfoliofy/graph/badge.svg?token=LU62T9HB4E)](https://codecov.io/gh/ggeerraarrdd/portfoliofy)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ggeerraarrdd_portfoliofy&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=ggeerraarrdd_portfoliofy)
[![Renovate enabled](https://img.shields.io/badge/renovate-enabled-brightgreen.svg)](https://renovatebot.com/)
<!-- markdownlint-enable MD041 -->

# Portfoliofy

A RESTful API to generate portfolio-ready screenshots of your awesome web projects

## Table of Contents

> [!NOTE]
> ALL CONTENTS IN THIS REPO ARE FOR EDUCATIONAL PURPOSES ONLY.

* [Description](#description)
* [Target Users](#target-users)
* [Features](#features)
* [Project Structure](#project-structure)
* [Quick Start](#quick-start)
* [Local Setup](#local-setup)
  * [Prerequisites](#prerequisites)
  * [Dependencies](#dependencies)
  * [Installation](#installation)
  * [Configuration](#configuration)
* [Usage](#usage)
* [Production Setup](#production-setup)
* [System Administration](#system-administration)
* [Author(s)](#authors)
* [Version History](#version-history)
  * [Release Notes](#release-notes)
  * [Initial Release](#initial-release)
* [Future Work](#future-work)
* [License](#license)
* [Contributing](#contributing)
* [Acknowledgments](#acknowledgments)
* [Screenshots](#screenshots)

## Description

Once a web project is done, it's time to document your hard work and show it off. _Portfoliofy_ makes that process easier by doing all the screenshots for you and assembling them together into configurable, portfolio-ready files through a RESTful API interface.

![Portfoliofy](/assets/portfoliofy1.png)
_(Sample of `OUTPUT_MAIN` - a multi-device viewport composite of [art.gsa.gov](https://art.gsa.gov/) showing desktop, laptop, tablet and smartphone views with stylized device mockups. More screenshots below.)_

## Target Users

_Portfoliofy_ is intended for:

* **Student and professional web developers** building portfolios to showcase their web development projects
* **Self-directed learners** looking to learn Python, in general, and RESTful API development using FastAPI, specifically, within the context of building a web screenshot generator and image manipulation application.

## Features

_Portfoliofy_ v3.0.0-beta.3 exposes RESTful API endpoints that process HTTP requests for the following `OUTPUT` types, each offering configurable visual stylings, document layouts and output formats.

### `OUTPUT_MAIN`

* Eye-catching composite of viewport-specific screenshots at multiple device resolutions (desktop, laptop, tablet, smartphone)
* Each screenshot overlaid on a stylized device mockup
* Supported formats: PNG, JPEG, BMP, TIFF, PDF

### `OUTPUT_BROWSER`

* Viewport-specific screenshot at desktop resolution, overlaid on a stylized browser mockup
* Supported formats: PNG, JPEG, BMP, TIFF, PDF

### `OUTPUT_MOBILES`

* Side-by-side composite of viewport-specific screenshots at tablet and smartphone resolutions
* Each screenshot overlaid on a stylized device mockup
* Supported formats: PNG, JPEG, BMP, TIFF, PDF

### `OUTPUT_FULL`

* Full-page screenshot of the entire webpage content from top to bottom, overlaid on a stylized browser mockup
* Supported formats: PNG, JPEG, BMP, TIFF

### `OUTPUT_MOVIE`

* A scroll animation video of a full-page screenshot, framed by a stylized browser mockup
* Supported format: MP4

### `OUTPUT_SCREENSHOTS`

* Plain, viewport-specific screenshots at the following resolutions:
  * Desktop (2160x1360)
  * Laptop (1440x900)
  * Tablet (768x1024)
  * Smartphone (230x490)
* Plain, full-page screenshot of the entire webpage content from top to bottom
* Supported formats: PNG, JPEG, BMP, TIFF, PDF (except for full-page)

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
│   │   ├── schemas/
│   │   │   └── __init__.py
│   │   └── services/
│   │       └── __init__.py
│   │
│   ├── output/
│   │
│   ├── routers/
│   │   ├── __init__.py
│   │   └── endpoints/
│   │       └── __init__.py
│   │
│   └── portfoliofy.py
│  
├── assets/
├── .gitignore
├── .pylintrc
├── README.md
└── requirements.txt
```

## Quick Start

For those who want to get up and running quickly with default settings:

```bash
# Clone repository
git clone https://github.com/ggeerraarrdd/portfoliofy.git
cd portfoliofy

# Set up environment
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt

# Configure ChromeDriver path in .env file
echo "CHROMEDRIVER_PATH='/path/to/your/chromedriver'" > .env

# Start the server
python3 -m uvicorn api.portfoliofy:app --reload

# Access API documentation at http://127.0.0.1:8000/docs
```

## Local Setup

### Prerequisites

* Python 3.12
  * _Portfoliofy_ not fully tested on other versions
* Google Chrome
  * Latest stable version recommended
* ChromeDriver
  * Must match your Chrome browser version
  * Download from the [official ChromeDriver website](https://developer.chrome.com/docs/chromedriver/downloads)
  * Must be in system PATH or configured via `.env` (see [Configuration](#configuration))

### Dependencies

* See `requirements.txt`

**Note:** CairoSVG may require additional systems libraries. Refer to their [official documentation](https://cairosvg.org/documentation/).

### Installation

1. **Clone the repository**

    ```bash
    git clone https://github.com/ggeerraarrdd/portfoliofy.git
    ```

2. **Create and activate a virtual environment**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**

    ```bash
    pip install -r requirements.txt
    ```

### Configuration

1. **Configure the chromedriver path**
  
    * Create a `.env` file in the root directory of the project
    * Specify your ChromeDriver path:

    ```python
    CHROMEDRIVER_PATH='/path/to/your/chromedriver'
    ```

    * Update path to match local ChromeDriver installation

## Usage

1. **Start development server**

    ```bash
    python3 -m uvicorn api.portfoliofy:app --reload
    ```

2. **Access the documentation user interfaces**

    The _Portfoliofy_ REST API was built using FastAPI, which comes with two documentation user interfaces:

    * [Swagger UI](https://swagger.io/tools/swagger-ui/): served at `/docs`.
    * [ReDoc](https://redocly.github.io/redoc/): served at `/redoc`.

    ![Portfoliofy](/assets/portfoliofy6.png)
    _The Swagger UI for Portfoliofy served at `/docs`_

3. **Choose an endpoint for your needs**

    `POST /main` - `OUTPUT_MAIN`

    `POST /browser` - `OUTPUT_BROWSER`

    `POST /mobiles` - `OUTPUT_MOBILES`

    `POST /full` - `OUTPUT_FULL`

    `POST /movie` - `OUTPUT_MOVIE`

    `POST /screenshots/desktop` - plain, viewport-specific screenshots at desktop resolution (2160x1360)

    `POST /screenshots/laptop` - plain, viewport-specific screenshots at laptop resolution (1440x900)

    `POST /screenshots/tablet` - plain, viewport-specific screenshots at tablet resolution (768x1024)

    `POST /screenshots/smartphone` - plain, viewport-specific screenshots at smartphone resolution (230x490)

    `POST /screenshots/full` - plain, full-page screenshot

4. **Configure your request parameters**

    This is the request body schema for all endpoints.

    | Parameter           | Type     | Default value                         | Value range                                  | Description                                                                           |
    | ------------------- | -------- | ------------------------------------- | -------------------------------------------- | ------------------------------------------------------------------------------------- |
    | request             | bool     | False                                 | True, False                                  | If TRUE, requested OUTPUT type is processed                                           |
    | remote_url          | string   | "<https://ggeerraarrdd.github.io/>"   | ...                                          | URL to portfoliofy                                                                    |
    | wait                | int      | 2                                     | 1 - 100                                      | Delay in seconds before capturing screenshot                                          |
    | format              | string   | "png"                                 | "bmp", "jpeg", "mp4", "pdf", "png", "tiff"   | File format for API response document                                                 |
    | doc_pad_h           | int      | 300                                   | 1 - 1000                                     | Horizontal padding in pixels between OUTPUT content and API response document edges   |
    | doc_pad_v           | int      | 200                                   | 1 - 1000                                     | Vertical padding in pixels between OUTPUT content and API response document edges     |
    | doc_fill_color      | string   | "#FFFFFF"                             | ...                                          | Background color of API response document in 6-digit hex                              |
    | base_stroke_color   | string   | "#23445D"                             | ...                                          | Outline color of device mockup frame in 6-digit hex                                   |
    | base_fill_color     | string   | "#BAC8D3"                             | ...                                          | Background color of device mockup frame in 6-digit hex                                |

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

    * `POST /movie` returns `204 NO CONTENT` for full-page heights ≥ 20,000px at 1280px width.
    * `POST /movie` enforces MP4 output regardless of format parameter.

## Production Setup

* TBD

## System Administration

* TBD

## Author(s)

* [@ggeerraarrdd](https://github.com/ggeerraarrdd/)

## Version History

### Release Notes

* See [https://github.com/ggeerraarrdd/portfoliofy/releases](https://github.com/ggeerraarrdd/portfoliofy/releases)

### Initial Release

The [initial release](https://github.com/ggeerraarrdd/portfoliofy/releases/tag/v1.0.0) of _Portfoliofy_ was submitted as a final project for [CS50P: Introduction to Programming with Python](https://cs50.harvard.edu/python/2022/) (HarvardX, 2023). Read the [project brief](https://cs50.harvard.edu/python/2022/project/) as of November 2023.

## Future Work

* Improvements and new features development are ongoing.

## License

* [MIT License](https://github.com/ggeerraarrdd/large-parks/blob/main/LICENSE)

## Contributing

This project is not accepting contributions at this time. It is intended solely for personal learning and exploration. However, feel free to clone the repository and use it as a learning resource.

## Acknowledgments

* [Sanjeev Thiyagarajan](https://www.linkedin.com/in/sanjeev-thiyagarajan-690001163/)'s massive, 19-hour Python API Development [course](https://www.youtube.com/playlist?list=PL8VzFQ8k4U1IiGUWdBI7s9Y7dm-4tgCXJ) is `the` best online tutorial video I have watched not just on APIs but on any IT topic.

## Screenshots

_(From top to bottom: OUTPUT_BROWSER, OUTPUT_MOBILES, OUTPUT_FULL, OUTPUT_MOVIE for the US General Services Administration Fine Arts Collection website @ [https://art.gsa.gov/](https://art.gsa.gov/))_

![Portfoliofy](/assets/portfoliofy2.png)

![Portfoliofy](/assets/portfoliofy3.png)

![Portfoliofy](/assets/portfoliofy4.png)

<https://github.com/ggeerraarrdd/portfoliofy/assets/50889794/c93ae299-1e76-42c1-b297-713a923eab79>

## Frontispiece

Portfoliofy API. (2023). [Multi-device viewport composite of art.gsa.gov: Desktop, laptop, tablet, and smartphone views with stylized device mockups] [Digital output]. Author's collection. In the public domain.
