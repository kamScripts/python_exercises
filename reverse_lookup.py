import histogram
def reverse_lookup(d, v):
    """Reverse lookup is much slower than forward lookup"""
    for k in d:
        if d[k] == v:
            return k
    raise LookupError()


d=histogram.histogram('Blood and Transplant')
print(reverse_lookup(d, 3))