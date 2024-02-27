import sys


sys.stdin = open('input.txt')

for t in range(1, 11):
    T = int(input())
    ladder = []
    for _ in range(100):
        ladder.append(input().split())
    
    for i in range(100):
        if ladder[-1][i] == '2':
            des = i
            break
    x, y = 99, des

    while 0 < x:
        if 0 <= y - 1 and ladder[x][y-1] == '1':
            while 0 < y and ladder[x][y-1] == '1':
                y -= 1
            x -= 1
            continue
        if y + 1 < 100 and ladder[x][y+1] == '1':
            while y + 1 < 100 and ladder[x][y+1] == '1':
                y += 1
            x -= 1
            continue
        if ladder[x-1][y] == '1':
            x -= 1
    print(f"#{t} {y}")
    