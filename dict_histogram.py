def histogram(s):
    """Creates mapping of a string and counts how many time letters appear
    s: str
    Returns: dict"""
    d= {}
    for c in s:
        v= d.get(c,0)
        d[c] = v+1
    return d


