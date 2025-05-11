def fibonacci(n):
    """Find n number of the Fibonacci sequence"""
    if not isinstance(n, int):
        return None
    if n < 0:
        return None
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
def fibonacci_fast(n):
    known = {0:0, 1:1}
    def fibo(n):
        if n in known:
            return known[n]
        res = fibo(n-1) + fibo(n-2)
        known[n] = res
        return res
    return fibo(n)
print(fibonacci(10))


