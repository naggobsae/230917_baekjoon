stack = []

time = int(input())

for i in range(time):
    n = input().rstrip()
    if len(n) > 1:
        stack.append(int(n[2:]))
    else:
        if n == '2':
            if len(stack) < 1:
                print(-1)
            else:
                print(stack[-1])
                stack.pop()
        elif n == '3':
            print(len(stack))
        elif n == '4':
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        else:
            if len(stack) < 1:
                print(-1)
            else:
                print(stack[-1])