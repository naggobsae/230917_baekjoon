import sys

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def lcm(a, b):
    return int((a * b) / gcd(a, b))

a, b = map(int, sys.stdin.readline().split())

print(gcd(a, b))
print(lcm(a, b))