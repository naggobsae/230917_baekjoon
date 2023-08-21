# 풀이 1 : 시간 초과
# import sys

# n = int(sys.stdin.readline())

# seq = list(map(int, sys.stdin.readline().split()))

# for i in range(n):
#     temp = seq[i]
#     if i == n - 1:
#         print(-1, end=' ')
#     else:
#         for j in range(i+1, n):
#             if temp < seq[j]:
#                 print(seq[j], end=' ')
#                 break
#             if j == n - 1:
#                 print(-1, end=' ')

#풀이 2 : o(n^2)을 o(n)으로 바꿔서 풀 방법을 생각하자! stack을 활용

import sys

n = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))
stack = []
ans = [-1] * n

for i in range(n):
    while stack and seq[i] > stack[-1][1]:
        index, value = stack.pop()
        ans[index] = seq[i]

    stack.append([i, seq[i]])

print(*ans)
        