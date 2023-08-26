import sys

string = sys.stdin.readline().rstrip()
res = []

for i in range(len(string)):
    res.append(string[i:])

res.sort()

for i in res:
    print(i)