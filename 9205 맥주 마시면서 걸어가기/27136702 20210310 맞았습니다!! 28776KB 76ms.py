import sys


input = sys.stdin.readline
t = int(input())
for l in range(t):
    n = int(input())
    house = tuple(map(int, input().split()))
    convenience = set()
    for i in range(n):
        convenience.add(tuple(map(int, input().split())))
    festival = tuple(map(int, input().split()))
    convenience.add(festival)  # 목적지를 넣어준다
    start = set([house])
    while True:
        near = set()
        for i in start:
            for j in convenience:
                if abs(j[0] - i[0]) + abs(j[1] - i[1]) <= 1000:
                    near.add(j)
        convenience -= near
        start = near
        if not near:
            check = 1
            break
        elif festival in near:
            check = 0
            break
    if check == 1:
        print('sad')
    else:
        print('happy')
