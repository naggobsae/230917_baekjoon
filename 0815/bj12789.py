import sys

n = int(sys.stdin.readline().rstrip())
stack = list(map(int, sys.stdin.readline().split()))
re_stack = []


for i in range(1, n + 1):
    if i not in stack:
        if re_stack:
            value = re_stack.pop()
            if value == i:
                if i == n:
                    print("Nice")
                continue
            else:
                print("Sad")
                break
        else:
            print("Sad")
            break
    else:
        while True:
            value = stack[0]
            re_stack.append(value)
            stack.remove(stack[0])
            if value == i:
                re_stack.pop()
                if i == n:
                    print("Nice")
                break