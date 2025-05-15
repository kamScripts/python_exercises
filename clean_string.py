import string

p= string.punctuation+'“”‘’'
w= string.whitespace
empty_chars=['' for _ in range(len(p))]
w_e_c =[' ' for _ in range(len(w))]
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
        fin.seek(52)
        print(fin.readline())
        for line in fin:
            line=line.translate(mytable)
            l= line.strip().lower().split(' ')
            for word in l:
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
words, t, u=clean_string('Alice_Adeventures_in_wonderlad.txt')
print(words, t, u)