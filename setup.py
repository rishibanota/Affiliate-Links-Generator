from setuptools import setup, find_packages

setup(
    name="affiliate_link_converter",
    version="0.1.0",
    description="A Python tool to convert normal product URLs to affiliate links.",
    author="Rishi Banota",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'affiliate-converter=main:main',
        ],
    },
    python_requires=">=3.7",
)
