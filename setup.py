#!/usr/bin/env python
import os
from setuptools import setup
from setuptools import find_packages

# read the contents of your README file
from pathlib import Path
from distutils.util import convert_path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


with open(os.path.join(this_directory, "VERSION")) as version_file:
    version = version_file.read().strip()


setup(
    name="geocover",
    version=version,  # noqa: F821
    description="Set of tools for generating the geological datamodel "
    "(https://www.geologieportal.ch/en/knowledge/lookup/data-models/geology-data-model.html) ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="swisstopo",
    maintainer="Marc Monnerat",
    maintainer_email="marc.monnerat@swisstopo.ch",
    url="https://github.com/swisstopo/lg-geology-data-model",
    license="LICENSE.txt",
    packages=find_packages(where="src"),  # Automatically find packages under src
    package_dir={'': 'src'},
    include_package_data=True,  # Must be in included in MANIFEST.in
    package_data={
        "geocover": ["data/*.csv"],
    },
    python_requires=">=3.7",  # ArcGis Pro 3.3 is still 3.7.11
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: BSD License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Topic :: Scientific/Engineering :: Image Processing",
        "Topic :: Scientific/Engineering :: GIS",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    install_requires=[
        "jinja2",
        "pyyaml",
        "click",
        "geopandas",
        "pandas",
        "click",
        "loguru",
        "shapely >= 2.0.0",
        "babel",
        "jsonschema",
        "openpyxl",
        "ruamel.yaml",
    ],
    tests_require=["coverage", "unittests"],
    entry_points={
        "console_scripts": [
            "geocover = geocover.geocover:geocover",
            "datamodel = geocover.datamodel:datamodel",
        ],
    },
)
