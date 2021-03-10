import sys

input = sys.stdin.readline
target = int(input().rstrip())
num = int(input().rstrip())
error = set(input().split())
use_able = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'} - error  # 가능한 숫자를 넣어보고, 그중 최솟값을 다음 방향으로 선택하는 방안은?
replace_target = ''
i = 0
while True:
    if not (set(str(target + i)) - use_able) or not (set(str(target - i)) - use_able):
        break
    i += 1
print(min(i + len(str(target)), abs(100 - target)))
