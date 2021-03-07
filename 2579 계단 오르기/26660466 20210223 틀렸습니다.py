import sys


input = sys.stdin.readline
num = int(input())
stairs = {'0': 0, num+1: 0}
for i in range(1, num+1):
    stairs[i] = int(input())
floor = {x: 0 for x in range(num+1)}
for i in range(num, -1, -1):
    if i == num-1:
        continue
    value = floor[i]
    if i == 2:
        floor[0] = max(floor[0], value + stairs[1] + stairs[2])
    elif i == 1:
        floor[0] = max(floor[0], value + stairs[1])
    elif i == 0:
        print(floor[0])
    else:
        floor[i-3] = max(floor[i-3], value + stairs[i] + stairs[i-1])
        floor[i-2] = max(floor[i-2], value + stairs[i])