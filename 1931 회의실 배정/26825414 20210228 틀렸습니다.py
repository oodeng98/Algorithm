import sys


input = sys.stdin.readline
num = int(input())
total_data = []
for i in range(num):
    total_data.append(tuple(map(int, input().split())))
total_data.sort(key=lambda x: (x[0], x[1]))
finish = min(total_data, key=lambda x: x[1])
count = 1
for i in range(total_data.index(finish)+1, num):
    if total_data[i][0] >= finish[1]:
        if finish[1] == total_data[i][0] and finish[1] == total_data[i][1]:
            count += 1
            continue
        finish = total_data[i]
        count += 1
    else:
        if total_data[i][0] > finish[0]:
            if total_data[i][1] < finish[1]:
                finish = total_data[i]