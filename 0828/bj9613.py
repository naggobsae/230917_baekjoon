import sys

t = int(sys.stdin.readline())

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

for i in range(t):
    num_list = list(map(int, sys.stdin.readline().split()))
    ans = 0
    for i in range(1, num_list[0] + 1):
        for j in range(i + 1, num_list[0] + 1):
            ans += gcd(num_list[i], num_list[j])
    print(ans)

