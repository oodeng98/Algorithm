import sys

sys.stdin = open('input.txt')

from collections import deque
direction = {
    1: (1, -1), 
    2: (1, 1), 
    3: (-1, 1), 
    4: (-1, -1), 
}

def dfs(x, y, d, visit):
    # 가장 위의 점을 기준으로 진행할 것
    # 시계 방향으로 점을 계속 이동시키는데, 만약 조건에 부합하지 않는다면 방향을 꺾을 것
    # print(x, y, d, visit)
    a, b = x + direction[d][0], y + direction[d][1]  # 기존 진행 방향대로 한칸 이동
    if (a, b, d) == (i, j, 4):
        global max_value
        max_value = max(max_value, len(visit))
        return
    if 0 <= a < N and 0 <= b < N:  # 진행 방향을 유지할 것이냐
        if arr[a][b] not in visit:
            visit.add(arr[a][b])
            dfs(a, b, d, visit)
            visit.remove(arr[a][b])
        # 꺾을 것이냐
            if d + 1 <= 4:
                visit.add(arr[a][b])
                dfs(a, b, d+1, visit)
                visit.remove(arr[a][b])


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [input().split() for _ in range(N)]
    max_value = 0
    for i in range(N - 2):  # 맨 아래 줄과 그 위의 줄은 할 필요가 없다
        for j in range(1, N - 1):  # 맨 왼쪽 줄과 맨 오른쪽 줄은 할 필요가 없다
            dfs(i, j, 1, {arr[i][j]})
            # print(max_value, 'max')
            # break
    if max_value == 0:
        max_value -= 1
    print(f"#{t} {max_value}")
    # break