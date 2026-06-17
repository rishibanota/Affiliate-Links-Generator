import urllib.parse
from .base import BaseProvider

class ShareASaleProvider(BaseProvider):
    """
    Generic Provider for ShareASale merchants.
    Expects config format: {'userid': 'your_user_id', 'merchantid': 'target_merchant_id', 'bannerid': 'optional_banner_id'}
    """
    def can_handle(self, url: str) -> bool:
        # ShareASale can handle any domain as long as it's for a merchant you are approved for.
        # But for auto-conversion, we either need a mapping of domain -> merchant ID,
        # or we just assume if ShareASale config is provided, we can wrap it if it matches the merchant's domain.
        # For simplicity, we'll check if a specific merchant ID is provided in the config and wrap it.
        # However, to avoid wrapping everything, we could just check a custom attribute, but let's implement a domain check.
        # This will be a generic wrapper if merchant domain matches an expected list, but since we don't have it,
        # we will only convert if this provider is explicitly forced, or we can check if it's NOT a known competitor.
        # Alternatively, we'll just return False here and require explicit routing, OR we can check if config has 'merchant_domain'
        domain = urllib.parse.urlparse(url).netloc.lower()
        merchant_domain = self.config.get('merchant_domain', '').lower()
        if merchant_domain and merchant_domain in domain:
            return True
        return False

    def convert(self, url: str) -> str:
        userid = self.config.get('userid')
        merchantid = self.config.get('merchantid')
        
        if not userid or not merchantid:
            return url
            
        bannerid = self.config.get('bannerid', '0')
        encoded_url = urllib.parse.quote(url, safe='')
        
        affiliate_url = (
            f"https://www.shareasale.com/r.cfm?"
            f"b={bannerid}&u={userid}&m={merchantid}&urllink={encoded_url}"
        )
        return affiliate_url
