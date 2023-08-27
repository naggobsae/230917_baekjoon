# 풀이 1 : 당연히 시간초과
# import sys

# n, m = map(int, sys.stdin.readline().split())
# count = 0

# def factorial(n):
#     res = 1
#     for i in range(2, n + 1):
#         res *= i
    
#     return res

# num = factorial(n) / (factorial(m) * factorial(n - m))

# while num % 10 == 0:
#     count += 1
#     num // 10

# print(count)

# 풀이 2
import sys

n, m = map(int, sys.stdin.readline().split())

def two_count(n):
    count = 0
    while n != 0:
        n = n // 2
        count += n
    return count

def five_count(n):
    count = 0
    while n != 0:
        n = n // 5
        count += n
    return count

num_of_two = two_count(n) - (two_count(m) + two_count(n - m))
num_of_five = five_count(n) - (five_count(m) + five_count(n - m))

print(min(num_of_two, num_of_five))

