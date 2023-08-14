import sys

a, b = map(int, sys.stdin.readline().split())

a_list = list(map(int, sys.stdin.readline().split()))
b_list = list(map(int, sys.stdin.readline().split()))

dic1 = {}
dic2 = {}

for i in a_list:
    dic1[i] = 0

for i in b_list:
    dic2[i] = 0
    if i in dic1:
        dic1[i] = 1

for i in a_list:
    if i in dic2:
        dic2[i] = 1

count = 0

for i in dic1:
    if dic1[i] == 0:
        count += 1
for i in dic2:
    if dic2[i] == 0:
        count += 1
        
print(count)