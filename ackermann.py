def ack(m, n):
    """Computes the ackermann function"""
    if m == 0:
        return n + 1
    if n == 0:
        return ack(m - 1, 1)
    
    return ack(m -1, ack(m, n-1))
print(ack(3, 6))