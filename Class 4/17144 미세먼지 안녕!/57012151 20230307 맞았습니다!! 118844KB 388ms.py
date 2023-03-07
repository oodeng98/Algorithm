import sys


input = sys.stdin.readline
R, C, T = map(int, input().split())
room = []
for i in range(R):
    room.append(list(map(int, input().split())))

air_cleaner = []
for i in range(R):
    if room[i][0] == -1:
        air_cleaner.append(i)

for _ in range(T):
    next_room = [[0 for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if room[i][j] == -1:
                next_room[i][j] = -1
                continue
            count = 0
            spread = room[i][j] // 5
            if spread == 0:
                next_room[i][j] += room[i][j]
                continue
            for r, c in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= r < R and 0 <= c < C:
                    if room[r][c] == -1:
                        continue
                    count += 1
                    next_room[r][c] += spread
            next_room[i][j] += room[i][j] - spread * count

    # left
    for i in range(air_cleaner[0] - 1, -1, -1):
        next_room[i + 1][0] = next_room[i][0]
    # up
    next_room[0] = next_room[0][1:] + [next_room[1][-1]]
    # right
    for i in range(air_cleaner[0]):
        next_room[i][-1] = next_room[i + 1][-1]
    # down
    next_room[air_cleaner[0]] = [-1, 0] + next_room[air_cleaner[0]][1:-1]

    # left
    for i in range(air_cleaner[1] + 1, R - 1):
        next_room[i][0] = next_room[i + 1][0]
    # down
    next_room[-1] = next_room[-1][1:] + [next_room[-2][-1]]
    # right
    for i in range(R - 2, air_cleaner[1] - 1, -1):
        next_room[i + 1][-1] = next_room[i][-1]
    # up
    next_room[air_cleaner[1]] = [-1, 0] + next_room[air_cleaner[1]][1:-1]

    room = next_room

ret = 2
for i in room:
    ret += sum(i)
print(ret)
