import sys

a, b = map(int, sys.stdin.readline().split())

m = int(sys.stdin.readline())

num_list = list(map(int, sys.stdin.readline().split()))

base10 = 0

for i in range(1, len(num_list) + 1):
    base10 += num_list[-i] * (a**(i-1))

ans = []

while base10 != 0:
    ans.append(base10 % b)
    base10 = base10 // b

print(*ans[::-1])