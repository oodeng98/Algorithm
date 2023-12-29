import sys
from collections import deque

n, m = map(int, input().split())

l = []
for _ in range(n):
    l.append(sys.stdin.readline())

visited = [[2] * m for _ in range(n)]  # 2 방문 안함, 0이면 방문, 1이면 벽을 하나 뚫고옴
visited[0][0] = 0

res = 0
queue = deque([[0, 0]])

can = False

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while queue:
    if can:
        break

    res += 1
    for _ in range(len(queue)):
        x, y = queue.popleft()

        if x == n - 1 and y == m - 1:
            print(res)
            can = True
            break

        for i in range(4):
            nx, my = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= my < m:
                if l[nx][my] == '0' and visited[nx][my] > visited[x][y]:  # 0인 지역 중 방문하지 않은 지역을 갈 때
                    visited[nx][my] = visited[x][y]  # visited 계승
                    queue.append([nx, my])
                elif l[nx][my] == '1' and not visited[x][y]:  # 벽을 뚫을 때
                    visited[nx][my] = visited[x][y] + 1  # 무조건 1의 값을 가진다, visited[x][y] == 0인 상태니까
                    queue.append([nx, my])
                print(visited)
# 방문하지 않은 지역은 방문하지 않은 지역대로 가고, 벽을 뚫은 경우는 벽을 뚫은 경우대로 가게 된다
# 벽을 뚫지 않은 경우가 더 빠르게 일부 지역에 도착하게 된다면, 벽을 뚫지 않은 경우의 값을 계승하게 되므로 또 벽을 뚫을 수 있게 된다
if not can:
    print(-1)
