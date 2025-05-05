import math

def read_text(file, func, *args):
    with open(file, 'r', encoding='UTF-8') as fin:
        for line in fin:
            func(args)

def more_than_20_chars(word:str)->None:
    """Find and print strings with more than 20 chars.
        
        word - string
        
        returns: word longer than 20 characters.
    """
    word = word.strip()
    if len(word) > 20:
        return word

def has_no_e(word:str)->bool:
    """Check if a word contains letter 'e'.
    
        word: string 
               
        Returns: True if string does not contain 'e'
    """
    return word.find('e')==-1
def check_percentage(f, func)->float:
    """Measures how many times words meeting condition occur on the list.
    
    f: class '_io.TextIOWrapper' - opened text file.
    func: class 'function' - condition to check.
    
    Returns: float - Percentage of words in the list that meet condition.
    """
    total = 0
    counter = 0
    
    for line in f:
        total+=1
        stripped= line.strip()

        if func(stripped):
            counter+=1

    return round(counter/total * 100, 4)

def avoids(word, forbidden_letters):
    for l in word:
        if  l in forbidden_letters:
            return False
    return True
def uses_only(word, allowed_letters):
    """Returns True if word contains only letters in the list."""
    for l in word:
        if not l in allowed_letters:
            return False
    return True
def uses_all(word, allowed_all):
    """Returns True if word uses all required letters."""
    for l in allowed_all:
        if l not in word:
            return False
    return True
d
with open('words.txt', 'r', encoding='UTF-8') as fin:
    #res = check_percentage(fin, has_no_e)
    #print(res, '%')
    for line in fin:
        word=line.strip()
        if uses_only(word, 'aeiou'):
           print(word)


