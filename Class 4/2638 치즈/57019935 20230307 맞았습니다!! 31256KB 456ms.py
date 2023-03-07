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
    while start:
        new_start = set()
        for x, y in start:
            for a, b in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= a < n and 0 <= b < m:
                    if not paper[a][b]:
                        new_start.add((a, b))
                        paper[a][b] = 2
        start = new_start

    check = 0
    for i in paper:
        for j in i:
            if j == 1:
                check = 1
                break
        if check:
            break
    if not check:
        print(time)
        break
    time += 1

    start = set()
    for i in range(n):
        for j in range(m):
            if paper[i][j] == 1:
                count = 0
                for a, b in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                    if paper[a][b] == 2:
                        count += 1
                        if count > 1:
                            paper[i][j] = 0
                            start.add((a, b))
                            break
