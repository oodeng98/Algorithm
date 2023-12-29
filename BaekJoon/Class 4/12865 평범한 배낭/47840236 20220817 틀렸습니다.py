import sys

input = sys.stdin.readline
n, k = map(int, input().split())

arr = []
for i in range(n):
    arr.append(tuple(map(int, input().split())))
arr.sort(key=lambda x: x[0])

bag = {}
for i in range(k+1):
    bag[i] = 0

for i in range(n):
    for j in bag:
        if j + arr[i][0] <= k:
            bag[j + arr[i][0]] = max(bag[j + arr[i][0]], bag[j] + arr[i][1])
print(bag[k])
