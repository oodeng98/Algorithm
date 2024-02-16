import sys

sys.stdin = open('input.txt')


def dfs():
    queue = [start]
    visit = {start: ''}
    while queue:
        new_queue = []
        for node in queue:
            if node not in graph:
                continue
            for j in graph[node]:
                if j not in visit:
                    visit[j] = ''
                    new_queue.append(j)
        if not new_queue:
            max_value = -float('inf')
            for i in queue:
                if max_value < i:
                    max_value = i
        queue = new_queue
    return max_value


for t in range(1, 11):
    N, start = map(int, input().split())
    data = list(map(int, input().split()))
    graph = {}
    for i in range(N // 2):
        a, b = data[2*i], data[2*i+1]
        if a in graph:
            graph[a].append(b)
        else:
            graph[a] = [b]
    print(f"#{t} {dfs()}")
    