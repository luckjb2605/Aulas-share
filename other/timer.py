import time

"""

for i in range(5, 0, -1):
    print(i, end = '\r', flush = True)
    time.sleep(1)
print('End.')

"""

n = int(input('Timer: How many seconds?'))

for i in range(n, 0, -1):
    print(f'Progress: {i} out of {n} seconds remaining', end = '\r', flush = True)
    time.sleep(1)
print('End.')