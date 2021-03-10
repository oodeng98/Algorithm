import sys

input = sys.stdin.readline
target = input().rstrip()
num = int(input().rstrip())
error = set(map(int, input().split()))
use_able = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0} - error
replace_target = ''
for i in target:
    small_target = int(i)
    if small_target in use_able:
        replace_target += i
        continue
    else:
        small = 10
        replace = 0
        for j in use_able:
            if small > abs(j - small_target):
                small = abs(j - small_target)
                replace = j
        replace_target += str(replace)
        if replace < int(i):  # 만약 원래 값이 더 크다면 -> 나머지는 무조건 가장 큰 값으로 설정해줘야함
            big = max(use_able)
            while len(replace_target) < len(target):
                replace_target += str(big)
        else:  # 만약 원래 값이 더 작다면 -> 나머지는 무조건 가장 작은 값으로 설정해줘야 한다
            small = min(use_able)
            while len(replace_target) < len(target):
                replace_target += str(small)
        break
print(min(len(replace_target) + abs(int(target) - int(replace_target)), abs(100 - int(target))))
