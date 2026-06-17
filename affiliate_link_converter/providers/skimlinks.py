import urllib.parse
from .base import BaseProvider

class SkimlinksProvider(BaseProvider):
    """
    Provider for Skimlinks.
    Expects config format: {'publisher_id': 'your_pub_id'}
    """
    def can_handle(self, url: str) -> bool:
        # Skimlinks can wrap practically any domain, so we convert if the config is set
        # and the URL is not already a skimlinks URL
        parsed = urllib.parse.urlparse(url)
        return 'skimresources.com' not in parsed.netloc.lower()

    def convert(self, url: str) -> str:
        publisher_id = self.config.get('publisher_id')
        
        if not publisher_id:
            return url
            
        encoded_url = urllib.parse.quote(url, safe='')
        
        affiliate_url = (
            f"https://go.skimresources.com/?"
            f"id={publisher_id}&url={encoded_url}"
        )
        return affiliate_url
