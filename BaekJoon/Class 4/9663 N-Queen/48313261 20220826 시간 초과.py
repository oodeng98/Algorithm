import sys


def possible_area(path):
    if not path:
        return [1 for _ in range(n)]
    result = [1 for _ in range(n)]
    for index, i in enumerate(path):
        result[i] = 0
        if i + (len(path) - index) < n:
            result[i + (len(path) - index)] = 0
        if 0 <= i - (len(path) - index):
            result[i - (len(path) - index)] = 0
    return result


def queen(path, count):
    new = possible_area(path)
    if 1 not in set(new):
        if count == n:
            return 1
        return 0
    total = 0
    for index, i in enumerate(new):
        if i:
            total += queen(path + [index], count + 1)
    return total


input = sys.stdin.readline
n = int(input())
print(queen([], 0))
