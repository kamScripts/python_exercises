import string
from dict_histogram import histogram
import timer
import random
from bisect import bisect
p= string.punctuation+'“”‘’'+'0123456789'
spaces= [' ' for i in range(len(p))]
w= string.whitespace
translation_dict= dict(zip(p, spaces))
translation_table=str.maketrans(translation_dict)


def clean_string(file):
    """Break each line of text to single words and strip
    whitespaces and punctuation
    Returns: tuple (dict, total_words, unique_words)
    """
    with open(file, 'r', encoding='UTF-8') as fin:
        d={}
        for line in fin:
            line=line.translate(translation_table)
            for word in line.split():
                word=word.lower()
                d[word]= d.get(word, 0) + 1
        return d, sum(d.values()), len(d)
def find_20_most_common(d):
    """Find 20 most common words in the dictionary"""
    items=sorted(d.items(), key=lambda item: item[1], reverse=True)
    return items[:20]
def print_results(t):
    """print elements of the list of 2 el. tuples"""
    print('most common words')
    for fr, key in t:
        print(key, fr, sep='\t')
def subtract(d1, d2):
    """Display words from d1 that are not listed in d2"""
    words={}
    for key in d1:
        if key not in d2:
            words[key]=None
    return words
def set_subtract(d1,d2):
    """Display the difference between sets of words
    Set approach may be slower than version with loop
    as it has to copy data and create new data structures"""
    return set(d1)-set(d2)
def random_word(h):
    t=[]
    for word,freq in h.items():
        t.extend([word]*freq)
    return random.choice(t)
def random_w(h):
    total_freq=0
    ws=[]
    freqs=[]
    for word, freq in h.items():
        total_freq+=freq
        ws.append(word)
        freqs.append(total_freq)
    x=random.randint(0, total_freq-1)
    index=bisect(freqs,x)
    
    return ws[index]

    
if __name__=='__main__':
#    alice, at, au=clean_string('Alice_Adeventures_in_wonderlad.txt')
#   shakespeare, st, su=clean_string('shakespeare.txt')
#    jekyll_and_hyde, jt, ju=clean_string('jekyll_and_hyde.txt')
#    print('Alice in the Wonderland\n',find_20_most_common(alice),
#          f'total words count: {at}, unique words count: {au}')
#    print('Shakespeare poetry\n',find_20_most_common(shakespeare),
#          f'total words count: {st}, unique words count: {su}')
#    print('Mr. Jekyll and Mr. Hyde\n',find_20_most_common(jekyll_and_hyde),
#          f'total words count: {jt}, unique words count: {ju}')
    emma,et,eu=clean_string('emma.txt')
    words, wt, wu = clean_string('words.txt')
#    timer.timer(set_subtract, emma,words)
#    timer.timer(subtract, emma, words)
    print_results(find_20_most_common(emma))
    for key in emma:
        if len(key)==4:
            print(key)
    
   