def extract_features(url):
    url = str(url)
    features = []
    
    # URL length
    features.append(len(url))
    
    # Number of digits
    features.append(sum(c.isdigit() for c in url))
    
    # Number of hyphens
    features.append(url.count('-'))
    
    # Safe parse for host
    if '//' in url:
        host = url.split('//')[1].split('/')[0]
    else:
        host = url.split('/')[0] if '/' in url else url
    
    # Has IP address (simple check)
    features.append(1 if '.' in host and all(part.replace('.','').isdigit() for part in host.split('.')) else 0)
    
    # Number of subdomains (simple)
    features.append(max(0, len(host.split('.')) - 2))
    
    # Has HTTPS
    features.append(1 if url.startswith('https') else 0)
    
    return features
