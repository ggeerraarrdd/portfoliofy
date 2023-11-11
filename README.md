# Portfoliofy

Assemble screenshots of web projects for your portfolio

## Description

Once a web project is done, it's time to document your hard work and show it off. _Portfoliofy!_ makes that process easier by doing all the screenshots for you and assembling them together into portfolio-ready files.

As of v1.0.0, two files are generated:

* A desktop browser screenshot (2048x1152)
* A collage of screenshots for various devices: desktop (1920x1080), laptop (1280x720), tablet (600x800), mobile (230x490).

![Portfoliofy](/images/portfoliofy1.png)

More screenshots below.

## Disclaimer

ALL CONTENTS IN THIS REPO ARE FOR EDUCATIONAL PURPOSES ONLY.

## Getting Started

### Dependencies

* Pillow==10.1.0
* Requests==2.31.0
* selenium==4.15.0

### Usage

Clone it!

```bash
git clone https://github.com/ggeerraarrdd/portfoliofy.git
```

Go into the project directory and run the command:

```bash
python portfoliofy.py
```

Enter a valid and accessible URL as requested.

The output files are stored in a directory inside the `output` directory.

## Author(s)

* [@ggeerraarrdd](https://github.com/ggeerraarrdd/)

## Version History

### Release Notes

* See [https://github.com/ggeerraarrdd/portfoliofy/releases](https://github.com/ggeerraarrdd/portfoliofy/releases)

### Initial Release

The [initial realease](https://github.com/ggeerraarrdd/portfoliofy/releases/tag/v1.0.0) of _Portfoliofy!_ was submitted as the final project for [CS50P: Introduction to Programming with Python](https://cs50.harvard.edu/python/2022/) (HarvardX, 2023).

[Project brief](https://cs50.harvard.edu/python/2022/project/) as of November 2023:

_The design and implementation of your project is entirely up to you, albeit subject to these requirements:_

* _Your project must be implemented in Python._
* _Your project must have a main function and three or more additional functions. At least three of those additional functions must be accompanied by tests that can be executed with pytest._
* _Your main function must be in a file called project.py, which should be in the “root” (i.e., top-level folder) of your project._
* _Your 3 required custom functions other than main must also be in project.py and defined at the same indentation level as main (i.e., not nested under any classes or functions)._
* _Your test functions must be in a file called test_project.py, which should also be in the “root” of your project. Be sure they have the same name as your custom functions, prepended with test (test_custom_function, for example, where custom_function is a function you’ve implemented in project.py)._
* _You are welcome to implement additional classes and functions as you see fit beyond the minimum requirement._
* _Implementing your project should entail more time and effort than is required by each of the course’s problem sets._
* _Any pip-installable libraries that your project requires must be listed, one per line, in a file called requirements.txt in the root of your project._

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
