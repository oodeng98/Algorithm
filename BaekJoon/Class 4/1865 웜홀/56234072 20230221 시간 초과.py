import sys


def circuit():
    for test in range(2):
        for i in range(1, n + 1):  # 노드 i 에서 출발
            for j in range(1, n + 1):  # 노드 j 를 거치고
                for k in range(1, n + 1):  # 노트 k 에 도착
                    try:
                        if path[i][k] > path[i][j] + path[j][k]:
                            if test:
                                print('YES')
                                return
                            path[i][k] = path[i][j] + path[j][k]
                    except TypeError:
                        continue
                    if i == k:
                        if path[i][k] < 0:
                            print('YES')
                            return
    print('NO')
    return


# input part
input = sys.stdin.readline
tc = int(input())
for case in range(tc):
    n, m, w = map(int, input().split())
    path = [[None for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        path[i][i] = 0

    for i in range(m):
        s, e, t = map(int, input().split())
        if path[s][e] is None:
            path[s][e] = t
        else:
            path[s][e] = min(path[s][e], t)
        if path[e][s] is None:
            path[e][s] = t
        else:
            path[e][s] = min(path[e][s], t)

    for _ in range(w):
        s, e, t = map(int, input().split())
        if path[s][e] is None:
            path[s][e] = -t
        else:
            path[s][e] = min(path[s][e], -t)

    circuit()
