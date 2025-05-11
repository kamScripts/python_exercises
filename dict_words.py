from wordlist import word_list as append_to_list
from in_list import in_bisect
from timer import timer
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
if __name__ == '__name__':
    words_d=words_dict('words.txt')
    words_list= append_to_list('words.txt')
    timer(in_bisect, 'table', words_list)
    timer(words_d.get, 'table')

