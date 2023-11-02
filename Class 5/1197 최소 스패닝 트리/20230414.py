import sys
import heapq


input = sys.stdin.readline
v, e = map(int, input().split())
queue = []
for _ in range(e):
    a, b, c = map(int, input().split())
    heapq.heappush(queue, [c, a, b])
while queue:
    print(heapq.heappop(queue))
