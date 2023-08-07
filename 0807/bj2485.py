n = int(input())
lst = []
dist_lst = []
count = 0

for i in range(n):
    lst.append(int(input()))

for i in range(len(lst) - 1):
    dist = lst[i + 1] - lst[i]
    dist_lst.append(dist)

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

gcd_num = dist_lst[0]
for i in range(len(dist_lst)):
    gcd_num = gcd(gcd_num, dist_lst[i])

for i in dist_lst:
    count += i // gcd_num - 1

print(count)