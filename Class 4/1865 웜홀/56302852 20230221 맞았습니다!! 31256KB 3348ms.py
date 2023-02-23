import sys


def circuit():
    for _ in range(n - 1):
        for node in edge:
            for neighbor in edge[node]:
                cost[neighbor] = min(cost[node] + edge[node][neighbor], cost[neighbor])

    for node in edge:
        for neighbor in edge[node]:
            if cost[neighbor] > cost[node] + edge[node][neighbor]:
                print('YES')
                return
    print('NO')


# input part
input = sys.stdin.readline
tc = int(input())
for case in range(tc):
    n, m, w = map(int, input().split())
    edge = {}

    for _ in range(m):
        s, e, t = map(int, input().split())
        if s in edge:
            if e in edge[s]:
                edge[s][e] = min(edge[s][e], t)
            else:
                edge[s][e] = t
        else:
            edge[s] = {e: t}
        if e in edge:
            if s in edge[e]:
                edge[e][s] = min(edge[e][s], t)
            else:
                edge[e][s] = t
        else:
            edge[e] = {s: t}

    for _ in range(w):
        s, e, t = map(int, input().split())
        if s in edge:
            if e in edge[s]:
                edge[s][e] = min(edge[s][e], -t)
            else:
                edge[s][e] = -t
        else:
            edge[s] = {e: -t}

    cost = [10001 for _ in range(n + 1)]
    start = 1
    cost[start] = 0

    circuit()
