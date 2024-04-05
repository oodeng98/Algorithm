import sys
from heapq import heappush, heappop


input = sys.stdin.readline
N, K = map(int, input().split())
jewels = dict()
for _ in range(N):  # 반복문 N번을 도는 것은 동일하지만, list comprehesion에 비해 느릴 수도 있음
    weight, value = map(int, input().split())
    if weight in jewels:
        jewels[weight].append(value)
    else:
        jewels[weight] = [value]
jewels_weight = sorted(jewels.keys(), reverse=True)  # 가방의 개수를 줄였으므로 여기서 nlogn의 시간복잡도가 조금 줄었을 수 있음
        
bags = sorted([int(input()) for _ in range(K)])

result = 0
heap = []
for bag in bags:
    while jewels_weight and jewels_weight[-1] <= bag:  # 어차피 도는 반복문의 횟수는 똑같음
        weight = jewels_weight.pop()
        for value in jewels[weight]:  # 앞서 아낀 부분도 여기서 추가로 돌기 때문
            heappush(heap, -value)
    if heap:
        result += heappop(heap)
print(-result)
# 그런데 왜 시간이 훨씬 빠른가..?