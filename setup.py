from setuptools import setup, find_packages

setup(
    name="Affiliate-Links-Generator",
    version="0.1.1",
    description="A Python tool to convert normal product URLs to affiliate links.",
    author="Rishi Banota",
    packages=find_packages(),
    py_modules=["main"],
    entry_points={
        'console_scripts': [
            'affiliate-converter=main:main',
        ],
    },
    python_requires=">=3.7",
    long_description=open("README_pypi.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/rishibanota/Affiliate-Links-Generator",
    project_urls={
        "Bug Tracker": "https://github.com/rishibanota/Affiliate-Links-Generator/issues",
        "Documentation": "https://github.com/rishibanota/Affiliate-Links-Generator#readme",
        "Source Code": "https://github.com/rishibanota/Affiliate-Links-Generator",
    },
)
