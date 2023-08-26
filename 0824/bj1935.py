import sys

n = int(sys.stdin.readline())
equation = sys.stdin.readline().rstrip()
nums = []
stack = []
dic = {}


for i in range(n):
    nums.append(int(sys.stdin.readline()))

nums.reverse()

for i in equation:
    if i in dic:
        continue
    elif i.isupper():
        dic[i] = nums.pop()

for i in equation:
    if i.isupper():
        stack.append(dic[i])
    else:
        num1 = stack.pop()
        num2 = stack.pop()
        if i == '+':
            stack.append(num2 + num1)
        elif i == '-':
            stack.append(num2 - num1)
        elif i == '*':
            stack.append(num2 * num1)
        else:
            stack.append(num2 / num1)

print("{:.2f}".format(stack[0]))