import sys

input = sys.stdin.readline
target = input().rstrip()
num = int(input().rstrip())
error = set(map(int, input().split()))
use_able = list({1, 2, 3, 4, 5, 6, 7, 8, 9, 0} - error)
first = list({1, 2, 3, 4, 5, 6, 7, 8, 9, 10} - error)

i = 0
while i < len(target):
    if i == 0:
        first.sort(key=lambda x: abs(x - int(target[i])))
        replace_target = [first[:3]]
    else:
        use_able.sort(key=lambda x: abs(x - int(target[i])))
        replace_target.append(use_able[:3])
    if int(target[i]) not in replace_target[i]:
        break
    i += 1
# 더 이상은 같은 값을 넣어줄 수 없는 상태, 즉 이제부터 target 값과 가장 가까운 값을 찾아야함
i -= 1  # 같은 값을 넣어줄 수 없는 지점 직전부터 값을 다시 설정해줌
if i < 0:
    i = 0
result = target[:i]
candidate = []
for j in replace_target[i]:
    target_len = len(target)
    if j == 10:
        target_len += 1
    if j > int(target[i]):
        new = result + str(j)
        new_append = min(use_able)
        while len(new) < target_len:
            new += str(new_append)
        candidate.append(new)
    elif j < int(target[i]):
        new = result + str(j)
        new_append = max(use_able)
        while len(new) < target_len:
            new += str(new_append)
        candidate.append(new)
    else:
        try:
            new = result + str(j) + str(replace_target[i+1][0])
            # 결국 이 값도 이미 원래의 값과 달라졌으므로, 큰지 작은지 판별 후 위와 같은 과정을 거치면 된다
            if int(new) > int(target[:len(new)]):
                new_append = min(use_able)
                while len(new) < target_len:
                    new += str(new_append)
            else:
                new_append = max(use_able)
                while len(new) < target_len:
                    new += str(new_append)
            candidate.append(new)
        except IndexError:  # 만약 모든 값을 정상적으로 입력할 수 있는 경우
            candidate.append(target)
standard = 500000
real_result = 0
for i in candidate:
    compare = abs(int(i) - int(target))
    if compare < standard:
        real_result = i
        standard = compare
print(min(abs(100 - int(target)), standard + len(real_result)))

# 모든 숫자를 정상적으로 입력할 수 있는 경우 오류가 발생한다
"""
99999
1
6
"""
