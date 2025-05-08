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
            print(l,r)
        if sorted_list[m] > target_value:

            r= m-1
    return False


print(in_bisect(10, [1,2,3,4,5,6]))