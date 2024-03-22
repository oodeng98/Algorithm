import sys
from heapq import heappush, heappop


def dijkstra(start, end):
    heap = []
    heappush(heap, (0, start))
    distance = [float('inf') for _ in range(N+1)]
    distance[start] = 0
    while heap:
        weight, now = heappop(heap)
        if now not in graph:
            continue
        if distance[now] < weight:
            continue
        for next_node in graph[now]:
            new_dist = weight + graph[now][next_node]
            if distance[next_node] <= new_dist:
                continue
            distance[next_node] = new_dist
            heappush(heap, (distance[next_node], next_node))
    return distance[end]


sys.stdin = open('input.txt')
T = int(input())
for t in range(1, T+1):
    N, M, X = map(int, input().split())
    graph = {}
    for _ in range(M):
        x, y, c = map(int, input().split())
        if x in graph:
            graph[x][y] = c
        else:
            graph[x] = {y: c}
    
    result = 0
    for node in range(1, N+1):
        if node == X:
            continue
        result = max(result, dijkstra(X, node) + dijkstra(node, X))
    print(f"#{t} {result}")