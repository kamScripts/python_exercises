def count_letters(text):
    d={}
    count=0
    with open(text, 'r', encoding='UTF-8') as fin:
        for line in fin:
            for c in line.lower().strip():
                if c>='a':
                    
                    val = d.get(c, 0)
                    d[c] = val+1
    return (d,c)
pl=count_letters('sample_pl.txt')
eng=count_letters('sample_eng.txt')
de=count_letters('sample_de.txt')




def most_frequent(d):
    m_fr=[]
    for key, val in d.items():

        m_fr.append((val, key))
    m_fr.sort()
    return m_fr[::-1]

print(most_frequent(pl[0]))
print(most_frequent(eng[0]))
print(most_frequent(de[0]))