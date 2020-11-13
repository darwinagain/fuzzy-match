import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="fuzzy-match",
    version="0.0.1",
    description="Fuzzy string matching in Python",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/darwinagain/fuzzy-match",
    author="darwinagain",
    author_email="iamdarwinagain@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["fuzzy_match"]
)
