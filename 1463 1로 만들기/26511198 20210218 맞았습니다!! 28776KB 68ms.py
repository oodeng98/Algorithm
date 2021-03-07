import sys

input = sys.stdin.readline

num = int(input())
count = 0
temp = {num: 0}
while num != 1:
    temp_temp = temp
    temp = {}
    for i in temp_temp:
        if i % 3 == 0:
            temp[i / 3] = 0
        if i % 2 == 0:
            temp[i / 2] = 0
        temp[i - 1] = 0
    count += 1
    if 1 in temp:
        break
print(count)