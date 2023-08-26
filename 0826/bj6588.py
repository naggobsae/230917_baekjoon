# 풀이 1: pypy에선 ok but python은 시간초과
# import sys

# prime_list = [True for i in range(1000001)] # 에라토스테네스의 체
# for i in range(2, 1001):
#     if i != 2 and i % 2 == 0:
#         continue
#     else:
#         j = 2
#         while i * j <= 1000000:
#             prime_list[i * j] = False
#             j += 1


# while True:
#     n = int(sys.stdin.readline())
#     if n == 0:
#         break
#     for i in range(2, n):
#         if prime_list[i] == True and prime_list[n - i] == True:
#             print("{0} = {1} + {2}".format(n, i, n - i))
#             break
#         else:
#             if i == n - 1:
#                 print("Goldbach's conjecture is wrong")
#             else:
#                 continue

import sys

prime_list = [True for i in range(1000001)]
for i in range(2, 1001):
    if i != 2 and i % 2 == 0:
        continue
    else:
        j = 2
        while i * j <= 1000000:
            prime_list[i * j] = False
            j += 1


while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    for i in range(3, int(n / 2) + 1, 2): # 반복 횟수를 감소
        if prime_list[i] == True and prime_list[n - i] == True:
            print("{0} = {1} + {2}".format(n, i, n - i))
            break
        else:
            if i == n - 1:
                print("Goldbach's conjecture is wrong")
            else:
                continue