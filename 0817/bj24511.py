# 1번 풀이 : 시간 초과
# import sys
# import collections

# n = int(sys.stdin.readline())

# is_stack = list(map(int, sys.stdin.readline().split()))
# queuestack = list(map(int, sys.stdin.readline().split()))
# m = int(sys.stdin.readline())
# insert = list(map(int, sys.stdin.readline().split()))

# for i in insert:
#     move = i
#     for j in range(len(is_stack)):
#         if is_stack[j] == 0:
#             temp = move
#             move = queuestack[j]
#             queuestack[j] = temp
#         else:
#             continue
#     print(move, end = ' ')

import sys
import collections

n = int(sys.stdin.readline())

is_stack = list(map(int, sys.stdin.readline().split()))
queuestack = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
insert = list(map(int, sys.stdin.readline().split()))
ans = collections.deque()

for i in range(n):
    if is_stack[i] == 0:
        ans.appendleft(queuestack[i])

for i in range(m):
    ans.append(insert[i])
    print(ans.popleft(), end = ' ')