import time
def word_list(file):
    """Returns list of lines from a file
    
    file: file path
    
    Returns: list"""
    t=[]
    with open(file, 'r', encoding='UTF-8') as fin:
        for line in fin:
            t.append(line.strip())
    return t
def word_list2(file):
    t=[]
    with open(file, 'r', encoding='UTF-8') as fin:
        for line in fin:
            t= t + [line.strip()]
    return t

