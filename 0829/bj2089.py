import sys

num = int(sys.stdin.readline())

ans = []

if num == 0:
    print(0)
    exit()

while num:
    if num % (-2) == 0:
        ans.append(0)
        num = num // (-2)
    else:
        ans.append(1)
        num = num // (-2) + 1

for i in range(1, len(ans) + 1):
    print(ans[-i], end='')