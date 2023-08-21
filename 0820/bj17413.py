import sys
import collections

str_list = list(sys.stdin.readline().strip())

dequeue = collections.deque()
flag = True

for i in range(len(str_list)):
    if str_list[i] == '<':
        flag = False
        while dequeue:
            n = dequeue.pop()
            print(n, end='')
        dequeue.append(str_list[i])
    elif str_list[i] == '>':
        flag = True
        dequeue.append(str_list[i])
        while dequeue:
            n = dequeue.popleft()
            print(n, end='')
    elif str_list[i] == ' ':
        if not flag:
            while dequeue:
                n = dequeue.popleft()
                print(n, end='')
            print(' ', end='')
        else:
            while dequeue:
                n = dequeue.pop()
                print(n, end='')
            print(' ', end='')
    else:
        dequeue.append(str_list[i])

while dequeue:
    n = dequeue.pop()
    print(n, end='')
    
        