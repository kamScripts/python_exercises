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

with open('words.txt', 'r', encoding='UTF-8') as fin:
    #more_than_20_chars(fin)
    for line in fin:
        stripped= line.strip()
        if has_no_e(stripped):
            print(stripped)