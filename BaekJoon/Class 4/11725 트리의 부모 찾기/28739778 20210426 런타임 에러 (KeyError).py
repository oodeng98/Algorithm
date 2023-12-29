import sys


input = sys.stdin.readline
n = int(input())
tree = {1: set()}
find_parent = {}
for i in range(n - 1):
    a, b = map(int, input().split())
    if a in tree:
        tree[a].add(b)
        tree[b] = set()
        find_parent[b] = a
    elif b in tree:
        tree[b].add(a)
        tree[a] = set()
        find_parent[a] = b
for i in range(2, n + 1):
    print(find_parent[i])
