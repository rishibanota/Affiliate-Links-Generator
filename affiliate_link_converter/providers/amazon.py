from urllib.parse import urlparse
from .base import BaseProvider
from ..utils import update_url_query

class AmazonProvider(BaseProvider):
    """
    Provider for Amazon Associates.
    Expects config format: {'tag': 'your_associate_tag-20'}
    """
    def can_handle(self, url: str) -> bool:
        parsed = urlparse(url)
        domain = parsed.netloc.lower()
        # Handle amazon domains (e.g. amazon.com, amazon.co.uk, amazon.in)
        # Avoid matching aws.amazon.com
        return 'amazon' in domain and not domain.endswith('aws.amazon.com')

    def convert(self, url: str) -> str:
        tag = self.config.get('tag')
        if not tag:
            return url
            
        return update_url_query(url, {'tag': tag})
