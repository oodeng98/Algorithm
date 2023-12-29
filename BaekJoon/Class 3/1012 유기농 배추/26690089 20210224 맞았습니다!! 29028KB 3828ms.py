import sys


def ver(a, b):
    if a[0] == b[0]:
        if a[1] - b[1] == 1 or b[1] - a[1] == 1:
            return 1
    return 0


def hor(a, b):
    if a[1] == b[1]:
        if a[0] - b[0] == 1 or b[0] - a[0] == 1:
            return 1
    return 0


input = sys.stdin.readline
num = int(input())
for k in range(num):
    farm = list(map(int, input().split()))
    data = []
    for i in range(farm[-1]):
        data.append(list(map(int, input().split())))
    group = 0
    while True:
        if len(data) == 0:
            print(group)
            break
        temp = [data.pop(0)]
        i = 0
        while True:
            for j in data:
                if ver(temp[i], j) or hor(temp[i], j):
                    if j not in temp:
                        temp.append(j)
            i += 1
            if i >= len(temp):
                break
        for i in range(1, len(temp)):
            data.remove(temp[i])
        group += 1