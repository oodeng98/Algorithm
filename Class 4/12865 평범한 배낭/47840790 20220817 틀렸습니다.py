import sys
import copy

input = sys.stdin.readline
n, k = map(int, input().split())

arr = []
for i in range(n):
    arr.append(tuple(map(int, input().split())))
arr.sort(key=lambda x: x[0])

bag = {}
for i in range(k+1):
    bag[i] = [0, []]

for i in range(n):
    for j in bag:
        if j + arr[i][0] <= k and i not in bag[j][1]:
            if bag[j + arr[i][0]][0] > bag[j][0] + arr[i][1]:
                continue
            else:
                bag[j + arr[i][0]][0] = bag[j][0] + arr[i][1]
                bag[j + arr[i][0]][1] = copy.deepcopy(bag[j][1])
                bag[j + arr[i][0]][1].append(i)

print(max(bag.values())[0])
