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

