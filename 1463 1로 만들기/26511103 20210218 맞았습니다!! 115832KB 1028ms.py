import sys

input = sys.stdin.readline

num = int(input())
count = 0
temp = [num]
while num != 1:
    temp_temp = temp
    temp = []
    for i in temp_temp:
        if i % 3 == 0:
            temp.append(i / 3)
        if i % 2 == 0:
            temp.append(i / 2)
        temp.append(i - 1)
    count += 1
    if 1 in temp:
        break
print(count)