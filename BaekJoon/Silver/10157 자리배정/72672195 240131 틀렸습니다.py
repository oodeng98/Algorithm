import sys

def check(x, y):
    return 0 < x <= C and 0 < y <= R

input = sys.stdin.readline

C, R = map(int, input().split())
K = int(input())
if K > C * R:
    print(0)
else:
    dic = {(1, 1): 0}
    pos = [1, 1]
    count = 1
    now_dir = 0
    dir = {0: 1, 1: 2, 2: 3, 3: 0} # 0: 위, 1: 오른쪽, 2: 아래, 3: 왼쪽
    while True:
        if now_dir == 0:
            temp = (pos[0], pos[1] + 1)
            if check(*temp) and temp not in dic:
                dic[temp] = 0
                pos[1] += 1
                count += 1
            else:
                now_dir = dir[now_dir]
        if now_dir == 1:
            temp = (pos[0] + 1, pos[1])
            if check(*temp) and temp not in dic:
                dic[temp] = 0
                pos[0] += 1
                count += 1
            else:
                now_dir = dir[now_dir]
        if now_dir == 2:
            temp = (pos[0], pos[1] - 1)
            if check(*temp) and temp not in dic:
                dic[temp] = 0
                pos[1] -= 1
                count += 1
            else:
                now_dir = dir[now_dir]
        if now_dir == 3:
            temp = (pos[0] - 1, pos[1])
            if check(*temp) and temp not in dic:
                dic[temp] = 0
                pos[0] -= 1
                count += 1
            else:
                now_dir = dir[now_dir]
        if count >= K:
            break
    print(*pos)
    