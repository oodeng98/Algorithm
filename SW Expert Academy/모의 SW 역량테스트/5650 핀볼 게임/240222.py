import sys

sys.stdin = open('input.txt')


def Move(x, y, direction):
    a, b = x, y
    score = 0
    dx, dy = move[direction]
    while True:
        new_value = 5
        if 0 <= a < N and 0 <= b < N:
            new_value = arr[a][b]
        if new_value != 0:
            if new_value == -1:
                break
            if 6 <= new_value <= 10:
                a, b = wormhole[(a, b)]
                a += dx
                b += dy
                if (a, b) == (x, y):
                    break
                continue
            direction = block[new_value][direction]
            dx, dy = move[direction]
            score += 1
        a += dx
        b += dy
        if (a, b) == (x, y):
            break
    return score


def Game():
    score = 0
    for x in range(N):
        for y in range(N):
            if arr[x][y] != 0:
                continue
            for direction in ['up', 'down', 'right', 'left']:
                score = max(score, Move(x, y, direction))
    return score
        
block = {
            1: {'down': 'right', 'left': 'up', 'right': 'left', 'up': 'down'},  
            2: {'up': 'right', 'left': 'down', 'right': 'left', 'down': 'up'},  
            3: {'up': 'left', 'right': 'down', 'left': 'right', 'down': 'up'},  
            4: {'right': 'up', 'down': 'left', 'left': 'right', 'up': 'down'}, 
            5: {'right': 'left', 'left': 'right', 'down': 'up', 'up': 'down'}
        }


move = {'up': (-1, 0), 'down': (1, 0), 'right': (0, 1), 'left': (0, -1)}


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = []
    wormhole_dic = {i: [] for i in range(6, 11)}
    for i in range(N):
        temp = list(map(int, input().split()))
        for j in range(N):
            if 6 <= temp[j]:
                wormhole_dic[temp[j]].append((i, j))
        arr.append(temp)
    wormhole = {}
    for i in wormhole_dic:
        if wormhole_dic[i]:
            a, b = wormhole_dic[i]
            wormhole[a] = b
            wormhole[b] = a
    print(f"#{t} {Game()}")