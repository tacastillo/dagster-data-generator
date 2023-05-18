from pathlib import Path
from typing import Dict

from setuptools import find_packages, setup


# def get_version() -> str:
#     version: Dict[str, str] = {}
#     with open(Path(__file__).parent / "dagster_data_generator/version.py", encoding="utf8") as fp:
#         exec(fp.read(), version)

#     return version["__version__"]


# ver = get_version()
ver = "0.0.1"
# dont pin dev installs to avoid pip dep resolver issues
pin = "" if ver == "1!0+dev" else f"=={ver}"
setup(
    name="dagster-data-generator",
    # version=ver,
    version="0.0.1",
    author="Elementl",
    author_email="hello@elementl.com",
    license="Apache-2.0",
    description="Package for generating simulated data for experimenting with Dagster.",
    # url="https://github.com/dagster-io/dagster/tree/master/python_modules/libraries/dagster-duckb",
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    # include_package_data=True,
    install_requires=[
        "Faker==18.4.0",
        # f"dagster{pin}",
        "dagster==1.3.4",
    ],
    zip_safe=False,
)
