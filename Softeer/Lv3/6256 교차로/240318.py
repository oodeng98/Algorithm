import sys
from collections import deque


def move(count):
    for i in range(count):
        temp = roads()
        if temp:
            for j in temp:
                if road[j]:
                    out[road[j].popleft()] = pre + i
        else:
            break
    if road['A'] and road['B'] and road['C'] and road['D']:
        return True


def roads():
    ret = []
    turn = ["A", "B", "C", "D"]
    for i in range(4):
        if not road[turn[i-1]] and road[turn[i]]:
            ret.append(turn[i])
            if not road[turn[i-3]] and road[turn[i-2]]:
                ret.append(turn[i-2])
            break
    return ret


input = sys.stdin.readline
N = int(input())
seq = [input().split() for _ in range(N)]
road = {'A': deque([]), 'B': deque([]), 'C': deque([]), 'D': deque([])}
out = [0 for _ in range(N)]
pre = 0
check = False
for index, t_w in enumerate(seq):
    if check:
        out[index] = -1
        continue
    t, w = t_w
    t = int(t)
    car = t - pre
    check = move(car)
    pre = t
    road[w].append(index)
check = move(1000000000)
if check:
    for i in road:
        for j in road[i]:
            out[j] = -1

for i in out:
    print(i)