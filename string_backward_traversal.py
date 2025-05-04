def backward_traversal(string):
    """traverse string characters backward"""
    j = -1
    while j >  -len(string)-1:
        print(string[j])
        j-=1        
backward_traversal("wolny weekend")