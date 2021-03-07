def find_square1(data):
    if len(data[0]) == 1:
        if data[0][0] == 1:
            return 1
        return 0
    check = 0
    for i in data:
        for j in i:
            if j == 0:
                check = 1
                break
        if check == 1:
            break
    if check == 0:
        return 1
    data1 = []
    data2 = []
    data3 = []
    data4 = []
    new_square = len(data) // 2
    for i in range(new_square):
        data1.append(data[i][:new_square])
        data2.append(data[i][new_square:])
        data3.append(data[new_square + i][:new_square])
        data4.append(data[new_square + i][new_square:])
    return find_square1(data1) + find_square1(data2) + find_square1(data3) + find_square1(data4)


def find_square0(data):
    if len(data[0]) == 1:
        if data[0][0] == 0:
            return 1
        return 0
    check = 0
    for i in data:
        for j in i:
            if j == 1:
                check = 1
                break
        if check == 1:
            break
    if check == 0:
        return 1
    data1 = []
    data2 = []
    data3 = []
    data4 = []
    new_square = len(data) // 2
    for i in range(new_square):
        data1.append(data[i][:new_square])
        data2.append(data[i][new_square:])
        data3.append(data[new_square + i][:new_square])
        data4.append(data[new_square + i][new_square:])
    return find_square0(data1) + find_square0(data2) + find_square0(data3) + find_square0(data4)

import sys

input = sys.stdin.readline

num = int(input())
square = []
for i in range(num):
    square.append(list(map(int, input().split())))

print(find_square0(square))
print(find_square1(square))