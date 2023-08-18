import sys
import collections

n = int(sys.stdin.readline())
deque = collections.deque(enumerate(map(int, sys.stdin.readline().split())))
ans = []

while deque:
    index, num = deque.popleft()
    ans.append(index + 1)
    if num > 0:
        deque.rotate(-(num - 1))
    elif num < 0:
        deque.rotate(-num)

for i in ans:
    print(i, end = ' ')
    



