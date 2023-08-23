import sys
import collections

deque = collections.deque()

n = int(sys.stdin.readline())

for i in range(n):
    order = sys.stdin.readline().rstrip()
    if order[:10] == "push_front":
        deque.appendleft(int(order[11:]))
    elif order[:9] == "push_back":
        deque.append(int(order[10:]))
    elif order == "pop_front":
        if not deque:
            print(-1)
        else:
            print(deque.popleft())
    elif order == "pop_back":
        if not deque:
            print(-1)
        else:
            print(deque.pop())
    elif order == "size":
        print(len(deque))
    elif order == "empty":
        if not deque:
            print(1)
        else:
            print(0)
    elif order == "front":
        if not deque:
            print(-1)
        else:
            print(deque[0])
    elif order == "back":
        if not deque:
            print(-1)
        else:
            print(deque[-1])