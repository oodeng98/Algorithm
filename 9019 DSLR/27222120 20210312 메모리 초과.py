import sys


def d(num_path):
    return (num_path[0] * 2) % 10000, num_path[1] + 'D'


def s(num_path):
    if num_path[0] == 1:
        return 9999, num_path[1] + 'S'
    else:
        return num_path[0] - 1, num_path[1] + 'S'


def l(num_path):
    left_to_right = num_path[0] // 1000
    return (num_path[0] % 1000) * 10 + left_to_right, num_path[1] + 'L'  # 이거 좀 이상하다, 1000넣으면 1이 나와야하는데 안나옴


def r(num_path):
    right_to_left = num_path[0] % 10
    return right_to_left * 1000 + num_path[0] // 10, num_path[1] + 'R'


input = sys.stdin.readline
num = int(input())
for k in range(num):
    n, target = map(int, input().split())
    n = (n, '')
    start = [d(n), s(n), l(n), r(n)]
    first_check = 0
    for i in start:
        if i[0] == target:
            print(i[1])
            first_check = 1
            break
    if first_check == 1:
        continue
    result = ''
    while True:
        temp = []
        for i in start:
            temp.extend([d(i), s(i), l(i), r(i)])
        check = 0
        for i in temp:
            if i[0] == target:
                result = i[1]
                check = 1
                break
        if check == 1:
            break
        start = temp
    print(result)


