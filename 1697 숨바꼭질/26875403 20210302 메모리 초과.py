import sys


input = sys.stdin.readline
start, target = map(int, input().split())
temp = [start]
if start == target:
    print(0)
else:
    j = 0
    while True:
        j += 1
        new_temp = []
        for i in temp:
            new_temp.extend([i-1, i+1, i*2])
        if target in new_temp:
            break
        temp = new_temp
    print(j)