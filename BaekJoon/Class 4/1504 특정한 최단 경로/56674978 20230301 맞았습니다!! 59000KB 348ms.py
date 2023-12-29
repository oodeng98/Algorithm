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
n, e = map(int, input().split())
graph = {}
for i in range(1, n + 1):
    graph[i] = {}
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c
via1, via2 = map(int, input().split())

from_start = search(graph, 1)
from_via1 = search(graph, via1)
from_via2 = search(graph, via2)

ret1 = from_start[via1] + from_via1[via2] + from_via2[n]
ret2 = from_start[via2] + from_via2[via1] + from_via1[n]

if ret1 == float('inf') and ret2 == float('inf'):
    print(-1)
else:
    print(min(ret1, ret2))
