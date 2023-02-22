import sys


def circuit(trial=1):
    for i in range(n):  # 노드 i 에서 출발
        for j in range(n):  # 노드 j 를 거치고
            for k in range(n):  # 노트 k 에 도착
                if trial == 1:
                    path[i][k] = min(path[i][k], path[i][j] + path[j][k])
                else:
                    if path[i][k] > path[i][j] + path[j][k]:
                        print('YES')
                        return
    if trial == 2:
        print('NO')


# input part
input = sys.stdin.readline
tc = int(input())
for case in range(tc):
    n, m, w = map(int, input().split())
    path = [[10001 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        path[i][i] = 0

    for i in range(m):
        s, e, t = map(int, input().split())
        path[s-1][e-1] = min(path[s-1][e-1], t)
        path[e-1][s-1] = min(path[e-1][s-1], t)

    for _ in range(w):
        s, e, t = map(int, input().split())
        path[s-1][e-1] = min(path[s-1][e-1], -t)

    circuit()
    circuit(trial=2)
