import sys


def count(n, arr, target):
    if n == 1:
        if arr[0][0] == target:
            return 1
        return 0
    check = 0
    for i in arr:
        for j in i:
            if j != target:
                check = 1
                break
        if check == 1:
            break
    if check == 0:
        return 1
    arr_split = [arr[:n//3], arr[n//3:n//3*2], arr[n//3*2:]]
    new_arr = []
    # 아래부분 고쳐줘야함
    for i in arr_split:
        temp1 = []
        temp2 = []
        temp3 = []
        for j in i:
            temp1.append(j[:n // 3])
            temp2.append(j[n // 3:n // 3 * 2])
            temp3.append(j[n // 3 * 2:])
        new_arr.append(temp1)
        new_arr.append(temp2)
        new_arr.append(temp3)
    result = 0
    for i in range(9):
        result += count(n//3, new_arr[i], target)
    return result


input = sys.stdin.readline
num = int(input())
data = []
for i in range(num):
    data.append(list(map(int, input().split())))
print(count(num, data, -1))
print(count(num, data, 0))
print(count(num, data, 1))