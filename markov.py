"""This module contains a code example related to

Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Copyright 2015 Allen Downey

License: http://creativecommons.org/licenses/by/4.0/
"""
import random
suffixes_map={}
prefix=()
def read_file(file, prefix_len=2):

    with open(file,'r',encoding='UTF-8') as fin:
        for line in fin:

            for word in line.strip().split():
                process_word(word, prefix_len)
                
def process_word(word, prefix_len=2):
    global prefix
    if len(prefix)<prefix_len:
        prefix+=(word,)
        return
    try:
        suffixes_map[prefix].append(word)
    except KeyError:
        suffixes_map[prefix]= [word]
    prefix = prefix[1:]+ (word,)
def random_text(length=300):
    start = random.choice(list(suffixes_map.keys()))
    
    for i in range(length):
        suffixes = suffixes_map.get(start, None)
        if suffixes == None:
            # if the start isn't in map, we got to the end of the
            # original text, so we have to start again.
            random_text(length-i)
            return

        # choose a random suffix
        word = random.choice(suffixes)
        print(word, end=' ')
        start = start[1:]+(word,)
#read_file('emma.txt')
read_file('emma.txt')

random_text()