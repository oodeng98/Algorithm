import sys
from heapq import heappush, heappop


def dijkstra():
    heap = []
    heappush(heap, 0)
    distance[0] = 0
    while heap:
        now = heappop(heap)
        if now not in graph:
            continue
        for next_node in graph[now]:
            new_dist = distance[now] + graph[now][next_node]
            if distance[next_node] <= new_dist:
                continue
            distance[next_node] = new_dist
            heappush(heap, next_node)


sys.stdin = open('input.txt')
T = int(input())
for t in range(1, T+1):
    N, E = map(int, input().split())
    graph = {}
    for _ in range(E):
        s, e, w = map(int, input().split())
        if s in graph:
            graph[s][e] = w
        else:
            graph[s] = {e: w}
    distance = [float('inf') for _ in range(N+1)]
    dijkstra()
    print(f"#{t} {distance[N]}")