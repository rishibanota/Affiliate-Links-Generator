# Contributing Guidelines

Thank you for considering contributing to **Affiliate Links Generator**! 🎉

We welcome contributions of all kinds, including bug reports, new feature suggestions, additions of new affiliate providers, documentation improvements, and code refactoring.

Please read through these guidelines to ensure a smooth and effective contribution process.

---

## 📜 Code of Conduct

By participating in this project, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md). Please report any unacceptable behavior to the project maintainers.

---

## 🚀 Quick Start & Development Setup

### 1. Fork & Clone the Repository

Fork the repository on GitHub, then clone your fork locally:

```bash
git clone https://github.com/YOUR-USERNAME/Affiliate-Links-Generator.git
cd Affiliate-Links-Generator
```

### 2. Set Up a Virtual Environment (Recommended)

```bash
# Create a virtual environment
python -m venv venv

# Activate it (Windows)
.\venv\Scripts\activate

# Activate it (macOS/Linux)
source venv/bin/activate
```

### 3. Install in Editable Mode

```bash
pip install -e .
```

---

## 🏗️ Project Architecture

```text
Affiliate-Links-Generator/
├── affiliate_link_converter/
│   ├── __init__.py
│   ├── converter.py           # Core AffiliateConverter orchestration class
│   ├── utils.py               # Shared URL handling helper utilities
│   └── providers/             # Provider implementations
│       ├── __init__.py
│       ├── base.py            # BaseProvider abstract class
│       ├── amazon.py
│       ├── ebay.py
│       ├── flipkart.py
│       ├── awin.py
│       └── ...
├── main.py                    # CLI entry point (argparse)
├── setup.py                   # Package setup & distribution metadata
├── test_awin.py               # Unit tests / verification scripts
├── README.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
└── LICENSE
```

---

## 🔌 Adding a New Affiliate Provider

Extending Affiliate Links Generator with new e-commerce networks or affiliate platforms is easy. Follow these steps:

### Step 1: Create a Provider Class

Add a new Python file under `affiliate_link_converter/providers/<provider_name>.py`:

```python
from .base import BaseProvider
from urllib.parse import urlparse

class MyNetworkProvider(BaseProvider):
    """
    Affiliate provider implementation for MyNetwork.
    Config parameters:
        - provider_tag: str
    """

    def can_handle(self, url: str) -> bool:
        domain = urlparse(url).netloc.lower()
        return 'mynetwork.com' in domain

    def convert(self, url: str) -> str:
        tag = self.config.get('provider_tag')
        if not tag:
            return url
        # Construct affiliate link logic here
        separator = '&' if '?' in url else '?'
        return f"{url}{separator}ref={tag}"
```

### Step 2: Register Provider in `converter.py`

In `affiliate_link_converter/converter.py`:

1. Import your provider class:
   ```python
   from .providers.mynetwork import MyNetworkProvider
   ```
2. Add your provider to the `provider_map`:
   ```python
   provider_map = {
       ...
       'mynetwork': MyNetworkProvider,
   }
   ```

### Step 3: Add CLI Support in `main.py`

In `main.py`, add appropriate CLI arguments to `argparse` for your provider's credentials:

```python
parser.add_argument('--mynetwork-tag', help='MyNetwork Tracking Tag')
```

And update the `config` construction dictionary in `main.py`.

### Step 4: Write Tests & Documentation

1. Add unit test coverage verifying `can_handle()` and `convert()`.
2. Update `README.md` under **Features & Supported Providers** and CLI usage examples.

---

## 🎨 Coding Standards & Requirements

* **Python 3.7+ Compatibility**: Code must run seamlessly across Python 3.7 through 3.12+.
* **Zero Heavy Dependencies**: Rely primarily on the **Python Standard Library** (`urllib.parse`, `argparse`, `re`, `abc`, etc.) to keep the package lightweight and fast.
* **Code Style**:
  * Follow [PEP 8](https://peps.python.org/pep-0008/) style conventions.
  * Use clear variable names and explicit type hints (`str`, `bool`, `dict`, `Optional`).
  * Include clear docstrings for all classes and functions.
* **Error Resilience**: Gracefully return original URLs or handle malformed input without raising unhandled exceptions.

---

## 🧪 Testing Guidelines

Run tests locally before submitting your pull request:

```bash
# Run existing provider tests
python -m unittest discover -s . -p "test_*.py"
```

Ensure all new provider logic includes test cases for:
1. Standard product URLs.
2. URLs with pre-existing query parameters.
3. URLs with missing or partial configuration parameters.

---

## 📥 Submitting a Pull Request (PR)

1. **Create a Feature Branch**:
   ```bash
   git checkout -b feature/add-mynetwork-provider
   ```
2. **Commit Your Changes**:
   Write clear, concise commit messages:
   ```bash
   git commit -m "feat: add MyNetwork affiliate link provider"
   ```
3. **Push to Your Fork**:
   ```bash
   git push origin feature/add-mynetwork-provider
   ```
4. **Open a Pull Request**:
   * Navigate to the original repository on GitHub.
   * Fill out the [Pull Request Template](.github/PULL_REQUEST_TEMPLATE.md).
   * Reference any related issues (e.g., `Fixes #12`).

---

## 💡 Reporting Issues & Feature Requests

* Search existing [GitHub Issues](https://github.com/rishibanota/Affiliate-Links-Generator/issues) to avoid duplicates.
* Provide reproducible details, Python version, and sample URLs (without sensitive secrets).

Thank you for helping make Affiliate Links Generator better for everyone! 🚀
