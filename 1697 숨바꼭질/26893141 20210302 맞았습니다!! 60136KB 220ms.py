import sys


input = sys.stdin.readline
start, target = map(int, input().split())
total = set([])
new_temp = set([start])
next_temp = new_temp - total
if start == target:
    print(0)
else:
    j = 0
    while True:
        j += 1
        for i in next_temp:
            new_temp.update([i-1, i+1])
            if i * 2 <= target + 2:
                new_temp.add(i * 2)
        next_temp = new_temp - total
        if target in next_temp:
            break
        total |= new_temp
        new_temp.clear()
    print(j)