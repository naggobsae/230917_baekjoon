n = int(input())
lst = []

for i in range(n):
    lst.append(input())

lst = list(set(lst))

lst.sort(key = lambda x : (len(x), x))

for i in lst:
    print(i)