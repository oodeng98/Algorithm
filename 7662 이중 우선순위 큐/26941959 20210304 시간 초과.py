import sys
import collections


input = sys.stdin.readline
n = int(input())
for i in range(n):
    num = int(input())
    queue = collections.deque([])
    for j in range(num):
        order, data = input().split()
        if order == 'D':
            if not queue:
                continue
            if data == '-1':
                queue.pop()
            else:
                queue.popleft()
        else:
            if not queue:
                queue.append(int(data))
            else:
                check = 0
                for k in range(len(queue)):
                    if queue[k] < int(data):
                        queue.insert(k, int(data))
                        check = 1
                        break
                if check == 0:
                    queue.append(int(data))
    if not queue:
        print('EMPTY')
    else:
        print(queue[0], queue[-1])