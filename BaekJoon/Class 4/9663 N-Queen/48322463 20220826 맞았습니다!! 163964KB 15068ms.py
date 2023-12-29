import sys


def possible_area(path):
    if not path:
        return [True for _ in range(n)]
    result = [True for _ in range(n)]
    for index, i in enumerate(path):
        result[i] = False
        if i + (len(path) - index) < n:
            result[i + (len(path) - index)] = False
        if 0 <= i - (len(path) - index):
            result[i - (len(path) - index)] = False
    return result


def queen(path, count):
    new = possible_area(path)
    if count == n:
        print(path)
        return 1
    total = 0
    for index, i in enumerate(new):
        if i:
            total += queen(path + [index], count + 1)
    return total


input = sys.stdin.readline
n = int(input())
print(queen([], 0))
# 14, 365596