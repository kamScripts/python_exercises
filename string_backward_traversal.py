def backward_traversal(string):
    i=0
    j = -1
    while i < len(string):
        
        print(string[j])
        j-=1
        i+=1
backward_traversal("wolny weekend")