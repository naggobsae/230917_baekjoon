import sys

while True:
    string = sys.stdin.readline().rstrip()
    stack = []
    flag = True
    if string == '.':
        break
    else:
        for i in range(len(string)):
            if string[i] == '(':
                stack.append('(')
            elif string[i] == '[':
                stack.append('[')
            elif string[i] == ')':
                if '(' not in stack:
                    flag = False
                    break
                else:
                    res = stack.pop()
                    if res != '(':
                        flag = False
                        break
            elif string[i] == ']':
                if '[' not in stack:
                    flag = False
                    break
                else:
                    res = stack.pop()
                    if res != '[':
                        flag = False
                        break
            else:
                continue
    print(stack)
    print(flag)
    if not stack and flag:
        print("yes")
    else:
        print("no")