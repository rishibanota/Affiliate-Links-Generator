from .providers.amazon import AmazonProvider
from .providers.flipkart import FlipkartProvider
from .providers.ebay import EbayProvider
from .providers.walmart import WalmartProvider
from .providers.aliexpress import AliExpressProvider
from .providers.shareasale import ShareASaleProvider
from .providers.cj import CJProvider
from .providers.impact import ImpactProvider
from .providers.rakuten import RakutenProvider
from .providers.skimlinks import SkimlinksProvider
from .providers.awin import AwinProvider

class AffiliateConverter:
    """
    Manager class to handle conversion across multiple providers.
    """
    def __init__(self, config=None):
        self.config = config or {}
        # Initialize providers with their respective configs
        self.providers = []
        
        provider_map = {
            'amazon': AmazonProvider,
            'flipkart': FlipkartProvider,
            'ebay': EbayProvider,
            'walmart': WalmartProvider,
            'aliexpress': AliExpressProvider,
            'shareasale': ShareASaleProvider,
            'cj': CJProvider,
            'impact': ImpactProvider,
            'rakuten': RakutenProvider,
            'skimlinks': SkimlinksProvider,
            'awin': AwinProvider
        }
        
        for key, provider_class in provider_map.items():
            if key in self.config:
                self.providers.append(provider_class(self.config[key]))

    def convert(self, url: str) -> str:
        """
        Convert a normal URL to an affiliate URL based on the matching provider.
        """
        for provider in self.providers:
            if provider.can_handle(url):
                return provider.convert(url)
        
        # If no provider matches, return the original URL
        return url
