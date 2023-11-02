# Portfoliofy!
Assemble screenshots of web projects for your portfolio

## Description

Once a web project is done and handed off, it's time to document the hard work you've done and show them off. _Portfoliofy!_ makes that process easier by doing all the screenshots for you and then assembling them together into portfolio-ready files.

As of v1.0.0, two files are generated:
* A full desktop browser screenshot (2048x1152)
* A collage of screenshots for various devices: desktop (1920x1080), laptop (1280x720), tablet (600x800), mobile (230x490).

_Portfoliofy!_ was originally designed and implemented by Gerard Bul-lalayao as the final project for CS50P: Introduction to Programming with Python (HarvardX, 2023).

<picture><img alt="Shelfie screenshot 1" src="/images/portfoliofy1.png"></picture>

More screenshots below.

## Disclaimer
ALL CONTENTS IN THIS REPO ARE FOR EDUCATIONAL PURPOSES ONLY.

## Learning Objectives

### Requirements
_[Assignment brief](https://cs50.harvard.edu/python/2022/project/) for CS50P's Final Project (as of November 2023)_

_The design and implementation of your project is entirely up to you, albeit subject to these requirements:_

* _Your project must be implemented in Python._
* _Your project must have a main function and three or more additional functions. At least three of those additional functions must be accompanied by tests that can be executed with pytest._
* _Your main function must be in a file called project.py, which should be in the “root” (i.e., top-level folder) of your project._
* _Your 3 required custom functions other than main must also be in project.py and defined at the same indentation level as main (i.e., not nested under any classes or functions)._
* _Your test functions must be in a file called test_project.py, which should also be in the “root” of your project. Be sure they have the same name as your custom functions, prepended with test (test_custom_function, for example, where custom_function is a function you’ve implemented in project.py)._
* _You are welcome to implement additional classes and functions as you see fit beyond the minimum requirement._
* _Implementing your project should entail more time and effort than is required by each of the course’s problem sets._
* _Any pip-installable libraries that your project requires must be listed, one per line, in a file called requirements.txt in the root of your project._

### Personal Goals
Apart from what was to be gained from implementing the requirements, this project was used as a vehicle to further learn and/or practice the following:

* Image manipulations

## Getting Started

### Dependencies
* Pillow==10.1.0
* Requests==2.31.0
* selenium==4.15.0

### Usage
Clone it!
```
$ git clone https://github.com/ggeerraarrdd/portfoliofy.git
```

Go into the project directory and run the command:
```
$ python portfoliofy.py
```
Enter a valid and accessible URL as requested.

The output files are stored in a directory inside the `output` directory.

## Author(s)
* [@ggeerraarrdd](https://github.com/ggeerraarrdd/)

## Version History
* See [https://github.com/ggeerraarrdd/readme-drafts/releases](https://github.com/ggeerraarrdd/readme-drafts/releases)

## Future Work
* Develop a user-friendly web interface
* More options

## License
* [MIT License](https://github.com/ggeerraarrdd/large-parks/blob/main/LICENSE)

## Acknowledgments
* The [tutorial](https://pillow.readthedocs.io/en/stable/handbook/tutorial.html) at Pillow's website.

## Screenshots
<picture><img alt="Shelfie screenshot 1" src="/images/portfoliofy2.png"></picture>
