import sys

n = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))
ans = [1] * n

for i in range(1, n):
    for j in range(i):
        if seq[i] > seq[j]:
            ans[i] = max(ans[i], ans[j]+1)

print(max(ans))