def caesar_cypher(string, cypher):
    encrypted = ''
    for c in string:
        encrypted += chr(ord(c) + cypher)
    return encrypted
print(caesar_cypher('HAL', -1))