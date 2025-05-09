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
print(fibonacci(10))

