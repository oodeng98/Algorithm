import sys
import heapq


def search(graph, start):
    distances = {i: [float('inf'), 0] for i in range(1, n + 1)}
    distances[start] = [0, 0]
    queue = []
    heapq.heappush(queue, [distances[start][0], start])

    while queue:
        current_distance, current_destination = heapq.heappop(queue)

        if distances[current_destination][0] < current_distance:
            continue

        if current_destination in graph:
            for new_destination, new_distance in graph[current_destination].items():
                distance = current_distance + new_distance
                if distance < distances[new_destination][0]:
                    distances[new_destination] = [distance, current_destination]
                    heapq.heappush(queue, [distance, new_destination])

    print(distances[des][0])
    ret = [str(des)]
    via = distances[des][1]
    while via != 0:
        ret.append(str(via))
        via = distances[via][1]

    print(len(ret))
    ret = reversed(ret)
    print(' '.join(ret))
    return distances


input = sys.stdin.readline
n = int(input())
m = int(input())
graph = {}
for _ in range(m):
    a, b, c = map(int, input().split())
    if a in graph:
        if b in graph[a]:
            graph[a][b] = min(graph[a][b], c)
        else:
            graph[a][b] = c
    else:
        graph[a] = {b: c}
start, des = map(int, input().split())
search(graph, start)

