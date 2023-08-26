import sys

n = int(sys.stdin.readline())
num_list = []
stack = []
ans = []
flag = True

for i in range(n):
    num = int(sys.stdin.readline().strip())
    num_list.append(num)

num = 1
for j in num_list:
    while not stack or j >= num:
        stack.append(num)
        ans.append('+')
        num += 1
    n = stack.pop()
    if j == n:
        ans.append('-')
    else:
        flag = False
        break

if flag == False:
    print("NO")
else:
    for i in ans:
        print(i)