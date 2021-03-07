def r(lst):
    lst.reverse()
    return lst


def d(lst):
    if not lst:
        return 0
    return lst[1:]


import sys


input = sys.stdin.readline
num = int(input())
for i in range(num):
    func = input().rstrip()
    trash = int(input())
    if trash == 0:
        new_trash = input()
        arr = []
    else:
        arr = input().strip('[]\n').split(',')
    for i in range(trash):
        arr[i] = int(arr[i])
    for i in func:
        if i == 'R':
            arr = r(arr)
        elif i == 'D':
            arr = d(arr)
        if arr == 0:
            break
    if arr == 0:
        print('error')
    else:
        print(arr)