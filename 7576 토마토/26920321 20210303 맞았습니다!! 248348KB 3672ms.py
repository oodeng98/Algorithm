import sys


def up(st, present):
    height_position = present[0] - 1
    if height_position < 0:
        return 0
    else:
        if st[height_position][present[1]] == 0:
            return height_position, present[1]
        else:
            return 0


def down(st, present):
    try:
        height_position = present[0] + 1
        if st[height_position][present[1]] == 0:
            return height_position, present[1]
        else:
            return 0
    except IndexError:
        return 0


def right(st, present):
    try:
        width_position = present[1] + 1
        if st[present[0]][width_position] == 0:
            return present[0], width_position
        else:
            return 0
    except IndexError:
        return 0


def left(st, present):
    width_position = present[1] - 1
    if width_position < 0:
        return 0
    else:
        if st[present[0]][width_position] == 0:
            return present[0], width_position
        else:
            return 0


def find_next(st, present):
    result = []
    up_position = up(st, present)
    if up_position:
        result.append(up_position)
    left_position = left(st, present)
    if left_position:
        result.append(left_position)
    down_position = down(st, present)
    if down_position:
        result.append(down_position)
    right_position = right(st, present)
    if right_position:
        result.append(right_position)

    return result


input = sys.stdin.readline
width, height = map(int, input().split())
storage = []
for i in range(height):
    storage.append(list(map(int, input().split())))
start = set([])
check = 0
for i in range(height):
    for j in range(width):
        if storage[i][j] == 1:
            start.add((i, j))
        elif storage[i][j] == -1:
            check += 1
already = set([])
already |= start
temp = set([])
count = 0
while True:
    temp.clear()
    for i in start:
        temp.update(find_next(storage, i))
    start = temp - already
    if not start:
        break
    already |= start
    count += 1
if len(already) == width * height - check:
    print(count)
else:
    print(-1)