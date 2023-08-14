import sys

t = int(sys.stdin.readline())
stack = []
ans = 0

for i in range(t):
    n = int(sys.stdin.readline())
    if n == 0:
        stack.pop()
    else:
        stack.append(n)

for i in range(len(stack)):
    ans += stack[i]

print(ans)