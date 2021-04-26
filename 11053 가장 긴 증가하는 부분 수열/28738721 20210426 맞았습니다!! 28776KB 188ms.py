import sys

input = sys.stdin.readline
n = int(input())
data = [0]
data.extend(list(map(int, input().split())))
count = [0 for x in range(n + 1)]
for i in range(1, n + 1):
    temp = 0
    for j in range(i):
        if data[j] < data[i]:
            temp = max(temp, count[j])
    count[i] = temp + 1
print(max(count))
