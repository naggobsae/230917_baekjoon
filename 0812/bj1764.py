import sys

n, m = map(int, sys.stdin.readline().split())

dic = {}
count = 0
ans = []

for i in range(n):
    dic[sys.stdin.readline().rstrip()] = 1

for i in range(m):
    listen = sys.stdin.readline().rstrip()
    if listen in dic:
        dic[listen] = 2

for i in dic:
    if dic[i] == 2:
        count += 1
        ans.append(i)

ans.sort()
print(count)
for i in ans:
    print(i)