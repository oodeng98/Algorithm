import sys

input = sys.stdin.readline
n, k = map(int, input().split())

if n > k:
    print(n - k)
else:
    dic = {}
    for i in range(k):
        dic[i] = 1000000
    position = {n: 0}
    while True:
        temp = list(position.keys())
        for i in temp:
            if i * 2 in position:
                position[i * 2] = min(position[i * 2], position[i])
            else:
                position[i * 2] = position[i]
            if i + 1 in position:
                position[i + 1] = min(position[i + 1], position[i] + 1)
            else:
                position[i + 1] = position[i] + 1
            if i - 1 in position:
                position[i - 1] = min(position[i - 1], position[i] + 1)
            else:
                position[i - 1] = position[i] + 1
        if k in position:
            print(position[k])
            break