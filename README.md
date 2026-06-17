# Affiliate Link Converter

A modular and easy-to-use Python command-line tool to convert normal product URLs into affiliate links for various e-commerce platforms.

## Supported Providers

- **Amazon Associates**: Appends your `tag` to any Amazon URL.
- **eBay Partner Network (EPN)**: Appends EPN parameters like `campid`, `mkevt`, `mkcid` to eBay listings.
- **Flipkart Affiliate**: Appends your `affid` to Flipkart URLs.
- **Walmart (Rakuten LinkSynergy)**: Generates a deep link via LinkSynergy using your publisher ID and encodes the Walmart URL.
- **AliExpress Portals**: Generates deep links using your `aff_short_key`.
- **ShareASale**: Generic deep link generator. Set `merchantid`, `userid`, and optionally `domain` to auto-wrap URLs.
- **CJ Affiliate (Commission Junction)**: Generic deep link generator using `pid` (Website ID) and `aid` (Ad ID).
- **Impact Radius**: Generic deep link generator using an Impact `base_url` (like `brand.pxf.io/c/...`) and `domain`.
- **Rakuten Advertising**: Generic deep link generator via LinkSynergy using `publisher_id`, `merchant_id` and `domain`.
- **Skimlinks**: Generic auto-wrapper that turns almost any merchant URL into a Skimlinks redirect using your `publisher_id`.
- **Awin (Affiliate Window)**: Generic deep link generator using `publisher_id` and `merchant_id`.

## Installation

Clone this repository and install the package:

```bash
git clone https://github.com/rishibanota/affiliate-link-converter.git
cd affiliate-link-converter
pip install -e .
```

## Usage

You can use the tool directly via the command line or import it into your own Python code.

### Command Line Interface

You can pass the URL and your affiliate credentials as arguments:

```bash
# Amazon Example
python main.py "https://www.amazon.com/dp/B08F7PTF53" --amazon-tag "your_tag-20"

# eBay Example
python main.py "https://www.ebay.com/itm/123456789" --ebay-campid "5338123456" --ebay-customid "my_campaign"

# Flipkart Example
python main.py "https://www.flipkart.com/some-product/p/itm1234" --flipkart-id "your_flip_id"

# Walmart Example
python main.py "https://www.walmart.com/ip/some-product/123456" --walmart-publisher-id "rakuten_pub_id"

# AliExpress Example
python main.py "https://www.aliexpress.com/item/100500123456789.html" --aliexpress-key "your_key"

# ShareASale Example
python main.py "https://www.example-merchant.com/product/123" \
    --shareasale-userid "123456" \
    --shareasale-merchantid "7890" \
    --shareasale-domain "example-merchant.com"

# CJ Affiliate Example
python main.py "https://www.some-store.com/item" \
    --cj-pid "1234567" \
    --cj-aid "98765432" \
    --cj-domain "some-store.com"

# Impact Radius Example
python main.py "https://www.target.com/p/item123" \
    --impact-url "https://goto.target.com/c/1234/5678" \
    --impact-domain "target.com"

# Skimlinks Example
python main.py "https://www.any-merchant.com/product" \
    --skimlinks-id "12345X67890"

# Awin Example
python main.py "https://www.etsy.com/listing/123" \
    --awin-pubid "12345" \
    --awin-mid "6220" \
    --awin-domain "etsy.com"
```

### Python API

You can also use the converter programmatically in your projects:

```python
from affiliate_link_converter.converter import AffiliateConverter

# Setup your configuration
config = {
    'amazon': {'tag': 'your_tag-20'},
    'ebay': {'campid': '5338123456', 'customid': 'social_media'},
    'flipkart': {'affid': 'your_flip_id'},
    'walmart': {'publisher_id': 'rakuten_pub_id'},
    'aliexpress': {'aff_short_key': 'my_key'},
    'shareasale': {'userid': '12345', 'merchantid': '6789', 'merchant_domain': 'merchant.com'},
    'cj': {'pid': '123', 'aid': '456', 'merchant_domain': 'merchant.com'},
    'impact': {'base_url': 'https://brand.pxf.io/c/123/45', 'merchant_domain': 'brand.com'},
    'rakuten': {'publisher_id': 'pub_123', 'merchant_id': 'mid_456', 'merchant_domain': 'merchant.com'},
    'skimlinks': {'publisher_id': '12345X67890'},
    'awin': {'publisher_id': '123', 'merchant_id': '456', 'merchant_domain': 'merchant.com'}
}

# Initialize converter
converter = AffiliateConverter(config)

# Convert URLs
amazon_url = converter.convert("https://www.amazon.com/dp/B08F7PTF53")
print("Amazon:", amazon_url)

ebay_url = converter.convert("https://www.ebay.com/itm/123456789")
print("eBay:", ebay_url)
```

## Extending Providers

The tool is designed to be easily extensible. To add a new provider:
1. Create a new file in `affiliate_link_converter/providers/`.
2. Inherit from `BaseProvider` and implement `can_handle(self, url)` and `convert(self, url)`.
3. Register your provider in `affiliate_link_converter/converter.py`.

## Requirements

- Python 3.7+
- Standard library only (no external dependencies required).
