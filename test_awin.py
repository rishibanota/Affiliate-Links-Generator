from affiliate_link_converter.converter import AffiliateConverter
config = {
    'awin': {
        'publisher_id': 'pub',
        'merchant_id': 'mid',
        'merchant_domain': 'etsy.com'
    }
}
converter = AffiliateConverter(config)
print(converter.convert("https://www.etsy.com/listing/1"))
