import sys

sys.stdin = open('input.txt')


def Manhattan(a, b, c, d):
    return abs(a - c) + abs(b - d)


T = int(input())
for t in range(1, T+1):
    N = int(input())
    Map = [list(map(int, input().split())) for _ in range(N)]
    person = []
    stair_pos = []
    for i in range(N):
        for j in range(N):
            if Map[i][j] == 1:
                person.append((i, j))
            elif 2 <= Map[i][j]:
                stair_pos.append((i, j))

    n = len(person)
    min_value = float('inf')
    for i in range(2 ** n):
        stair = [[], []]
        length = [0, 0]
        temp = 0
        for j in range(n):
            if i & (1 << j):
                stair[0].append(Manhattan(*person[j], *stair_pos[0]))
                length[0] += 1
            else:
                stair[1].append(Manhattan(*person[j], *stair_pos[1]))
                length[1] += 1
        for j in range(2):
            down = Map[stair_pos[j][0]][stair_pos[j][1]]
            if length[j] <= 3:
                if stair[j]:
                    temp = max(temp, max(stair[j]) + down)
                continue
            stair[j].sort()
            for k in range(length[j]-3):
                if stair[j][k] + down <= stair[j][k+3]:
                    continue
                stair[j][k+3] = stair[j][k] + down
            temp = max(temp, stair[j][-1] + down)
        min_value = min(min_value, temp)

    print(f"#{t} {min_value+1}")