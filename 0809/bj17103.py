import math

def is_prime(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return 0
    return 1

def get_prime_list(n):
    lst = [0]*(n+1)
    for i in range(2, len(lst)):
        if is_prime(i):
            lst[i] = 1
    
    return lst

t = int(input())
nums = []

for i in range(t):
    n = int(input())
    nums.append(n)

max_num = max(nums)
prime_list = get_prime_list(max_num)

for i in nums:
    count = 0
    for j in range(2, i // 2 + 1):
        if prime_list[j] and prime_list[i - j]:
            count += 1
    print(count)
