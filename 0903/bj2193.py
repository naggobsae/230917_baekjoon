n = int(input())

lst = [[0 for _ in range(2)] for i in range(n + 1)]
lst[1] = [0, 1]

for i in range(2, n + 1):
    lst[i][0] = lst[i - 1][0] + lst[i - 1][1]
    lst[i][1] = lst[i - 1][0]

print(sum(lst[n]))