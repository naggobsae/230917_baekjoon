import sys

n = int(sys.stdin.readline())
stack = []

for i in range(n):
    order = sys.stdin.readline().rstrip()
    if order[:4] == "push":
        stack.append(int(order[5:]))
    elif order == "pop":
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    elif order == "size":
        print(len(stack))
    elif order == "empty":
        if not stack:
            print(1)
        else:
            print(0)
    elif order == "top":
        if not stack:
            print(-1)
        else:
            print(stack[-1])