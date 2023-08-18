import sys
import collections

n ,k = map(int, sys.stdin.readline().split())

queue = collections.deque()
result = []

for i in range(1, n + 1):
    queue.append(i)

while len(queue):
    queue.rotate(-k)
    result.append(queue.pop())

print("<", end='')
for i in range(len(result) - 1):
    print(result[i], end = ', ')

print(str(result[-1]) + ">", end='')