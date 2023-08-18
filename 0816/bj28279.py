import sys
import collections

deque = collections.deque()

n = int(sys.stdin.readline())

for i in range(n):
    order = sys.stdin.readline().strip()
    if order[0] == '1':
        deque.appendleft(int(order[2:]))
    elif order[0] == '2':
        deque.append(int(order[2:]))
    elif order == '3':
        if not deque:
            print(-1)
        else:
            print(deque.popleft())
    elif order == '4':
        if not deque:
            print(-1)
        else:
            print(deque.pop())
    elif order == '5':
        print(len(deque))
    elif order == '6':
        if not deque:
            print(1)
        else:
            print(0)
    elif order == '7':
        if not deque:
            print(-1)
        else:
            print(deque[0])
    elif order == '8':
        if not deque:
            print(-1)
        else:
            print(deque[-1])