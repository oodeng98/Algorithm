import sys
import heapq


input = sys.stdin.readline
n, m, x = map(int, input().split())
go = {}
back = {}
for _ in range(m):
    a, b, c = map(int, input().split())
    if a in go:
        go[a][b] = c
    else:
        go[a] = {b: c}
    if b in back:
        back[b][a] = c
    else:
        back[b] = {a: c}

go_dist = {node: float('inf') for node in range(1, n + 1)}
go_dist[x] = 0
queue = []
heapq.heappush(queue, [go_dist[x], x])
while queue:
    current_distance, current_destination = heapq.heappop(queue)

    if go_dist[current_destination] < current_distance:
        continue
    for new_destination, new_distance in go[current_destination].items():
        distance = current_distance + new_distance
        if distance < go_dist[new_destination]:
            go_dist[new_destination] = distance
            heapq.heappush(queue, [distance, new_destination])

back_dist = {node: float('inf') for node in range(1, n + 1)}
back_dist[x] = 0
queue = []
heapq.heappush(queue, [back_dist[x], x])
while queue:
    current_distance, current_destination = heapq.heappop(queue)

    if back_dist[current_destination] < current_distance:
        continue
    for new_destination, new_distance in back[current_destination].items():
        distance = current_distance + new_distance
        if distance < back_dist[new_destination]:
            back_dist[new_destination] = distance
            heapq.heappush(queue, [distance, new_destination])

ret = 0
for i in range(1, n + 1):
    ret = max(ret, go_dist[i] + back_dist[i])
print(ret)
