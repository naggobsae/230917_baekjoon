import sys
input = sys.stdin.readline

aim = int(input())
n = int(input())

if n == 0:
    print(min(len(str(aim)), abs(aim - 100)))
    exit()

button = list(map(int, input().split()))

if aim == 100:
    print(0)
    exit()

if n == 10:
    print(abs(aim - 100))
    exit()

min_value = abs(aim - 100)
for i in range(1000001): # 500001이 아닌 이유는 채널의 개수가 무한이기 때문!
    for j in range(len(str(i))):
        if int(str(i)[j]) in button:
            break
        elif j == len(str(i)) - 1:
            min_value = min(min_value, abs(aim - i) + len(str(i)))


print(min_value)