import sys
from heapq import heappop, heappush


def d(x1, y1, x2, y2):
    return (x2 - x1) ** 2 + (y2 - y1) ** 2


def find_parent(n):
    while n != parent[n]:
        n = parent[n]
    return n


def union(x, y):
    x = find_parent(x)
    y = find_parent(y)
    if x == y:
        return
    parent[min(x, y)] = max(x, y)


def kruskal():
    count = 0
    total = 0
    while edges:
        w, s, e = heappop(edges)
        if find_parent(s) != find_parent(e):
            count += 1
            union(s, e)
            total += w
            if count == N-1:
                break
    return total


sys.stdin = open('input.txt')
T = int(input())
for t in range(1, T+1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())
    parent = [i for i in range(N+1)]
    edges = []
    for i in range(N):
        for j in range(i+1, N):
            heappush(edges, (d(X[i], Y[i], X[j], Y[j]), i, j))
    print(f"#{t} {round(kruskal()*E)}")