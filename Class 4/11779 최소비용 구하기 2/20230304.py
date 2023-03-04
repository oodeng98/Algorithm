import sys
import heapq


def search(graph, start):
    distances = {i: float('inf') for i in range(1, n + 1)}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_destination = heapq.heappop(queue)

        if distances[current_destination] < current_distance:
            continue

        for new_destination, new_distance in graph[current_destination].items():
            distance = current_distance + new_distance
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])
    return distances


input = sys.stdin.readline
n = int(input())
m = int(input())
graph = {}
for _ in range(m):
    a, b, c = map(int, input().split())
    if a in graph:
        if b in graph:
            graph[a][b] = min(graph[a][b], c)
        else:
            graph[a][b] = c
    else:
        graph[a] = {b: c}
start, des = map(int, input())
search(graph, start)