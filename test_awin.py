from affiliate_link_converter.converter import AffiliateConverter

def test_awin_conversion():
    config = {
        'awin': {
            'publisher_id': 'pub',
            'merchant_id': 'mid',
            'merchant_domain': 'etsy.com'
        }
    }
    converter = AffiliateConverter(config)
    result = converter.convert("https://www.etsy.com/listing/1")
    assert result == "https://www.awin1.com/cread.php?awinmid=mid&awinaffid=pub&ued=https%3A%2F%2Fwww.etsy.com%2Flisting%2F1"
