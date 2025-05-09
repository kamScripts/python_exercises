import time
from wordlist import word_list as append_to_list

def in_bisect(target_value,sorted_list):
    """Binary search to check if a element is on the list
    
    search_item: str or number 
    sorted_list: list of sorted elements
    
    Returns: boolean"""

    l=0
    r=len(sorted_list)-1
    if r == 0:
        return False
    while l <=r:
        m= l+((r-l)//2)
        if target_value== sorted_list[m]:
            return True
        if sorted_list[m] < target_value:
            l = m+1
    
        #if sorted_list[m] > target_value
        else:
            r= m-1
    return False

def in_bisect_r(target, sorted_list):
    """Recursive version"""

    if len(sorted_list)==0:
        return False

    mid=len(sorted_list)//2

    if sorted_list[mid]==target:
        return True

    if sorted_list[mid] < target:
        return in_bisect_r(target, sorted_list[mid+1:])
    return in_bisect_r(target, sorted_list[:mid])

#t= append_to_list('words.txt')
#
#s1=time.time()
#print(in_bisect('wryly', t))
#e1=time.time()
#s2=time.time()
#print('wryly' in t)
#e2=time.time()
#s3=time.time()
#print(in_bisect_r('wryly', t))
#e3=time.time()
#print(f"""
#      binary search: {e1-s1}s,
#      recursive b-search: {e3-s3}
#      iteration search: {e2-s2}s,
#      """)

