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
    
    Returns: tuple - (Percentage_of_words, count, total_words).
    """
    total = 0
    counter = 0
    
    for line in f:
        total+=1
        stripped= line.strip()

        if func(stripped):
            counter+=1
    return (round(counter/total * 100, 4), counter, total)

def avoids(word, forbidden_letters):
    """Returns True if characters are not on forbidden list."""
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
def is_abecedarian(word):
    """Checks if letters in a world appear in
    alphabetical order. Returns True or False"""
    for index, l in enumerate(word):
        if index == len(word)-1:
            break
        # this conditional doesn't need ord, only chars can be compared
        # to get the same effect. It is just cool new string method.
        if ord(word[index+1]) < ord(l):
            return False
    return True
def is_abecedarian_solution(word):
    """version from the book"""
    previous = word[0]
    for c in word:
        if c < previous:
            return False
        previous=c
    return True
def is_abecedarian_recursive(word):
    """recursive version from the book"""
    if len(word) <= 1:
        return True
    if word[0] > word[1]:
        return False
    return is_abecedarian(word[1:])
def three_doubles_finder(word):
    """Find word that has three consecutive double letters"""
    previous = word[0]

    i=1
    while i < len(word):
        if word[i] == previous:
            if i + 4 < len(word):
                return word[i+1]==word[i+2] and word[i+3]==word[i+4]
        else:
            previous=word[i]
        i+=1
    return False

with open('words.txt', 'r', encoding='UTF-8') as fin:
    #res = check_percentage(fin, has_no_e)
    #print(res, '%')
    for line in fin:
        stripped = line.strip()
        if three_doubles_finder(stripped):
            print(stripped)
    #fin.seek(0)
    #res = check_percentage(fin, is_abecedarian)
    #print(f'{res[0]}%, in alphabetical order: {res[1]}, total words: {res[2]}')

