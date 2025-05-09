def histogram(s):
    d= {}
    for c in s:
        v= d.get(c,0)
        d[c] = v+1
    return d
d=histogram('onomatopeja')
print(d.items())
