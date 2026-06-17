import urllib.parse
from .base import BaseProvider

class WalmartProvider(BaseProvider):
    """
    Provider for Walmart (via Rakuten LinkSynergy).
    Expects config format: {'publisher_id': 'your_rakuten_publisher_id'}
    """
    def can_handle(self, url: str) -> bool:
        parsed = urllib.parse.urlparse(url)
        return 'walmart.com' in parsed.netloc.lower()

    def convert(self, url: str) -> str:
        publisher_id = self.config.get('publisher_id')
        if not publisher_id:
            return url
            
        # Base Rakuten LinkSynergy format
        # Walmart's Merchant ID is 2149
        merchant_id = "2149"
        
        # We need to URL encode the product URL
        encoded_url = urllib.parse.quote(url, safe='')
        
        affiliate_url = (
            f"https://click.linksynergy.com/deeplink?"
            f"id={publisher_id}&mid={merchant_id}&murl={encoded_url}"
        )
        return affiliate_url
