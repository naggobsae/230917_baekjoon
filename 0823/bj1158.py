import sys
import collections

deque = collections.deque()

n, k = map(int, sys.stdin.readline().split())

for i in range(1, n + 1):
    deque.append(i)

print('<', end = '')
while len(deque) > 1:
    deque.rotate(-k)
    print(str(deque.pop()) + ',', end = ' ')

print(str(deque[-1]) + '>')