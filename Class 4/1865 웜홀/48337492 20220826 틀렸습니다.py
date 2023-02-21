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
        if e not in path:
            path[e] = {s: t}
        else:
            if s in path[e]:
                path[e][s] = min(path[e][s], t)
            else:
                path[e][s] = t

    for i in range(w):
        s, e, t = map(int, input().split())
        if s not in path:
            path[s] = {e: -t}
        else:
            if e in path[s]:
                path[s][e] = min(path[s][e], -t)
            else:
                path[s][e] = -t
    start = s
    result = [False for _ in range(n + 1)]
    result[s] = 0
    for i in path[start]:
        result[i] = path[start][i]

    for i in range(n-1):
        for j in path:
            for k in path[j]:
                if result[k] is not False:
                    result[k] = min(result[k], result[j] + path[j][k])
                else:
                    continue
    temp1 = result[1:]
    for j in path:
        for k in path[j]:
            if result[k] is not False:
                result[k] = min(result[k], result[j] + path[j][k])
            else:
                continue
    temp2 = result[1:]
    if temp1 == temp2:
        print('NO')
    else:
        print('YES')
