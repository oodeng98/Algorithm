import sys


def d(num):
    return (num * 2) % 10000


def d_reverse(num):
    if num % 2 != 0:
        return 0
    return [num // 2, (num + 10000) // 2]


def s(num):
    if num == 0:
        return 9999
    return num - 1


def s_reverse(num):
    if num == 9999:
        return 0
    return num + 1


def l(num):
    left_to_right = num // 1000
    return (num % 1000) * 10 + left_to_right


def r(num):
    right_to_left = num % 10
    return right_to_left * 1000 + num // 10


def find_path(pos, len_total):
    result = ''
    while len_total != 1:
        standard = int(len_total / 4)
        if pos < standard:
            result += 'D'
            pos -= 0
        elif pos < standard * 2:
            result += 'S'
            pos -= standard
        elif pos < standard * 3:
            result += 'L'
            pos -= standard * 2
        else:
            result += 'R'
            pos -= standard * 3
        len_total /= 4
    return result


input = sys.stdin.readline
count = int(input())
for k in range(count):
    n, target = map(int, input().split())
    start = {n: ''}
    from_target = {target: ''}
    position = 0
    count1 = 0
    count2 = 0
    while True:
        lst1 = []
        for j in start:
            if d(j) not in start:
                lst1.append((d(j), j, 'D'))
            if s(j) not in start:
                lst1.append((s(j), j, 'S'))
            if l(j) not in start:
                lst1.append((l(j), j, 'L'))
            if r(j) not in start:
                lst1.append((r(j), j, 'R'))
        temp = set([x[0] for x in lst1]) & set(from_target.keys())
        for i in lst1:
            if i[0] not in start:
                start[i[0]] = start[i[1]] + i[2]
        if temp:
            break

        lst2 = []
        for j in from_target:  # 이거 그냥 DSLR함수를 사용하면 안된다
            if d_reverse(j):
                if d_reverse(j)[0] not in from_target:
                    lst2.append((d_reverse(j)[0], j, 'D'))
                if d_reverse(j)[1] not in from_target:
                    lst2.append((d_reverse(j)[1], j, 'D'))
            if s_reverse(j) not in from_target:
                lst2.append((s_reverse(j), j, 'S'))
            if l(j) not in from_target:
                lst2.append((r(j), j, 'L'))
            if r(j) not in from_target:
                lst2.append((l(j), j, 'R'))
        temp = set([x[0] for x in lst2]) & set(start.keys())
        for i in lst2:
            if i[0] not in from_target:
                from_target[i[0]] = from_target[i[1]] + i[2]
        if temp:
            break
    print(start[list(temp)[0]], end='')
    print(''.join(reversed(from_target[list(temp)[0]])))
