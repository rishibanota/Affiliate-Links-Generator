<div align="center">
  <h1>🔗 Affiliate Links Generator</h1>
  <p><i>A modular, robust, and easy-to-use Python command-line tool to magically convert normal product URLs into your own affiliate links for various e-commerce platforms.</i></p>
  
  <a href="https://github.com/rishibanota/Affiliate-Links-Generator">
    <img src="https://img.shields.io/badge/GitHub-Repository-181717.svg?style=for-the-badge&logo=github" alt="GitHub Repository" />
  </a>
  <img src="https://img.shields.io/badge/Python-3.7+-blue.svg?style=for-the-badge&logo=python" alt="Python 3.7+" />
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge" alt="MIT License" />
  </a>
  <img src="https://img.shields.io/badge/Maintenance-Active-success.svg?style=for-the-badge" alt="Active Maintenance" />
</div>

<br/>

Welcome to the **Affiliate Links Generator**! 🎉 

Tired of manually generating affiliate links for different merchants? This tool makes it incredibly simple to automatically wrap or append your tracking IDs to regular product URLs. Whether you're working with Amazon, eBay, or 10+ other affiliate networks, we've got you covered!

---

## ✨ Features & Supported Providers

We support a wide array of top affiliate networks natively:

- 🛒 **Amazon Associates**: Seamlessly appends your `tag` to any Amazon URL.
- 📦 **eBay Partner Network (EPN)**: Adds EPN tracking parameters (`campid`, `mkevt`, `mkcid`) to eBay listings.
- 🛍️ **Flipkart Affiliate**: Appends your `affid` to Flipkart product URLs.
- 🏪 **Walmart (Rakuten LinkSynergy)**: Generates a deep link using your publisher ID.
- 🌏 **AliExpress Portals**: Generates deep links using your `aff_short_key`.
- 🤝 **ShareASale**: Auto-wraps URLs into deep links using your `merchantid` and `userid`.
- 💼 **CJ Affiliate**: Deep link generator using your `pid` (Website ID) and `aid` (Ad ID).
- 🎯 **Impact Radius**: Uses your Impact `base_url` to correctly redirect traffic.
- ⛩️ **Rakuten Advertising**: Deep link generator for the LinkSynergy network.
- 🪄 **Skimlinks**: Instantly wraps almost any merchant URL into a Skimlinks redirect using your `publisher_id`.
- 🌟 **Awin (Affiliate Window)**: Uses your `publisher_id` and `merchant_id` to generate trackable links.

---

## 🚀 Getting Started

### Installation

It's super easy to get up and running! Just clone the repo and install the package:

```bash
# Clone the repository
git clone https://github.com/rishibanota/Affiliate-Links-Generator.git

# Navigate into the project folder
cd Affiliate-Links-Generator

# Install the package locally
pip install -e .
```

---

## 💻 How to Use

You can use the Affiliate Links Generator directly from your terminal or integrate it into your own Python applications!

### 🎯 Command Line Interface (CLI)

Simply pass the target URL and your affiliate credentials as arguments:

```bash
# 🛒 Amazon Example
python main.py "https://www.amazon.com/dp/B08F7PTF53" --amazon-tag "your_tag-20"

# 📦 eBay Example
python main.py "https://www.ebay.com/itm/123456789" --ebay-campid "5338123456" --ebay-customid "my_campaign"

# 🛍️ Flipkart Example
python main.py "https://www.flipkart.com/some-product/p/itm1234" --flipkart-id "your_flip_id"

# 🏪 Walmart Example
python main.py "https://www.walmart.com/ip/some-product/123456" --walmart-publisher-id "rakuten_pub_id"

# 🤝 ShareASale Example
python main.py "https://www.example-merchant.com/product/123" \
    --shareasale-userid "123456" \
    --shareasale-merchantid "7890" \
    --shareasale-domain "example-merchant.com"
```
*(Check out the original `main.py` `--help` menu for a full list of commands for all providers!)*

---

### 🐍 Python API Integration

Want to use this in your web app or Discord bot? It's fully programmatic!

```python
from affiliate_link_converter.converter import AffiliateConverter

# 1. Setup your configuration dictionary
config = {
    'amazon': {'tag': 'your_tag-20'},
    'ebay': {'campid': '5338123456', 'customid': 'social_media'},
    'shareasale': {
        'userid': '12345', 
        'merchantid': '6789', 
        'merchant_domain': 'merchant.com'
    }
}

# 2. Initialize the converter
converter = AffiliateConverter(config)

# 3. Magically convert your URLs! ✨
amazon_url = converter.convert("https://www.amazon.com/dp/B08F7PTF53")
print("💰 Amazon Affiliate Link:", amazon_url)

ebay_url = converter.convert("https://www.ebay.com/itm/123456789")
print("💰 eBay Affiliate Link:", ebay_url)
```

---

## 🛠️ Extending Providers

Need a network that isn't supported yet? This tool is built to be highly extensible!

1. Create a new file in the `affiliate_link_converter/providers/` folder.
2. Inherit from the `BaseProvider` class and implement the `can_handle(self, url)` and `convert(self, url)` methods.
3. Register your shiny new provider in `affiliate_link_converter/converter.py`.

---

## 📋 Requirements

- **Python 3.7+**
- No external dependencies required! Everything runs perfectly using the Python Standard Library. 

---

## 👥 Community & Governance

We welcome contributions from everyone! Check out the links below to get involved:

- 🤝 **[Contributing Guidelines](CONTRIBUTING.md)**: Learn how to set up your environment and add new provider integrations.
- 📜 **[Code of Conduct](CODE_OF_CONDUCT.md)**: Our standards for maintaining a welcoming and inclusive community.
- 🛡️ **[Security Policy](SECURITY.md)**: Guidelines for reporting security vulnerabilities responsibly.
- 📄 **[License](LICENSE)**: This project is open-source and licensed under the **MIT License**.

---

<div align="center">
  <p>Made with ❤️ by <a href="https://github.com/rishibanota">Rishi Banota</a> and contributors.</p>
  <p>If you find this helpful, consider giving the <a href="https://github.com/rishibanota/Affiliate-Links-Generator">repository</a> a ⭐!</p>
</div>
