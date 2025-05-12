
def words_dict(file):
    """Reads line from text files and stores them in the dictionary.
    {word: word backwards}
    
    file: file path
    
    Returns: dictionary
    """
    d={}
    with open(file, 'r', encoding='UTF-8') as fin:
        for line in fin:
            ln=line.strip()
            d[ln]= ln[::-1]
    return d
if __name__ == '__main__':
    words_d=words_dict('words.txt')
    print(words_d)

