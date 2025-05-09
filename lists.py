def nested_sum(t):
    """Adds up elements of the nested lists
    
    t: nested list of numbers
    
    Returns: Integer, sum of nested lists.
    """
    total=0
    for i in t:
        total+=sum(i)
    return total
a=[[1,2], [3], [4,5,6]]
#print(nested_sum(a))

def cumsum(t):
    """Cumulative sum, each elements is a sum of element
    and previous elements
    
    t: list of numbers
    
    [1,2,3]->[1,3,6]
    
    Returns: new list of cumulative sums of elements 
    """
    new_list=[]
    for i in range(len(t)):
        new_list.append(sum(t[:i+1]))
    return new_list
print(cumsum([1,2,3,4,5]))

def middle(t):
    """Removes first and last elements of the list
    
    t: list
    
    Returns: New list.
    """
    return t[1:-1]

#print(middle([1,2,3,4]))
def chop(t):
    """Modifies list by removing first and last element from the list.
    
    t: list
    
    Returns: None"""
    
    del t[0]
    del t[-1]
b=[1,2,3]
#chop(b)
#print(b)

def is_sorted(t):
    """Checks if list is sorted
    
    t: list
    
    Returns: Boolean"""
    return t==sorted(t)
#print(is_sorted([3,2]))

def is_anagram(word1, word2):
    """Checks if words are anagrams
    word1: string or list
    word2: string or list
    
    Returns: boolean"""
    #t= list(word1)
    #x= list(word2)
    #t.sort()
    #x.sort()
    #print(t,x)
    #if len(t) != len(x):
    #    return False
    #for i, l in enumerate(x):
#
    #    if t[i] != l:
    #        return False
    #return True
    return sorted(word1)==sorted(word2)
#print(is_anagram('ab1ca', 'bc1aa'))

def has_duplicates(t):
    """Checks list if any element appear more than once
    
    t: list
    
    Returns: boolean
    """
    sorted_list=sorted(t)
    for i in range(len(sorted_list)-1):
        if sorted_list[i] == sorted_list[i+1]:
            return True
    return False
print(has_duplicates([1,2,3,4,1]))