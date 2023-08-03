import sys

n = int(sys.stdin.readline())
lst = list(map(int, str(n)))

lst.sort(reverse=True)

for i in lst:
    print(i, end = "")

