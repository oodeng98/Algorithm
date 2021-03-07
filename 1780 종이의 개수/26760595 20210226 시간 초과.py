import sys  # 한번에 하는 방법을 찾아야할듯


def count(n, arr, count_dict):  # 뭔가 count가 이상하게 되고있다
    if n == 1:
        count_dict[arr[0][0]] += 1
        return
    ele = {-1: 0, 0: 0, 1: 0}
    for i in arr:
        for j in i:
            ele[j] += 1
    for i in ele:
        if ele[i] == n * n:
            count_dict[i] += 1
            return
    arr_split = [arr[:n//3], arr[n//3:n//3*2], arr[n//3*2:]]
    new_arr = []
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
    for i in range(9):
        count(n//3, new_arr[i], count_dict)
    return


input = sys.stdin.readline
num = int(input())
data = []
for i in range(num):
    data.append(list(map(int, input().split())))
result = {-1: 0, 0: 0, 1: 0}
count(num, data, result)
for i in result:
    print(result[i])