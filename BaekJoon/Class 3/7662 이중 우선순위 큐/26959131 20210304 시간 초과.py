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
                queue.popleft()  # O(1)
            else:
                queue.pop()  # O(1)
        else:
            if not queue:
                queue.append(int(data))  # O(1)
            else:
                bisect.insort(queue, int(data))  # 어떻게 하면 시간을 더 줄일 수 있지?  # O(log n)
    if not queue:
        print('EMPTY')
    else:
        print(queue[-1], queue[0])