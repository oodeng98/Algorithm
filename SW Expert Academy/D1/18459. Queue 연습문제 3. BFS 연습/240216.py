import sys

sys.stdin = open('input.txt')


v, e = map(int, input().split())
graph = {i: [] for i in range(1, e+1)}
edges = list(map(int, input().split()))
for i in range(e):
    a, b = edges[2*i], edges[2*i+1]
    graph[a].append(b)

print(f"#{1}", end=' ')
queue = [1]
visit = [0 for i in range(e+1)]
while queue:
    new_queue = []
    for i in queue:
        print(i, end=' ')
        for j in graph[i]:
            if visit[j] == 1:
                continue
            else:
                visit[j] = 1
                new_queue.append(j)
    queue = new_queue