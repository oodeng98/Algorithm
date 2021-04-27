import sys


input = sys.stdin.readline
n = int(input())
data = {}
for i in range(n - 1):
    a, b = map(int, input().split())
    a, b = min(a, b), max(a, b)
    if a in data:
        data[a].append(b)
    else:
        data[a] = [b]
    if b in data:
        data[b].append(a)
    else:
        data[b] = [a]
tree = {1: data[1]}
find_parent = {}
for i in data[1]:
    find_parent[i] = 1
start = [1]
while True:
    if len(tree) == n:
        break
    new_start = []
    for i in start:
        for j in data[i]:
            temp = data[j]
            temp.remove(i)
            tree[j] = temp
            for k in temp:
                find_parent[k] = j
            new_start.append(j)
    start = new_start
for i in range(2, n + 1):
    print(find_parent[i])
"""
7
6 3
3 5
4 1
2 4
4 7
1 6
"""
