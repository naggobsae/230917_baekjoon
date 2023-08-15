import sys
import collections

n = int(sys.stdin.readline())
queue = collections.deque()

for i in range(n):
    order = sys.stdin.readline().rstrip()
    if order[:4] == "push":
        queue.append(int(order[5:]))
    elif order == "pop":
        if not queue:
            print(-1)
        else:
            print(queue.popleft()) # deque를 쓰지 않고 0번째 원소를 제거하면 O(n) 시간복잡도를 가져 오래 걸림
    elif order == "size":
        print(len(queue))
    elif order == "empty":
        if not queue:
            print(1)
        else:
            print(0)
    elif order == "front":
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif order == "back":
        if not queue:
            print(-1)
        else:
            print(queue[-1]) 