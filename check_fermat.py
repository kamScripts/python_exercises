
def check_fermat(a, b, c, n):
    """Check if Fermat's Last Theorem holds
    there are no positive integers a,b and c such that
    a**n + b**n = c**n for any value > 2 """
    
    
    eq_left = a ** n + b ** n
    eq_right = c ** n
    if n > 2:
        if eq_left == eq_right:
            print('Holy smokes, Fermat was wrong')
        else:
            print(f'No, that doesn\'t work {eq_left} not equal {eq_right}')
    else:
        print('n need to be greater than 2')

check_fermat(3, 3, 4, 3)