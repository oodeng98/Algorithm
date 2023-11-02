import sys
import heapq


input = sys.stdin.readline
v, e = map(int, input().split())
queue = []
for _ in range(e):
    a, b, c = map(int, input().split())
    heapq.heappush(queue, [c, a, b])

check = [i for i in range(v + 1)]
while queue:
    temp = heapq.heappop(queue)
    if check[temp[1]] == temp[1] and check[temp[2]] == temp[2]:  # 두개의 노드가 어느 그룹에도 속해있지 않은 경우
        mini = min(temp[1], temp[2])
        check[temp[1]] = mini
        check[temp[2]] = mini
    elif check[temp[2]] == temp[2]:  # temp[1]만 그룹에 속해있는 경우
        check[temp[2]] = check[temp[1]]
    elif check[temp[1]] == temp[1]:  # temp[2]만 그룹에 속해있는 경우
        check[temp[1]] = check[temp[2]]



