import sys

n = int(sys.stdin.readline())

for i in range(n):
    check = False
    stack = []
    ps = sys.stdin.readline().rstrip()
    for i in range(len(ps)):
        if ps[i] == '(':
            stack.append(ps[i])
        else:
            if not stack:
                check = True
                break
            else:
                stack.pop()
    if not stack and not check:
        print("YES")
    else:
        print("NO")