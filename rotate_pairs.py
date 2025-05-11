from caesar_cypher import caesar_cypher

def words_to_dict(file):
    """converts lines from a file to a dictionary"""
    d={}
    with open(file, 'r', encoding='UTF-8') as fin:
        for line in fin:
            d[line.strip()] = []
    return d


def rotate_pairs(d):
    """Uses caesar cypher to rotate words by n and checks
    if rotated string creates a word form the list"""
    for word in d:
        for i in range(1, 26):
            rotated= caesar_cypher(word, i)
            if rotated in d:
                d[word].append((i, rotated))

if __name__=='__main__':
    words=words_to_dict('words.txt')
    rotate_pairs(words)
    for key, value in words.items():
        if len(value) > 0:
            print(f'{key}: {value}')
