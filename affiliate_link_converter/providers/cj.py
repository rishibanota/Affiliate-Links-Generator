import urllib.parse
from .base import BaseProvider

class CJProvider(BaseProvider):
    """
    Generic Provider for CJ Affiliate (Commission Junction).
    Expects config format: {'pid': 'your_property_id', 'aid': 'ad_id', 'merchant_domain': 'example.com'}
    """
    def can_handle(self, url: str) -> bool:
        domain = urllib.parse.urlparse(url).netloc.lower()
        merchant_domain = self.config.get('merchant_domain', '').lower()
        if merchant_domain and merchant_domain in domain:
            return True
        return False

    def convert(self, url: str) -> str:
        pid = self.config.get('pid') # Website ID
        aid = self.config.get('aid') # Ad ID
        
        if not pid or not aid:
            return url
            
        encoded_url = urllib.parse.quote(url, safe='')
        
        # CJ often uses various tracking domains like www.kqzyfj.com, www.jdoqocy.com, www.anrdoezrs.net
        # anrdoezrs.net is a standard default for deep links.
        affiliate_url = (
            f"https://www.anrdoezrs.net/click-{pid}-{aid}?url={encoded_url}"
        )
        return affiliate_url
