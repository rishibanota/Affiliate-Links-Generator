import urllib.parse
from .base import BaseProvider

class AliExpressProvider(BaseProvider):
    """
    Provider for AliExpress Portals.
    Expects config format: {'aff_short_key': 'your_short_key'}
    """
    def can_handle(self, url: str) -> bool:
        parsed = urllib.parse.urlparse(url)
        return 'aliexpress.com' in parsed.netloc.lower()

    def convert(self, url: str) -> str:
        aff_short_key = self.config.get('aff_short_key')
        if not aff_short_key:
            return url
            
        encoded_url = urllib.parse.quote(url, safe='')
        
        affiliate_url = (
            f"https://s.click.aliexpress.com/deep_link.htm?"
            f"aff_short_key={aff_short_key}&dl_target_url={encoded_url}"
        )
        return affiliate_url
