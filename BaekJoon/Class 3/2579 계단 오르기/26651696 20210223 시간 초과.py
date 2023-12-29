import sys


input = sys.stdin.readline
num = int(input())
stairs = {'0': 0}
for i in range(1, num+1):
    stairs[i] = int(input())
floor = [(num, 0)]
values = 0
while True:
    if len(floor) == 0:
        break
    n, value = floor.pop(0)
    if n == 2:
        values = max(values, value + stairs[1] + stairs[2])
    elif n == 1:
        values = max(values, value + stairs[1])
    elif n == 0:
        values = max(values, floor.pop(0)[1])
    else:
        floor.append((n-3, value + stairs[n] + stairs[n-1]))
        floor.append((n-2, value + stairs[n]))

print(values)