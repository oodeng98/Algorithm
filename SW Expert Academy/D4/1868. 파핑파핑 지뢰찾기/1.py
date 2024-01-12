def zeroDetection(x, y):
    if visitTable[x][y] == 0:
        return 0

    noneBombTile = []
    bombCount = 0
    for a in range(-1, 2):
        for b in range(-1, 2):
            if a == 0 and b == 0:
                continue
            if (0 <= x + a < N) and (0 <= y + b < N):
                if table[x + a][y + b] == '.':
                    if visitTable[x + a][y + b] == 1:
                        noneBombTile.append((x + a, y + b))
                else:
                    bombCount += 1

    if bombCount == 0:
        visitTable[x][y] = 0
        for a, b in noneBombTile:
            zeroDetection(a, b)
            visitTable[a][b] = 0
        return 1
    return 0


T = int(input())
for t in range(T):
    N = int(input())
    table = []
    for _ in range(N):
        table.append(input())
    visitTable = [[1 for _ in range(N)] for _ in range(N)]
    
    totalBombCount = 0
    totalZeroareaCount = 0
    for i in range(N):
        for j in range(N):
            if table[i][j] == "*":
                totalBombCount += 1
                continue

            totalZeroareaCount += zeroDetection(i, j)

    nearBomb = 0
    for i in visitTable:
        nearBomb += sum(i)

    print(f"#{t+1} {nearBomb + totalZeroareaCount - totalBombCount}")