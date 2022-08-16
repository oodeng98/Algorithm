import sys


input = sys.stdin.readline
num = int(input())
one = list(map(lambda x: x ** 2, range(1, 224)))
temp = [num]
count = 1
check = 0
while True:
    for i in temp:
        if i in one:
            check = 1
            break
    if check == 1:
        break
    temp_temp = temp
    temp = []
    for i in temp_temp:
        for j in one:
            if j < i:
                temp.append(i - j)
    count += 1
print(count)