from time import time


import time

def sum(n):
    initial_time = time.time()
    sum = 0
    for i in range(n + 1):
        sum += i
    
    execution_time = time.time() - initial_time

    return sum, execution_time

def chad_sum(n):
    initial_time = time.time()
    sum = n * (n + 1) / 2
    execution_time = time.time() - initial_time
    return sum, execution_time

