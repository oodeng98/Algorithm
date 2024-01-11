import sys

def unionFind(x):
    if x != visitRoot[x]:
        visitRoot[x] = unionFind(visitRoot[x])
    return visitRoot[x]


input  = sys.stdin.readline

v, e = map(int, input().split())
visitRoot = [i for i in range(v + 1)]
graph = []
for i in range(e):
    graph.append(list(map(int, input().split()))) # [A, B, C]의 형태, A번 정점과 B번 정점이 가중치 C인 간선으로 연결되어 있다는 의미

graph.sort(key=lambda x: x[2])

answer = 0
for s, e, w in graph:
    sRoot = unionFind(s)
    eRoot = unionFind(e)
    if sRoot != eRoot: # 그룹 합치는 부분
        if sRoot > eRoot:
            visitRoot[sRoot] = eRoot
        else:
            visitRoot[eRoot] = sRoot
        answer += w

print(answer)