import collections
import sys

n = int(sys.stdin.readline())

queue = collections.deque()

for i in range(1, n + 1):
    queue.append(i)

while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue[0])