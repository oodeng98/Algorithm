import sys
import bisect

input = sys.stdin.readline
target = input().rstrip()
num = int(input().rstrip())
error = set(map(int, input().split()))
use_able = list({1, 2, 3, 4, 5, 6, 7, 8, 9, 0} - error)
use_able.sort()
first = set(10 * x + y for x in use_able for y in use_able)
first.update(use_able)
if use_able:
    if use_able[0] == 0 and len(use_able) != 1:
        """
9
9
1 2 3 4 5 6 7 8 9
        """
        temp = 100 * use_able[1] + 10 * use_able[0] + use_able[0]
    else:
        temp = 100 * use_able[0] + 10 * use_able[0] + use_able[0]
    first.add(temp)
    first = sorted(list(first))
    i = 0
    # 어디서부터 다른 값으로 대체해줘야 하는지 찾아내기
    while i < len(target):
        if int(target[i]) not in use_able:
            break
        i += 1
    i = max(i, 1)
    # 가장 처음은 자릿수 2개를 한꺼번에 비교해줘야할듯
    correct = target[:i - 1]
    summit = target[i - 1:i + 1]  # 자릿수가 작은게 문제구나, 정확히는 자릿수가 많아질 경우 문제가 생김
    pos = bisect.bisect_left(first, int(summit))  # 이 위치에 삽입될것이다-> 결과값과 결과값 -1값이 가장 가까운 크고작은값
    candidate = []
    try:
        big = str(first[pos])
        use_able_min = min(use_able)
        for j in range(len(target) - i - 1):
            big += str(use_able_min)
        candidate.append(correct + big)
    except IndexError:
        pass
    try:
        small = str(first[pos-1])
        use_able_max = max(use_able)
        for j in range(len(target) - i - 1):
            small += str(use_able_max)
        candidate.append(correct + small)
    except IndexError:
        pass
    candidate_count = []
    for i in candidate:
        candidate_count.append(abs(int(i) - int(target)) + len(i))
    result = min(abs(100 - int(target)), min(candidate_count))
    print(result)
else:
    print(abs(100 - int(target)))