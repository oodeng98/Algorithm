import sys


def r(direction):
    if direction == 1:
        direction = 0
    else:
        direction = 1
    return direction


def d(lst, direction):
    if not lst:
        return 0
    if direction == 1:
        lst.pop(0)
    else:
        lst.pop(-1)
    return lst


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
    arr = list(map(int, arr))
    dire = 1
    for i in func:
        if i == 'R':
            dire = r(dire)
        elif i == 'D':
            arr = d(arr, dire)
        if arr == 0:
            break
    if arr == 0:
        print('error')
    else:
        if dire == 1:
            print(arr)
        else:
            arr.reverse()
            print(arr)