import sys
from collections import deque


def delta(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        if 0 <= x + dx[i] < N and 0 <= y + dy[i] < N:
            yield x + dx[i], y + dy[i]


input = sys.stdin.readline

N, L, R = map(int, input().split())
population = [list(map(int, input().split())) for _ in range(N)]
count = -1
flag = 1
while flag:
    count += 1
    visit = [[0 for _ in range(N)] for _ in range(N)]
    flag = 0
    for i in range(N):
        for j in range(N):
            if visit[i][j]:
                continue
            visit[i][j] = 1
            countries = set([(i, j)])
            total = population[i][j]
            queue = deque([(i, j)])
            while queue:
                x, y = queue.popleft()
                for a, b in delta(x, y):
                    if visit[a][b]:
                        continue
                    if L <= abs(population[x][y] - population[a][b]) <= R:
                        queue.append((a, b))
                        visit[a][b] = 1
                        countries.add((a, b))
                        total += population[a][b]

            if 1 < len(countries):
                flag = 1
            for country in countries:
                a, b = country
                population[a][b] = total // len(countries)
print(count)