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
)
