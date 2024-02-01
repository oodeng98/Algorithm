import sys


input = sys.stdin.readline

w, h = map(int, input().split())
p, q = map(int, input().split())
T = int(input())

dir = [1, 1]
t = 0
count = 0
while t < T:
    x = p + dir[0]
    y = q + dir[1]
    if x < 0 or w < x: # 위아래 충돌
        dir[0] *= -1
        continue
    if y < 0 or h < y: # 좌우측 충돌
        dir[1] *= -1
        continue
    p += dir[0]
    q += dir[1]
    t += 1
print(p, q)