import sys


def d(num):
    return (num * 2) % 10000


def s(num):
    if num == 1:
        return 9999
    else:
        return num - 1


def l(num):
    left_to_right = num // 1000
    return (num % 1000) * 10 + left_to_right


def r(num):
    right_to_left = num % 10
    return right_to_left * 1000 + num // 10


input = sys.stdin.readline
count = int(input())
for k in range(count):
    n, target = map(int, input().split())
    start = [n]
    position = []
    while True:
        temp = []
        for i in start:
            temp.extend([d(i), s(i), l(i), r(i)])
        check = 0
        for i in range(len(temp)):
            if temp[i] == target:
                position = [i, len(temp)]
                check = 1
                break
        if check == 1:
            break
        start = temp
    result = ''
    squared = position[1]
    while squared != 1:
        standard = int(squared / 4)
        if position[0] < standard:
            result += 'D'
            position[0] -= 0
        elif position[0] < standard * 2:
            result += 'S'
            position[0] -= standard
        elif position[0] < standard * 3:
            result += 'L'
            position[0] -= standard * 2
        else:
            result += 'R'
            position[0] -= standard * 3
        squared /= 4
    print(result)
