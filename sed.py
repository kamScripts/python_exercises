def sed(pattern, replacement, file1, file2):
    """Reads a source file and writes the destination file.

    In each line, replaces pattern with replace.

    pattern: string
    replace: string
    file1: string filename
    file2: string filename
    """
    with open(file1, 'r', encoding='UTF-8') as f1:
        with open(file2, 'w', encoding='UTF-8') as f2:
            for line in f1:
                if pattern in line:
                    f2.write(line.replace(pattern, replacement))
def main():
    pn='się'
    rt='!!!!!!!!!'
    source='sample_pl.txt'
    copy='new.txt'
    sed(pn,rt,source,copy)
if __name__=='__main__':
    main()