import sys


def move(tail, direction):
    if tail == 0:
        return
    else:
        count[tail] += 1
    if direction == 0:  # 파이프가 가로로 놓여있을 때
        move(*right(tail))
        move(*diagonal(tail))
    elif direction == 1:  # 파이프가 대각선으로 놓여있을 때
        move(*right(tail))
        move(*diagonal(tail))
        move(*down(tail))
    else:  # 파이프가 세로로 놓여있을 때
        move(*diagonal(tail))
        move(*down(tail))


def right(tail):
    if tail[1] + 1 < size:
        if home[tail[0]][tail[1] + 1] == 0:
            tail = (tail[0], tail[1] + 1)
            return tail, 0
    return 0, 0


def diagonal(tail):
    if tail[0] + 1 < size and tail[1] + 1 < size:
        if home[tail[0]][tail[1] + 1] + home[tail[0] + 1][tail[1]] + home[tail[0] + 1][tail[1] + 1] == 0:
            tail = (tail[0] + 1, tail[1] + 1)
            return tail, 1
    return 0, 0


def down(tail):
    if tail[0] + 1 < size:
        if home[tail[0] + 1][tail[1]] == 0:
            tail = (tail[0] + 1, tail[1])
            return tail, 2
    return 0, 0


input = sys.stdin.readline
size = int(input())
home = []
for _ in range(size):
    home.append(list(map(int, input().split())))

count = {}
for i in range(size):
    for j in range(size):
        count[(i, j)] = 0
move((0, 1), 0)
print(count[(size-1, size-1)])
