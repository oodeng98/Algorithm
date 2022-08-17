import sys

input = sys.stdin.readline
n, k = map(int, input().split())

if n > k:
    print(n - k)
else:
    position = {n: 0}
    while True:
        temp = list(position.keys())
        for i in temp:
            if 0 <= i * 2 <= 100000:
                if i * 2 in position:
                    position[i * 2] = min(position[i * 2], position[i])
                else:
                    position[i * 2] = position[i]
            if 0 <= i + 1 <= 100000:
                if i + 1 in position:
                    position[i + 1] = min(position[i + 1], position[i] + 1)
                else:
                    position[i + 1] = position[i] + 1
            if 0 <= i - 1 <= 100000:
                if i - 1 in position:
                    position[i - 1] = min(position[i - 1], position[i] + 1)
                else:
                    position[i - 1] = position[i] + 1
        if k in position:
            print(position[k])
            break
