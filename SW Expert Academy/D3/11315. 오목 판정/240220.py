import sys

sys.stdin = open('input.txt')


def check():
    for i in range(N):
        for j in range(N - 4):
            for k in range(5):
                if board[i][j+k] != 'o':
                    break
            else:
                print('YES')
                return
    
    for i in range(N - 4):
        for j in range(N):
            for k in range(5):
                if board[i+k][j] != 'o':
                    break
            else:
                print('YES')
                return

    for i in range(N - 4):
        for j in range(N - 4):
            for k in range(5):
                if board[i+k][j+k] != 'o':
                    break
            else:
                print('YES')
                return

    for i in range(N - 4):
        for j in range(N - 4):
            for k in range(5):
                if board[N-1-i-k][j+k] != 'o':
                    break
            else:
                print('YES')
                return
    print('NO')


T = int(input())
for t in range(1, T+1):
    N = int(input())
    board = [input().rstrip() for _ in range(N)]
    print(f"#{t}", end=' ')
    check()
