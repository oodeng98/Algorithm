import sys


def up(maze, present):
    height_position = present[0] - 1
    if height_position < 0:
        return 0
    else:
        if maze[height_position][present[1]] == 1:
            return height_position, present[1]
        else:
            return 0


def down(maze, present):
    try:
        height_position = present[0] + 1
        if maze[height_position][present[1]] == 1:
            return height_position, present[1]
        else:
            return 0
    except IndexError:
        return 0


def right(maze, present):
    try:
        width_position = present[1] + 1
        if maze[present[0]][width_position] == 1:
            return present[0], width_position
        else:
            return 0
    except IndexError:
        return 0


def left(maze, present):
    width_position = present[1] - 1
    if width_position < 0:
        return 0
    else:
        if maze[present[0]][width_position] == 1:
            return present[0], width_position
        else:
            return 0


def find_next(maze, present):
    result = []
    up_position = up(maze, present)
    if up_position:
        result.append(up_position)
    left_position = left(maze, present)
    if left_position:
        result.append(left_position)
    down_position = down(maze, present)
    if down_position:
        result.append(down_position)
    right_position = right(maze, present)
    if right_position:
        result.append(right_position)

    return result


input = sys.stdin.readline
height, width = map(int, input().split())
data = []
for i in range(height):
    data.append(input().rstrip())
for i in range(height):
    data[i] = [int(x) for x in data[i]]
path = set([])
next_position = set([(0, 0)])  # 중복을 제거해줘야함
count = 1
while True:
    temp = set([])
    for i in next_position:
        temp.update(find_next(data, i))
    path.update(next_position)
    if (height-1, width-1) in temp:
        count += 1
        print(count)
        break
    next_position = temp - path
    count += 1