# basic invert_dict
from dict_histogram import histogram
def invert_dict(d):
    inverse = {}
    for key in d:
        val=d[key]
        if val not in inverse:
            inverse[val]=[key]
        else:
            inverse[val].append(key)
    return inverse
def invert_dict_a(d):
    """inverts keys and values, implementing
    
    d: dictionary
    
    Returns dictionary
    """
    inverse={}
    for key in d:
        val=d[key]
        inverse.setdefault(val, []).append(key)
    return inverse

if __name__== '__main__':
    s=histogram('placebo')
    print(s)
    di1= invert_dict(s)
    di2= invert_dict_a(s)
    print(f"basic func: {di1}\n setdefault func: {di2}")