import sys
import heapq


input = sys.stdin.readline
num = int(input())
heap = []
for i in range(num):
    temp = int(input())
    if temp == 0:
        if len(heap) != 0:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (abs(temp), temp))