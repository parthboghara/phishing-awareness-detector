import re

def extract_features(url: str):
    """
    Extract numerical features from a URL for phishing detection
    """
    return [
        len(url),
        url.count('.'),
        url.count('-'),
        url.count('@'),
        1 if url.startswith("https") else 0,
        1 if re.search(r'login|secure|verify|account|update', url.lower()) else 0
    ]
