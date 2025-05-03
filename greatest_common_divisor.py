def gcd(a,b)->int:
    """
    The greatest common divisor(GCD) of a and b is the largest
    number that divides both of them with no reminder
    Euclid's alghoritm
    it is based on fact that, given two positive integers a and b,
    the common divisor of a and are the same as the common divisor of a-b and b
    GCD(a,a)=a
    GCD(a,b)=GCD(a-b,b) when a>b
    GCD(a,b)=GCD(a, b-a) when b>a"""
    if a<=0 or b<=0:
        raise ValueError("Numbers must be non negative and greater than 0")
    #base case
    if a == b:
        return a
    #recursive steps
    if a > b:
        return gcd(a-b, b)
    #when b> a
    return gcd(a, b-a)
def gcd_r(a,b):
    """This algorithm is based on the principle that
    gcd(a,b) = gcd(b,r), where r is the reminder when a
    is divided by b. The base case is gcd(a,0) = a"""
    #base
    if b == 0:
        return a
    #recursive step gcd(a,b)=gcd(b, a % b)
    else:
        return gcd_r(b, a % b)

print(gcd(48, 18))
print(gcd_r(48,18))

