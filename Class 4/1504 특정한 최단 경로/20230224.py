import sys


def search1():
    visit = [1]
    while True:
        min_value = graph[0][1]
        min_index = graph[0][1]
        for index, cost in enumerate(graph[0]):
            if min_value > cost:
                if index in visit:
                    continue  # 여기 수정해줘야함
                min_value = cost
                min_index = index
        for node in range(1, n):
            graph[1][node] = min(graph[1][node], graph[1][min_index] + graph[min_index][node])
        visit.append(min_index)
        print(graph)
        if len(visit) == n:
            break


input = sys.stdin.readline
n, e = map(int, input().split())
graph = [[-1 for _ in range(n)] for _ in range(n)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a - 1][b - 1] = c
    graph[b - 1][a - 1] = c
for i in range(n):
    graph[i][i] = 0
via1, via2 = map(int, input().split())
search1()
# 1->via1->via2->n 번 정점으로 이동
