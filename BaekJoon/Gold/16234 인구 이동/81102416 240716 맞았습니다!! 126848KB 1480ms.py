import sys


def delta(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        a, b = x + dx[i], y + dy[i]
        if 0 <= a < N and 0 <= b < N and visit[a][b] != 1:
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
            countries = set()
            total = population[i][j]
            stack = [(i, j)]
            while stack:
                x, y = stack.pop()
                countries.add((x, y))
                for a, b in delta(x, y):
                    if L <= abs(population[x][y] - population[a][b]) <= R:
                        stack.append((a, b))
                        visit[a][b] = 1
                        total += population[a][b]

            if 1 < len(countries):
                flag = 1
            for a, b in countries:
                population[a][b] = total // len(countries)
print(count)