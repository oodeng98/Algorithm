import sys


input = sys.stdin.readline
start, target = map(int, input().split())
temp = set([start])
if start == target:
    print(0)
else:
    j = 0
    while True:
        j += 1
        new_temp = set([])
        for i in temp:
            new_temp.update([i-1, i+1, i*2])
        if target % 2 == 0:
            if target-1 in new_temp or target+1 in new_temp or target // 2 in new_temp:
                j += 1
                break
        else:
            if target-1 in new_temp or target+1 in new_temp:
                j += 1
                break
        temp |= new_temp
    print(j)