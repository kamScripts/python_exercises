import math
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
    
    file: list - text file
    func: function - condition to check
    
    Returns: float - Percentage of words in the list that meet condition.
    """
    total = 0
    counter = 0
    
    for line in fin:
        total+=1
        stripped= line.strip()

        if func(stripped):
            counter+=1

    return round(counter/total * 100, 4)

with open('words.txt', 'r', encoding='UTF-8') as fin:
    res = check_percentage('words.txt', has_no_e)
    print(res, '%')