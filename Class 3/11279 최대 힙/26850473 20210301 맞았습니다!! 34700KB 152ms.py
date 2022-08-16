import sys
import heapq


input = sys.stdin.readline
num = int(input())
heap = []
for i in range(num):
    temp = int(input())
    if temp != 0:
        heapq.heappush(heap, -temp)
    else:
        if not heap:
            print(0)
            continue
        print(-heapq.heappop(heap))