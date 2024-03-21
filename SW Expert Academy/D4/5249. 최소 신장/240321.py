import sys


def find_parent(n):
    child = n
    while child != parents[child]:
        child = parents[child]
    return child


def union(x, y):
    x = find_parent(x)
    y = find_parent(y)
    if x == y:
        return
    parents[min(x, y)] = max(x, y)

def kruskal():
    count = 0
    total = 0
    for s, e, w in edges:
        if find_parent(s) != find_parent(e):
            count += 1
            union(s, e)
            total += w
            if count == V:
                break
    return total


sys.stdin = open('input.txt')
T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    edges = []
    for _ in range(E):
        edges.append(tuple(map(int, input().split())))
    edges.sort(key=lambda x: x[2])
    parents = [i for i in range(V+1)]
    print(f"#{t} {kruskal()}")