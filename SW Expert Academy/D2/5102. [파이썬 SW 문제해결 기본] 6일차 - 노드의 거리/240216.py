import sys

sys.stdin = open('input.txt')


def dfs():
    queue = [start]
    visit = [0 for _ in range(v+1)]
    visit[start] = 0
    while queue:
        new_queue = []
        for node in queue:
            for j in graph[node]:
                if visit[j] == 0:
                    if des == j:
                        return 1 + visit[node]
                    new_queue.append(j)
                    visit[j] += 1 + visit[node]
        queue = new_queue
    return 0

T = int(input())
for t in range(1, T+1):
    v, e = map(int, input().split())
    graph = {i : [] for i in range(1, v+1)}
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    start, des = map(int, input().split())
    print(f"#{t} {dfs()}")