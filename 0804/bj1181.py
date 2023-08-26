n = int(input())
lst = []

for i in range(n):
    lst.append(input())

lst = list(set(lst)) # 중복 제거

lst.sort(key = lambda x : (len(x), x)) # 1순위 길이 2순위 사전식 순서로 정렬

for i in lst:
    print(i)