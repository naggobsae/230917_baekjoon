import sys

n, d = map(int, sys.stdin.readline().split())
count = 0

for i in range(1, n + 1):
    num = str(i)
    for j in range(len(num)):
        if num[j] == str(d):
            count += 1

print(count)