def plus(x, y):
    candidate = [(x, y)]
    for i in range(1, M):
        if x - i >= 0:
            candidate.append((x - i, y))
        if x + i < N:
            candidate.append((x + i, y))
        if y - i >= 0:
            candidate.append((x, y - i))
        if y + i < N:
            candidate.append((x, y + i))
    
    ret = 0
    for i, j in candidate:
        ret += area[i][j]
    return ret


def axe(x, y):
    candidate = [(x, y)]
    for i in range(1, M):
        if x - i >= 0 and y - i >= 0:
            candidate.append((x - i, y - i))
        if x + i < N and y + i < N:
            candidate.append((x + i, y + i))
        if x - i >= 0 and y + i < N:
            candidate.append((x - i, y + i))
        if x + i < N and y - i >= 0:
            candidate.append((x + i, y - i))
    
    ret = 0
    for i, j in candidate:
        ret += area[i][j]
    return ret


T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    area = []
    for i in range(N):
        area.append(list(map(int, input().split())))
    answer = 0

    for i in range(N):
        for j in range(N):
            answer = max(answer, plus(i, j), axe(i, j))

    print(f"#{t+1} {answer}")
