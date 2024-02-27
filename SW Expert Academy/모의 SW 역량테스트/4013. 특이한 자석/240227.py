import sys

sys.stdin = open('input.txt')


from collections import deque


def Rotate(magnet, direction):
    if direction == 1:
        magnet.appendleft(magnet.pop())
    else:
        magnet.append(magnet.popleft())
    return magnet


T = int(input())
for t in range(1, T+1):
    K = int(input())
    magnets = [deque(map(int, input().split())) for _ in range(4)]
    # 0은 N, 1은 S
    rotations = [list(map(int, input().split())) for _ in range(K)]
    # 1은 시계방향, -1은 반시계방향
    for temp_k, direction in rotations:
        k = temp_k - 1
        d = direction
        rotates = [(k, direction)]
        for i in range(k, 0, -1):
            d = -d
            if magnets[i][6] != magnets[i-1][2]:
                rotates.append((i-1, d))
            else:
                break
        d = direction
        for i in range(k, 3):
            d = -d
            if magnets[i][2] != magnets[i+1][6]:
                rotates.append((i+1, d))
            else:
                break
        for k, d in rotates:
            magnets[k] = Rotate(magnets[k], d)
    count = 0
    for index, magnet in enumerate(magnets):
        if magnet[0] == 1:
            count += 2 ** index
    print(f"#{t} {count}")