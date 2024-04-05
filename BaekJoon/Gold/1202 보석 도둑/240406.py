import sys
from heapq import heappush, heappop


input = sys.stdin.readline
N, K = map(int, input().split())
jewels = sorted([list(map(int, input().split())) for _ in range(N)])  # weight, value
bags = sorted([int(input()) for _ in range(K)])

result = 0
heap = []
index = 0
for bag in bags:
    while index < N and jewels[index][0] <= bag:
        heappush(heap, -jewels[index][1])
        index += 1
    if heap:
        result += heappop(heap)
print(-result)