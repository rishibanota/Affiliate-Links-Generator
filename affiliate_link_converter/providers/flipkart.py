from urllib.parse import urlparse
from .base import BaseProvider
from ..utils import update_url_query

class FlipkartProvider(BaseProvider):
    """
    Provider for Flipkart Affiliate.
    Expects config format: {'affid': 'your_flipkart_id'}
    """
    def can_handle(self, url: str) -> bool:
        parsed = urlparse(url)
        return 'flipkart.com' in parsed.netloc.lower()

    def convert(self, url: str) -> str:
        affid = self.config.get('affid')
        if not affid:
            return url
            
        return update_url_query(url, {'affid': affid})
