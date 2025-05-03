def is_power(a,b)->bool:
    """Checks if number a is a power of number b recursively
    'a' is a power of 'b' if it is divisable by 'b'
    and a/b is also a power of b
    """
    if b <=0:
        print('b should be positive')
        return False
    # if b equals 1, a must be 1 to be true
    if b==1:
        return a == 1
    #base case 1: if a equals b, it is b ** 1, which is a power of b
    if a == b:
        return True
    # base case 2: if a is not devisable by b, it fails the definition
    if a % b != 0 or a < b:
        return False
    # recursive step
    return is_power(a//b, b)
print(is_power(27, 3))