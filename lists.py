def nested_sum(t):
    """Adds up elements of the nested lists
    
    t: nested list of numbers
    
    Returns: Integer, sum of nested lists.
    """
    total=0
    for i in range(len(t)):
        total+=sum(t[i])
    return total
a=[[1,2], [3], [4,5,6]]
print(nested_sum(a))

def cumsum(t):
    """Cumulative sum, add previous elements of the list
    
    t: list of numbers
    
    [1,2,3]->[1,3,6]
    
    Returns: new list of cumulative sums of elements 
    """
    new_list=[]
    for i in range(len(t)):
        new_list.append(sum(t[:i+1]))
    return new_list
print(cumsum([1,2,3,4,5]))