import urllib.parse
from .base import BaseProvider

class ImpactProvider(BaseProvider):
    """
    Generic Provider for Impact (Impact Radius).
    Expects config format: {'base_url': 'your_impact_base_url', 'merchant_domain': 'example.com'}
    """
    def can_handle(self, url: str) -> bool:
        domain = urllib.parse.urlparse(url).netloc.lower()
        merchant_domain = self.config.get('merchant_domain', '').lower()
        if merchant_domain and merchant_domain in domain:
            return True
        return False

    def convert(self, url: str) -> str:
        base_url = self.config.get('base_url')
        
        if not base_url:
            return url
            
        # Ensure the base url doesn't end with a slash so we can cleanly append
        base_url = base_url.rstrip('/')
        
        encoded_url = urllib.parse.quote(url, safe='')
        
        # Check if base_url already has parameters
        separator = '&' if '?' in base_url else '?'
        
        affiliate_url = f"{base_url}{separator}u={encoded_url}"
        return affiliate_url
