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
        if b in graph:
            graph[a][b] = min(graph[a][b], c)
        else:
            graph[a][b] = c
    else:
        graph[a] = {b: c}
# print(graph)

# checked dict 설정
checked = {'check': {}, 'uncheck': {}}
for i in range(1, v + 1):
    checked['uncheck'][i] = 0

# 노드별 최단 경로 dict인 arr 설정
arr = {}
for i in range(1, v + 1):
    if i == start_node:
        arr[i] = 0
        continue
    arr[i] = INF

while len(checked['check']) < v:
    min_node = 0
    min_price = INF
    for i in range(1, v + 1):
        if i in checked['uncheck'] and arr[i] < min_price:
            min_node = i
            min_price = arr[i]
    if min_node in graph:
        for i in graph[min_node]:
            arr[i] = min(arr[i], arr[min_node] + graph[min_node][i])
    if min_node == 0:
        break
    del checked['uncheck'][min_node]
    checked['check'][min_node] = 0

for i in range(1, v + 1):
    if arr[i] == INF:
        print('INF')
        continue
    print(arr[i])

