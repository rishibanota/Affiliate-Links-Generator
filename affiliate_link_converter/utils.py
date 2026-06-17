from urllib.parse import urlparse, urlunparse, parse_qs, urlencode

def update_url_query(url: str, params: dict) -> str:
    """
    Updates the query parameters of a URL.
    Replaces existing params or adds new ones.
    """
    parsed = urlparse(url)
    query = parse_qs(parsed.query)
    
    for key, value in params.items():
        if value is not None:
            query[key] = [value]
            
    # Rebuild the query string, preserving existing parameters that weren't overwritten
    new_query = urlencode(query, doseq=True)
    return urlunparse(
        (parsed.scheme, parsed.netloc, parsed.path, parsed.params, new_query, parsed.fragment)
    )
