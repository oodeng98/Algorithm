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
    # 그냥 모든 지점을 다 고려해주는게 맞나?
    # 그러면 n*(m+w)가 되는데?
    # 이사람이 말한거처럼 node 0을 설정하고 거기서 모든 길을 연결해주는게 맞아보이는데
