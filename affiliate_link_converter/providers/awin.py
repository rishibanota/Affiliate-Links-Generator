import urllib.parse
from .base import BaseProvider

class AwinProvider(BaseProvider):
    """
    Generic Provider for Awin (Affiliate Window).
    Expects config format: {'publisher_id': 'your_pub_id', 'merchant_id': 'merchant_id', 'merchant_domain': 'example.com'}
    """
    def can_handle(self, url: str) -> bool:
        domain = urllib.parse.urlparse(url).netloc.lower()
        merchant_domain = self.config.get('merchant_domain', '').lower()
        if merchant_domain and merchant_domain in domain:
            return True
        return False

    def convert(self, url: str) -> str:
        publisher_id = self.config.get('publisher_id')
        merchant_id = self.config.get('merchant_id')
        
        if not publisher_id or not merchant_id:
            return url
            
        encoded_url = urllib.parse.quote(url, safe='')
        
        affiliate_url = (
            f"https://www.awin1.com/cread.php?"
            f"awinmid={merchant_id}&awinaffid={publisher_id}&ued={encoded_url}"
        )
        return affiliate_url
