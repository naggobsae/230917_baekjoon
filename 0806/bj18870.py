n = int(input())
lst = list(map(int, input().split()))

lst2 = sorted(list(set(lst)))

dic = {}
for i in range(len(lst2)):
    dic[lst2[i]] = i

for i in range(n):
    print(dic[lst[i]], end=' ')
