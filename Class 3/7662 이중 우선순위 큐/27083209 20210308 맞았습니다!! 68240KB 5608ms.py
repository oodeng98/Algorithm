import sys
import heapq


input = sys.stdin.readline
n = int(input())
for i in range(n):
    num = int(input())
    min_heap = []
    max_heap = []
    dic = {}
    for j in range(num):
        order, data = input().split()
        data = int(data)
        if order == 'D':
            if data == -1:
                while min_heap:
                    temp = heapq.heappop(min_heap)
                    if dic[temp] != 0:
                        dic[temp] -= 1
                        break
            else:
                while max_heap:
                    temp = heapq.heappop(max_heap)
                    if dic[-temp] != 0:
                        dic[-temp] -= 1
                        break
        else:
            heapq.heappush(min_heap, data)
            heapq.heappush(max_heap, -data)
            dic[data] = dic.setdefault(data, 0) + 1
    empty = 0
    for j in dic:
        if dic[j] != 0:
            empty = 1
            break
    if empty == 0:
        print('EMPTY')
    else:
        while dic[-max_heap[0]] == 0:
            heapq.heappop(max_heap)
        while dic[min_heap[0]] == 0:
            heapq.heappop(min_heap)
        print(-max_heap[0], min_heap[0])
