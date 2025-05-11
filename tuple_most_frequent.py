def count_letters(text):
    d={}
    count=0
    with open(text, 'r', encoding='UTF-8') as fin:
        for line in fin:
            for c in line.lower().strip():
                if c>='a':
                    count+=1
                    val = d.get(c, 0)
                    d[c] = val+1
    return (d,count)
pl=count_letters('sample_pl.txt')
eng=count_letters('sample_eng.txt')
de=count_letters('sample_de.txt')




def most_frequent(d):
    m_fr=[]
    count=d[1]
    for key, val in d[0].items():

        m_fr.append((val,f'{round(val/count*100,2)}%', key))
    m_fr.sort()
    return m_fr[::-1]

def print_output(t, lang):
    headers=('letters', 'frequency', 'counted')
    print('\n')
    print(lang.center(35, '*'), '\n')
    print('+', end=' ')
    print(': | '.join(headers), end=' ')
    print('+')
    print('|----------+------------+---------|')
    for c in t:
        print('| ',c[2].ljust(8), end='')
        print('|',c[1].ljust(11), end='')
        print('|',f'{c[0]}'.ljust(8), end='|')
        print()
    print('+----------+------------+---------+')
    
most_pl=most_frequent(pl)   
print_output(most_pl, 'Polish')