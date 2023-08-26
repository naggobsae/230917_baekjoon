import sys

def priority(sign):
    if sign == '*' or sign == '/':
        return 1
    else:
        return 0

equation = sys.stdin.readline().rstrip()
stack = []

for i in equation:
    if i.isupper():
        print(i, end='')
    else:
        if not stack:
            stack.append(i)
        else:
            if i == '(':
                stack.append(i)
            elif i == ')':
                while True:
                    temp = stack.pop()
                    if temp == '(':
                        break
                    else:
                        print(temp, end='')
            else:
                if stack[-1] != '(':
                    while stack and stack[-1] != '(' and priority(i) <= priority(stack[-1]):
                        print(stack.pop(), end='')
                stack.append(i)

while stack:
    print(stack.pop(), end='')

