import sys
import copy


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
    result = [[False for _ in range(n + 1)] for _ in range(n + 1)]
    for i in path:
        for j in path[i]:
            result[i][j] = path[i][j]

    for i in range(1, n + 1):
        for j in path:
            for k in path[j]:
                if result[i][k] is not False and result[i][j] is not False:
                    result[i][k] = min(result[i][k], result[i][j] + min(result[j][k], path[j][k]))
                else:
                    continue

    temp = copy.deepcopy(result)

    for i in range(1, n + 1):
        for j in path:
            for k in path[j]:
                if result[i][k] is not False and result[i][j] is not False:
                    result[i][k] = min(result[i][k], result[i][j] + min(result[j][k], path[j][k]))
                else:
                    continue

    if temp == result:
        print('NO')
    else:
        print('YES')
# 1인 경우를 고려하지 않았나?
