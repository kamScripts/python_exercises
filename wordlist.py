import time
def word_list(file):
    t=[]
    with open(file, 'r', encoding='UTF-8') as fin:
        for line in fin:
            t.append(line.strip())
    return t
def word_list2(file):
    t=[]
    with open(file, 'r', encoding='UTF-8') as fin:
        for line in fin:
            t= t + [line.strip()]
    return t
start1=time.time()
words=word_list('words.txt')
end1=time.time()
s2=time.time()
words_2= word_list2('words.txt')
e2=time.time()
print(f'append method {end1-start1}, el: {len(words)}, concatenation {e2-s2}, el: {len(words_2)}')