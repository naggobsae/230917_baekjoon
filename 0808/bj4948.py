import math

def is_prime(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return 0
    return 1

prime_list = []
for i in range(123456*2 + 1):
    if i == 0 or i == 1:
        prime_list.append(0)
    else:
        prime_list.append(is_prime(i))

while True:
    n = int(input())
    if n == 0:
        break
    count = 0
    for i in range(n + 1, 2 * n + 1):
        if prime_list[i] == 1:
            count += 1
    print(count)