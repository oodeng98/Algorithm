import sys


input = sys.stdin.readline
t = int(input())
for i in range(t):
    n = int(input())
    house = tuple(map(int, input().split()))
    convenience = []
    for j in range(n):
        convenience.append(tuple(map(int, input().split())))
    festival = tuple(map(int, input().split()))
    # 맥주를 풀로 채우고 갈 수 있는 최대 거리는 1000m
    convenience.extend([house, festival])
    convenience = sorted(convenience, key=lambda x: x[0] + x[1])
    convenience = convenience[convenience.index(house):]
    penalty = 0
    fail = 0
    for j in range(len(convenience) - 1):
        result = (convenience[j][0] + convenience[j][1] + 1000 - penalty) - (convenience[j+1][0] + convenience[j+1][1])
        if result < 0:
            fail = 1
            break
        else:
            penalty = result % 50
    if fail:
        print('sad')
    else:
        print('happy')
