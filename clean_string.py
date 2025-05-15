import string

p= string.punctuation+'“”‘’'
w= string.whitespace
empty_chars=['' for _ in range(len(p))]
tr= dict(zip(p, empty_chars))
mytable=str.maketrans(tr)

def clean_string(file):
    """Break each line of text to single words and strip
    whitespaces and punctuation
    Returns: tuple (dict, total_words, unique_words)
    """
    with open(file, 'r', encoding='UTF-8') as fin:
        d={}
        unique=0
        total=0
        
        for line in fin:
            if line.startswith('CHAPTER'):
                continue
            line=line.translate(mytable)
            l= line.strip(w).lower().split(' ')
            for word in l:
                if len(word)==1:
                    continue
                if word.isnumeric():
                    continue
                if word in w or word.isdigit():
                    continue
                if word not in d:
                    unique+=1
                    total+=1
                    d[word.strip('—')] = 1
                else:
                    total+=1
                    d[word]+=1
        return d, total, unique
def find_20_most_common(d):
    """Find 20 most common words in the dictionary"""
    items=[(index, val) for val, index in d.items()]
    
    items.sort(reverse=True)
    return items[:20]

alice, at, au=clean_string('Alice_Adeventures_in_wonderlad.txt')
shakespeare, st, su=clean_string('shakespeare.txt')
jekyll_and_hyde, jt, ju=clean_string('jekyll_and_hyde.txt')
print('Alice in the Wonderland\n',find_20_most_common(alice), f'total words count: {at}, unique words count: {au}')
print('Shakespeare poetry\n',find_20_most_common(shakespeare), f'total words count: {st}, unique words count: {su}')
print('Mr. Jekyll and Mr. Hyde\n',find_20_most_common(jekyll_and_hyde), f'total words count: {jt}, unique words count: {ju}')
