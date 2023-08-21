import sys

stack = []
count = 0

pipe = sys.stdin.readline().rstrip()

for i in range(len(pipe)):
    if pipe[i] == '(' and pipe[i + 1] == ')':
        count += len(stack)
        continue
    elif pipe[i] == '(':
        stack.append(pipe[i])
        count += 1
    elif pipe[i] == ')':
        if pipe[i - 1] == '(':
            continue 
        stack.pop()

print(count)