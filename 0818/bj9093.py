import sys

n = int(sys.stdin.readline())

for i in range(n):
    str_list = list(sys.stdin.readline().split())
    for j in range(len(str_list) - 1):
        print(str_list[j][::-1], end = ' ')
    print(str_list[-1][::-1])