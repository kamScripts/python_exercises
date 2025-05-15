def count_letters(text):
    d={}
    count=0
    with open(text, 'r', encoding='UTF-8') as fin:
        for line in fin:
            for c in line.lower().strip():
                if c>='a':
                    count+=1
                    d[c] = d.get(c, 0)+1
    return (d,count)

def most_frequent(d):
    m_fr=[]
    count=d[1]
    for key, val in d[0].items():

        m_fr.append((val,f'{round(val/count*100,2)}%', key))
    m_fr.sort(reverse=True)
    return m_fr

def print_output(t, lang):
    headers=('letters', 'frequency', 'counted')
    print('\n')
    print(lang.center(35, '*'), '\n')
    print('+', end=' ')
    print(': | '.join(headers), end=' ')
    print('+')
    print('|----------+------------+---------|')
    for val, fr, c in t:
        print('| ',c.ljust(8), end='')
        print('|',fr.ljust(11), end='')
        print('|',f'{val}'.ljust(8), end='|')
        print()
    print('+----------+------------+---------+')
if __name__=='__main__':
    pl=count_letters('sample_pl.txt')
    print(pl[0])
    eng=count_letters('sample_eng.txt')
    de=count_letters('sample_de.txt')
    most_pl=most_frequent(pl)
    most_de=most_frequent(de)
    most_eng=most_frequent(eng)
    print(pl[1])
    print_output(most_pl, 'Polish')
    print(eng[1])
    print_output(most_eng, 'English')
    print(de[1])
    print_output(most_de, 'German')
