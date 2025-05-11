def rotate_letter(l, n):
    """Rotate letter characters by n spaces"""
    if l.isupper():
        start=ord('A')
    elif l.islower():
        start=ord('a')
    else:
        return l
    char=ord(l) - start
    i = (char + n) % 26 + start
    return chr(i)
def caesar_cypher(string, n):
    """Rotate string by n spaces"""
    encrypted = ''
    for c in string:
        encrypted += rotate_letter(c, n)
    return encrypted

