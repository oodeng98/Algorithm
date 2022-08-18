import sys

INF = 3000000
# input 받기
input = sys.stdin.readline
v, e = map(int, input().split())
start_node = int(input())
graph = {}
for i in range(e):
    a, b, c = map(int, input().split())
    if a in graph:
        if b in graph[a]:
            graph[a][b] = min(graph[a][b], c)
        else:
            graph[a][b] = c
    else:
        graph[a] = {b: c}

# checked dict 설정
unchecked = {}
for i in range(1, v + 1):
    unchecked[i] = 0

# 노드별 최단 경로 dict인 arr 설정
arr = {}
for i in range(1, v + 1):
    if i == start_node:
        arr[i] = 0
        continue
    arr[i] = INF

while unchecked:
    min_node = 0
    min_price = INF

    rm_list = []
    for i in unchecked:
        if arr[i] < min_price:
            if i not in graph:
                rm_list.append(i)
                continue
            min_node = i
            min_price = arr[i]

    for i in rm_list:
        del unchecked[i]
    if min_node == 0:
        break

    for i in graph[min_node]:
        arr[i] = min(arr[i], arr[min_node] + graph[min_node][i])
    del unchecked[min_node]

for i in range(1, v + 1):
    if arr[i] == INF:
        print('INF')
        continue
    print(arr[i])

