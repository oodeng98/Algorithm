import sys


def up(apart, present):
    height_position = present[0] - 1
    if height_position < 0:
        return 0
    else:
        if apart[height_position][present[1]] == 1:
            return height_position, present[1]
        else:
            return 0


def down(apart, present):
    try:
        height_position = present[0] + 1
        if apart[height_position][present[1]] == 1:
            return height_position, present[1]
        else:
            return 0
    except IndexError:
        return 0


def right(apart, present):
    try:
        width_position = present[1] + 1
        if apart[present[0]][width_position] == 1:
            return present[0], width_position
        else:
            return 0
    except IndexError:
        return 0


def left(apart, present):
    width_position = present[1] - 1
    if width_position < 0:
        return 0
    else:
        if apart[present[0]][width_position] == 1:
            return present[0], width_position
        else:
            return 0


def find_next(apart, present):
    result = []
    up_position = up(apart, present)
    if up_position:
        result.append(up_position)
    left_position = left(apart, present)
    if left_position:
        result.append(left_position)
    down_position = down(apart, present)
    if down_position:
        result.append(down_position)
    right_position = right(apart, present)
    if right_position:
        result.append(right_position)

    return result


def check_complex(apart, present):
    bundle = set([present])
    new = set([present])
    while True:
        temp = set([])
        for i in new:
            temp.update(find_next(apart, i))
        new = temp - bundle
        before = len(bundle)
        bundle.update(new)
        after = len(bundle)
        if after == before:
            break
    return bundle


input = sys.stdin.readline
num = int(input())
data = []
for i in range(num):
    data.append(input().rstrip())
for i in range(num):
    data[i] = [int(x) for x in data[i]]
count = []
for i in range(num):
    for j in range(num):
        if data[i][j] == 1:
            bundle = check_complex(data, (i, j))
            count.append(len(bundle))
            for k in bundle:
                data[k[0]][k[1]] = 0
print(len(count))
for i in sorted(count):
    print(i)