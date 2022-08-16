import sys


def quadtree(n, square):
    if n == 1:
        return square[0][0]
    check = set([])
    for i in range(n):
        check.update(square[i])
    if len(check) == 1:
        return square[0][0]
    else:
        new_n = n // 2
        up = square[:new_n]
        down = square[new_n:]
        left_up = [x[:new_n] for x in up]
        right_up = [x[new_n:] for x in up]
        left_down = [x[:new_n] for x in down]
        right_down = [x[new_n:] for x in down]
        return quadtree(new_n, left_up), quadtree(new_n, right_up), quadtree(new_n, left_down), quadtree(new_n,
                                                                                                         right_down)


input = sys.stdin.readline
num = int(input())
data = []
for i in range(num):
    data.append(input().rstrip())
for i in range(num):
    data[i] = [int(x) for x in data[i]]
result = str(quadtree(num, data)).replace(',', '')
print(result.replace(' ', ''))