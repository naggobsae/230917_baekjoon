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
                    if res != '(': # ([(]]) 같은 반례를 걸러주기 위함
                        flag = False
                        break
            elif string[i] == ']':
                if '[' not in stack:
                    flag = False
                    break
                else:
                    res = stack.pop()
                    if res != '[': # ([(]]) 같은 반례를 걸러주기 위함
                        flag = False
                        break
            else:
                continue
    if not stack and flag:
        print("yes")
    else:
        print("no")