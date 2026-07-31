from setuptools import setup, find_packages

setup(
    name="Affiliate-Links-Generator",
    version="0.1.2",
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
    long_description="""# Affiliate Links Generator

A modular, robust, and easy-to-use Python command-line tool to magically convert normal product URLs into your own affiliate links for various e-commerce platforms.

Welcome to the **Affiliate Links Generator**! 🎉 

Tired of manually generating affiliate links for different merchants? This tool makes it incredibly simple to automatically wrap or append your tracking IDs to regular product URLs. Whether you're working with Amazon, eBay, or 10+ other affiliate networks, we've got you covered!

## Features & Supported Providers

We support a wide array of top affiliate networks natively:

- **Amazon Associates**: Seamlessly appends your `tag` to any Amazon URL.
- **eBay Partner Network (EPN)**: Adds EPN tracking parameters (`campid`, `mkevt`, `mkcid`) to eBay listings.
- **Flipkart Affiliate**: Appends your `affid` to Flipkart product URLs.
- **Walmart (Rakuten LinkSynergy)**: Generates a deep link using your publisher ID.
- **AliExpress Portals**: Generates deep links using your `aff_short_key`.
- **ShareASale**: Auto-wraps URLs into deep links using your `merchantid` and `userid`.
- **CJ Affiliate**: Deep link generator using your `pid` (Website ID) and `aid` (Ad ID).
- **Impact Radius**: Uses your Impact `base_url` to correctly redirect traffic.
- **Rakuten Advertising**: Deep link generator for the LinkSynergy network.
- **Skimlinks**: Instantly wraps almost any merchant URL into a Skimlinks redirect using your `publisher_id`.
- **Awin (Affiliate Window)**: Uses your `publisher_id` and `merchant_id` to generate trackable links.

## Installation

```bash
pip install Affiliate-Links-Generator
```

## How to Use

### Python API Integration

Want to use this in your web app or Discord bot? It's fully programmatic!

```python
from affiliate_link_converter.converter import AffiliateConverter

# 1. Setup your configuration dictionary
config = {
    'amazon': {'tag': 'your_tag-20'},
    'ebay': {'campid': '5338123456', 'customid': 'social_media'}
}

# 2. Initialize the converter
converter = AffiliateConverter(config)

# 3. Magically convert your URLs!
amazon_url = converter.convert("https://www.amazon.com/dp/B08F7PTF53")
print("Amazon Affiliate Link:", amazon_url)
```

For full documentation and CLI usage, please visit the [GitHub Repository](https://github.com/rishibanota/Affiliate-Links-Generator).
""",
    long_description_content_type="text/markdown",
    url="https://github.com/rishibanota/Affiliate-Links-Generator",
)
