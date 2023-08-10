# n = int(input())
# windows = [0] * (n + 1)
# count = 0

# for i in range(1, n + 1):
#     j = 1
#     while i * j <= n:
#         if windows[i*j] == 0:
#             windows[i*j] = 1
#         else:
#             windows[i*j] = 0
#         j += 1

# for i in range(len(windows)):
#     if windows[i] == 1:
#         count += 1

# print(windows)

# 위의 코드를 16까지 돌려서 windows의 규칙을 찾아내자!
n = int(input())
count = 1
temp = 3
ex = 1
while True:
    ex += temp
    if ex > n:
        break
    temp += 2
    count += 1

print(count)
    

