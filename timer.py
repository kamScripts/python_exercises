import time

def timer(func, *args):
    start= time.time()
    func(*args)
    stop=time.time()
    print(f'{func.__name__} Execution time: {round((stop-start)*1000, 6)} ms')