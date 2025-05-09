def histogram(s):
    d= {}
    for c in s:
        v= d.get(c,0)
        d[c] = v+1
    return d
d=histogram('onomatopeja')
print(d.items())

def invert_dict(d):
    inverse = {}
    for key in d:
        val=d[key]
        if val not in inverse:
            inverse[val]=[key]
        else:
            inverse[val].append(key)
    return inverse
i=invert_dict(d)
print(i)  