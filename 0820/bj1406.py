#1번 풀이 : 시간 초과
# import sys

# string = sys.stdin.readline().strip()
# str_list = list(string)

# n = int(sys.stdin.readline())

# cursor = len(str_list)
# for i in range(n):
#     order = sys.stdin.readline().strip()
#     if order == 'L':
#         if cursor > 0:
#             cursor -= 1
#     elif order == 'D':
#         if cursor < len(str_list):
#             cursor += 1
#     elif order == 'B':
#         if cursor > 0:
#             str_list.remove(str_list[cursor - 1])
#             cursor -= 1
#     else:
#         str_list.insert(cursor, order[2:])
#         cursor += 1

# print(''.join(str_list))

# 2번 풀이 : 커서를 기준으로 문자열을 스택 2개로 나누자!

import sys
import collections

str_list = list(sys.stdin.readline().strip())
n = int(sys.stdin.readline())
str2 = collections.deque()

for i in range(n):
    order = sys.stdin.readline().strip()
    if order == 'L':
        if str_list:
            str2.appendleft(str_list.pop())
    elif order == 'D':
        if str2:
            str_list.append(str2.popleft())
    elif order == 'B':
        if str_list:
            str_list.pop()
    else:
        str_list.append(order[2:])

str_list.extend(str2)
print(''.join(str_list))