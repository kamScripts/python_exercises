from lists import has_duplicates
from timer import timer

def has_duplicates_dict(t):
    """takes a list of parameters and returns True if any
    element appears more than once."""
    
    d={}
    for el in t:
        val = d.get(el, 0)
        d[el] = val+1
        if d[el] > 1:
            return True
    return False

if __name__=='__main__':
    timer(has_duplicates, [1,2,3,4,5,6,7,8,9,1])
    timer(has_duplicates_dict, [1,2,3,4,5,6,7,8,9,1])