import sys

string = sys.stdin.readline().rstrip()

dic = {}


for i in range(1, len(string) + 1):
    temp = 0
    while temp + i <= len(string):
        dic[string[temp:temp+i]] = 0
        temp += 1

count = 0
for i in dic:
    count += 1

print(count)