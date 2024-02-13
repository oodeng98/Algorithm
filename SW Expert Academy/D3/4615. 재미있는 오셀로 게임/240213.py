import sys

sys.stdin = open('input.txt')

def delta(x, y, color):
    board[x][y] = color
    for i, j in [[-1, 0], [1, 0], [0, -1], [0, 1], [1, 1], [-1, -1], [1, -1], [-1, 1]]:
        count = 1
        while 0 <= x + i * count < N and 0 <= y + j * count < N:
            if board[x+i*count][y+j*count] == 0:
                break
            elif board[x+i*count][y+j*count] == color:
                for k in range(1, count):
                    board[x+i*k][y+j*k] = color
                break
            count += 1


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())

    board = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N//2-1, N//2+1):
        board[i][i] = 2
        board[i][N-i-1] = 1
    
    for _ in range(M):
        y, x, color = map(int, input().split())  # y, x, color: 1은 흑돌, 2는 백돌
        delta(x-1, y-1, color)
    
    black = 0
    white = 0
    for i in board:
        for j in i:
            if j == 1:
                black += 1
            elif j == 2:
                white += 1
    print(f"#{t} {black} {white}")