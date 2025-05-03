def gcd(a,b):
    """
    The greatest common divisor(GCD) of a and b is the largest
    number that """
    
    if b == 0:
        return a
    if a == b:
        return a
    if a > b:
        return gcd(a-b, b)

    if b > a:
        return gcd(a, b-a)
        
print(gcd(48, 18))