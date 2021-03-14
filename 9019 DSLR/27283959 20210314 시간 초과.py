import sys
import collections


def d(num):
    return (num * 2) % 10000


def s(num):
    if num == 0:
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
    start = collections.deque([n])
    position = []
    i = 0
    while True:
        turn = start.popleft()
        new = [d(turn), s(turn), l(turn), r(turn)]
        if target in new:
            # 진짜 순서는 len(start) + 여기서의 순서
            break
        start.extend(new)
        i += 1
    position = len(start) + i + new.index(target)
    standard = 1
    while standard < position:
        standard *= 4
    standard //= 4
    lst = ['D', 'S', 'L', 'R']
    result = ''
    while standard > 1:
        temp = int(position // standard)
        result += lst[temp - 1]
        position -= standard * temp
        standard /= 4
    result += lst[int(position)]
    print(result)
