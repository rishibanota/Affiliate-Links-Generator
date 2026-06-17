from urllib.parse import urlparse
from .base import BaseProvider
from ..utils import update_url_query

class EbayProvider(BaseProvider):
    """
    Provider for eBay Partner Network (EPN).
    Expects config format: {'campid': 'your_campaign_id', 'customid': 'optional_custom_id'}
    """
    def can_handle(self, url: str) -> bool:
        parsed = urlparse(url)
        return 'ebay.com' in parsed.netloc.lower()

    def convert(self, url: str) -> str:
        campid = self.config.get('campid')
        if not campid:
            return url
            
        customid = self.config.get('customid', '')
        
        # New eBay EPN tracking format parameters
        params = {
            'mkevt': '1',
            'mkcid': '1', # 1 for EPN
            'mkrid': '711-53200-19255-0', # Default rotation ID for eBay US
            'campid': campid,
            'toolid': '10001',
        }
        
        if customid:
            params['customid'] = customid
            
        return update_url_query(url, params)
