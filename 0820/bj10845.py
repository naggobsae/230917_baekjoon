import sys
import collections

n = int(sys.stdin.readline())
queue = collections.deque()

for i in range(n):
    order = sys.stdin.readline().strip()
    if order[:4] == 'push':
        queue.append(int(order[5:]))
    elif order == 'pop':
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
    elif order == 'size':
        print(len(queue))
    elif order == 'empty':
        if not queue:
            print(1)
        else:
            print(0)
    elif order == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif order == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])