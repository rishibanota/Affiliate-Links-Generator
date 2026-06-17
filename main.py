import argparse
import sys
from affiliate_link_converter.converter import AffiliateConverter

def main():
    parser = argparse.ArgumentParser(description="Convert normal product URLs to affiliate URLs.")
    parser.add_argument("url", help="The normal product URL to convert")
    parser.add_argument("--amazon-tag", help="Amazon Associate Tag (e.g., your_tag-20)", default=None)
    parser.add_argument("--flipkart-id", help="Flipkart Affiliate ID", default=None)
    parser.add_argument("--ebay-campid", help="eBay Campaign ID", default=None)
    parser.add_argument("--ebay-customid", help="eBay Custom ID", default=None)
    parser.add_argument("--walmart-publisher-id", help="Walmart (Rakuten) Publisher ID", default=None)
    
    # New Providers
    parser.add_argument("--aliexpress-key", help="AliExpress Portals Short Key", default=None)
    parser.add_argument("--shareasale-userid", help="ShareASale User ID", default=None)
    parser.add_argument("--shareasale-merchantid", help="ShareASale Merchant ID", default=None)
    parser.add_argument("--shareasale-domain", help="ShareASale Merchant Domain to trigger on", default=None)
    parser.add_argument("--cj-pid", help="CJ Affiliate Property ID (Website ID)", default=None)
    parser.add_argument("--cj-aid", help="CJ Affiliate Ad ID", default=None)
    parser.add_argument("--cj-domain", help="CJ Affiliate Merchant Domain to trigger on", default=None)
    
    # Even More Providers
    parser.add_argument("--impact-url", help="Impact Radius base tracking URL (e.g., https://brand.pxf.io/c/123/456)", default=None)
    parser.add_argument("--impact-domain", help="Impact Radius merchant domain", default=None)
    parser.add_argument("--rakuten-pubid", help="Rakuten Publisher ID", default=None)
    parser.add_argument("--rakuten-mid", help="Rakuten Merchant ID", default=None)
    parser.add_argument("--rakuten-domain", help="Rakuten Merchant Domain", default=None)
    parser.add_argument("--skimlinks-id", help="Skimlinks Publisher ID", default=None)
    parser.add_argument("--awin-pubid", help="Awin Publisher ID", default=None)
    parser.add_argument("--awin-mid", help="Awin Merchant ID", default=None)
    parser.add_argument("--awin-domain", help="Awin Merchant Domain", default=None)

    args = parser.parse_args()

    # Create config dictionary from arguments
    config = {}
    if args.amazon_tag:
        config['amazon'] = {'tag': args.amazon_tag}
    if args.flipkart_id:
        config['flipkart'] = {'affid': args.flipkart_id}
    if args.ebay_campid:
        config['ebay'] = {'campid': args.ebay_campid, 'customid': args.ebay_customid}
    if args.walmart_publisher_id:
        config['walmart'] = {'publisher_id': args.walmart_publisher_id}
    if args.aliexpress_key:
        config['aliexpress'] = {'aff_short_key': args.aliexpress_key}
    if args.shareasale_userid and args.shareasale_merchantid:
        config['shareasale'] = {
            'userid': args.shareasale_userid, 
            'merchantid': args.shareasale_merchantid,
            'merchant_domain': args.shareasale_domain
        }
    if args.cj_pid and args.cj_aid:
        config['cj'] = {
            'pid': args.cj_pid, 
            'aid': args.cj_aid,
            'merchant_domain': args.cj_domain
        }
    if args.impact_url and args.impact_domain:
        config['impact'] = {
            'base_url': args.impact_url,
            'merchant_domain': args.impact_domain
        }
    if args.rakuten_pubid and args.rakuten_mid:
        config['rakuten'] = {
            'publisher_id': args.rakuten_pubid,
            'merchant_id': args.rakuten_mid,
            'merchant_domain': args.rakuten_domain
        }
    if args.skimlinks_id:
        config['skimlinks'] = {'publisher_id': args.skimlinks_id}
    if args.awin_pubid and args.awin_mid:
        config['awin'] = {
            'publisher_id': args.awin_pubid,
            'merchant_id': args.awin_mid,
            'merchant_domain': args.awin_domain
        }

    if not config:
        print("Warning: No affiliate IDs provided. The URL might be returned as is or just normalized.")
        print("Use --help to see available arguments.")

    try:
        converter = AffiliateConverter(config)
        affiliate_url = converter.convert(args.url)
        print(f"\nOriginal URL:  {args.url}")
        print(f"Affiliate URL: {affiliate_url}\n")
    except Exception as e:
        print(f"Error converting URL: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
