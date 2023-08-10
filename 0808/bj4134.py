import math

n = int(input())

def is_prime(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

def next_prime(n):
    while True:
        if is_prime(n):
            return n
        else:
            n += 1
        
for i in range(n):
    k = next_prime(int(input()))
    if k == 0 or k == 1:
        print(2)
    else:
        print(k)