import string

p= string.punctuation
w= string.whitespace
empty_chars=['' for _ in range(len(p))]
tr= dict(zip(p, empty_chars))
mytable=str.maketrans(tr)


def clean_string(file):
    """Break each line of text to single words and strip
    whitespaces and punctuation
    Returns: dict
    """
    with open(file, 'r', encoding='UTF-8') as fin:
        d={}
        for line in fin:
            l= line.translate(mytable).strip().lower().split(' ')
            for word in l:
                if word not in d:
                    d[word] = 1
                else:
                    d[word]+=1
        return d
print(clean_string('Alice_Adeventures_in_wonderlad.txt'))