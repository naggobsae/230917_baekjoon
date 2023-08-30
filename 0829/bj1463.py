# 풀이 1 : 그리디 알고리즘이 통하지 않는 문제라 틀림
# num = int(input())
# count = 0

# while num != 1:
#     if num % 3 == 0:
#         num //= 3
#         count += 1
#         continue
#     elif num % 2 == 0:
#         num //= 2
#         count += 1
#         continue
#     else:
#         num -= 1
#         count += 1

# print(count)

# 풀이 2: 다이나믹 프로그래밍(DP)을 써야함

num = int(input())

count = [0] * (num + 1)

for i in range(2, len(count)):
    count[i] = count[i - 1] + 1
    if i % 2 == 0:
        count[i] = min(count[i], count[i//2] + 1)
    if i % 3 == 0:
        count[i] = min(count[i], count[i//3] + 1)

print(count[num])