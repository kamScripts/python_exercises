
def caesar_cypher(string, cypher):
    encrypted = ''
    for c in string:
        print((ord(c)+cypher))
    return encrypted   
print(caesar_cypher('HAL', -1))

