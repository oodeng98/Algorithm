import sys


input = sys.stdin.readline
n, m = map(int, input().split())
paper = []
for _ in range(n):
    paper.append(list(map(int, input().split())))

start = {(0, 0), (0, m - 1), (n - 1, 0), (n - 1, m - 1)}
for i, j in start:
    paper[i][j] = 2
time = 0
while True:
    air = set()
    while start:
        new_start = set()
        for x, y in start:
            for a, b in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= a < n and 0 <= b < m:
                    if not paper[a][b]:
                        new_start.add((a, b))
                        paper[a][b] = 2
                    if paper[a][b] == 1:
                        air.add((a, b))
        start = new_start

    if not air:
        print(time)
        break
    time += 1

    start = set()
    for x, y in air:
        count = 0
        for a, b in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if paper[a][b] == 2:
                count += 1
                if count == 2:
                    start.add((x, y))
                    break
    for x, y in start:
        paper[x][y] = 2
