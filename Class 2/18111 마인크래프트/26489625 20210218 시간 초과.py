import sys

input = sys.stdin.readline


x, y, block = map(int, input().split())
data = []
for i in range(x):
    data.append(list(map(int, input().split())))

start = 256
finish = 0
for i in data:
    for j in i:
        if start > j:
            start = j
        if finish < j:
            finish = j

times = []
for k in range(start, finish + 1):
    blocks = block
    time = 0
    for i in data:
        for j in i:
            if k > j:
                blocks -= k - j
                time += k - j
            else:
                blocks += j - k
                time += (j - k) * 2
    if blocks < 0:
        print(f'height {k} is impossible')
    else:
        times.append((time, k))
times = sorted(times, key=lambda x: x[1], reverse=True)
times = sorted(times, key=lambda x: x[0])
print(times[0][0], times[0][1])