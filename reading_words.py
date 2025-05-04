def more_than_20_chars(file):
    with open(file, mode="r", encoding='UTF-8') as fin:
        line= fin.readline()
        for line in fin:
            word = line.strip()
            if len(word) > 20:
                print(word)
more_than_20_chars('words.txt')