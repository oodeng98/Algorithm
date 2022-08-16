import sys


input = sys.stdin.readline
num = int(input())
total_data = []
for i in range(num):
    total_data.append(tuple(map(int, input().split())))
total_data.sort(key=lambda x: (x[0], x[1]))
count = 0
while total_data:
    finish_ele = min(total_data, key=lambda x: (x[1], x[0]))
    total_data.remove(finish_ele)
    finish = finish_ele[1]
    while total_data:
        if total_data[0][0] < finish:
            total_data.pop(0)
        else:
            break
    count += 1
print(count)