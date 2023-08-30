import sys

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

n, s = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
lst = []

for i in range(n):
    lst.append(abs(num_list[i] - s))

if len(lst) == 1:
    ans = lst[0]
else:
    ans = gcd(lst[0], lst[1])

for i in range(2, len(lst)):
    ans = gcd(ans, lst[i])

print(ans)

