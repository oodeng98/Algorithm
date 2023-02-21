import sys


input = sys.stdin.readline
tc = int(input())
for case in range(tc):
    n, m, w = map(int, input().split())
    path = {}
    for i in range(m):
        s, e, t = map(int, input().split())
        if s not in path:
            path[s] = {e: t}
        else:
            if e in path[s]:
                path[s][e] = min(path[s][e], t)
            else:
                path[s][e] = t
    for i in range(w):
        s, e, t = map(int, input().split())
        if s not in path:
            path[s] = {e: -t}
        else:
            if e in path[s]:
                path[s][e] = min(path[s][e], -t)
            else:
                path[s][e] = -t
    result = [[False for _ in range(n + 1)] for _ in range(n + 1)]
    for i in path:
        for j in path[i]:
            result[i][j] = path[i][j]

    candidate = [(x, y) for x in range(1, n + 1) for y in range(1, n + 1)]

    for i in range(1, n + 1):
        pick = []
        for j in candidate:
            if i not in j and j[0] != j[1]:
                pick.append(j)
        for j in pick:
            if not result[j[0]][j[1]]:
                if result[j[0]][i] is not False and result[i][j[1]] is not False:
                    result[j[0]][j[1]] = min(result[j[0]][j[1]], result[j[0]][i] + result[i][j[1]])
            else:
                if result[j[0]][i] is not False and result[i][j[1]] is not False:
                    result[j[0]][j[1]] = result[j[0]][i] + result[i][j[1]]
    check = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if result[i][j] is not False and result[j][i] is not False:
                if result[i][j] + result[j][i] < 0:
                    print('YES')
                    check = 1
                    break
        if check:
            break
    if not check:
        print('NO')

