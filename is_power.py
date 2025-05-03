def is_power(a,b)->bool:
    """Checks if number a is a power of number b recursively
    'a' is a power of 'b' if it is divisable by 'b'
    and a/b is also a power of b
    """
    if b <=0:
        print('b should be positive')
        return False

    if b==1:
        return a == 1

    if a == b:
        return True
    if a % b != 0 or a < b:
        return False
    return is_power(a//b, b)
print(is_power(27, 3))