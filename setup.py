import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="topsis-khushi-102103479",
    version="1.0.0",
    description="Performs TOPSIS dor multi-criteria decision making",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/khushi-attri/topsis",
    author="Khushi Atti",
    author_email="kattri_be21@thapar.edu",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    packages=["topsis"],
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "topsis=topsis.__main__:main",
        ]
    },
)