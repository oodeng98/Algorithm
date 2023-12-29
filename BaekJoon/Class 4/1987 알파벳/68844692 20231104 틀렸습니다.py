import sys


def move(a, b, c):
    result = []
    if 0 <= a - 1:
        if board[a - 1][b] not in c:
            result.append((a - 1, b, c + board[a - 1][b]))
    if a + 1 < n:
        if board[a + 1][b] not in c:
            result.append((a + 1, b, c + board[a + 1][b]))
    if 0 <= b - 1:
        if board[a][b - 1] not in c:
            result.append((a, b - 1, c + board[a][b - 1]))
    if b + 1 < n:
        if board[a][b + 1] not in c:
            result.append((a, b + 1, c + board[a][b + 1]))
    return result


input = sys.stdin.readline
n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(input().strip()))

position = set()
position.add((0, 0, board[0][0]))
next_position = set()

count = 1
while True:
    for i in position:
        x, y, path = i
        next_position.update(move(x, y, path))
    
    if not next_position:
        break
    
    count += 1
    position.clear()
    position.update(next_position)
    next_position.clear()
    
print(count)