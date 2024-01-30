import sys

input = sys.stdin.readline

N = int(input())
max_count = 0
max_series = []
for n in range(1, N):
    count = 1
    series = [N, n]
    first = N
    second = n
    while second >= 0:
        temp = first
        first = second
        second = temp - second
        count += 1
        series.append(second)
    if max_count < count:
        max_count = count
        max_series = series
print(max_count)
print(' '.join(map(str, max_series[:-1])))