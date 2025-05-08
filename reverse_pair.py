from in_list import in_bisect
from wordlist import word_list

words=word_list('words.txt')

def reversed_pairs(t):
    """Search for reversed words in the list
    
    t: list of strings
    
    Returns: list"""
    
    res=[]
    
    for el in t:
        if in_bisect(el[::-1], t):
            res.append((el, el[::-1]))
    return res
reversed= reversed_pairs(words)
print(reversed, len(reversed))    
