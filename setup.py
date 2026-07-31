from pathlib import Path
from setuptools import setup, find_packages

HERE = Path(__file__).resolve().parent

setup(
    name="Affiliate-Links-Generator",
    version="0.1.1",
    description="A Python tool to convert normal product URLs to affiliate links.",
    author="Rishi Banota",
    packages=find_packages(),
    py_modules=["main"],
    entry_points={
        "console_scripts": [
            "affiliate-converter=main:main",
        ],
    },
    python_requires=">=3.7",
    long_description=(HERE / "README_pypi.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    url="https://github.com/rishibanota/Affiliate-Links-Generator",
)
