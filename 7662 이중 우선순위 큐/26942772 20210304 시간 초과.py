import sys
import collections
import bisect


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
                queue.popleft()
            else:
                queue.pop()
        else:
            if not queue:
                queue.appendleft(int(data))
            else:
                bisect.insort(queue, int(data))
    if not queue:
        print('EMPTY')
    else:
        print(queue[-1], queue[0])