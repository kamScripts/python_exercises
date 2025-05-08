import time
from wordlist import word_list as append_to_list

def in_bisect(target_value,sorted_list):
    """Binary search to check if a element is on the list
    
    search_item: str or number 
    sorted_list: list of sorted elements
    
    Returns: boolean"""

    l=0
    r=len(sorted_list)-1
    while l <=r:
        m= l+((r-l)//2)
        if target_value== sorted_list[m]:
            return True
        if sorted_list[m] < target_value:
            l = m+1
    
        if sorted_list[m] > target_value:
            r= m-1
    return False
t= append_to_list('words.txt')

s1=time.time()
print(in_bisect('wryly', t))
e1=time.time()
s2=time.time()
print('wryly' in t)
e2=time.time()
print(f'binary search time: {e1-s1}s, iteration search: {e2-s2}s')

