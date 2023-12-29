import sys

INF = 3000000

input = sys.stdin.readline
v, e = map(int, input().split())
start_node = int(input())
graph = {}
for i in range(e):
    a, b, c = map(int, input().split())
    if a in graph:
        graph[a][b] = c
    else:
        graph[a] = {b: c}

checked = [start_node]

arr = {}
for i in range(1, v + 1):
    if i == start_node:
        arr[i] = 0
        continue
    arr[i] = INF

for i in graph[start_node]:
    arr[i] = min(arr[i], graph[start_node][i])

while len(checked) < v:
    min_node = 0
    min_price = INF + 1
    for i in range(1, v + 1):
        if i not in checked and arr[i] < min_price:
            min_node = i
            min_price = arr[i]
    if min_node in graph:
        for i in graph[min_node]:
            arr[i] = min(arr[i], arr[min_node] + graph[min_node][i])
    checked.append(min_node)

for i in arr:
    if arr[i] == INF:
        print('INF')
        continue
    print(arr[i])



