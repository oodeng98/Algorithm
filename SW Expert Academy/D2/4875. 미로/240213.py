import sys

sys.stdin = open('input.txt')

def delta(a, b):
    ret = []
    for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if 0 <= a + i < N and 0 <= b + j < N and maze[a+i][b+j] != '1':
            ret.append((a+i, b+j))
    return ret


def find_path():
    visit = [[0 for _ in range(N)] for _ in range(N)]
    stack = [start]
    while stack:
        x, y = stack.pop()
        visit[x][y] = 1
        for i, j in delta(x, y):
            if (i, j) == des:
                return True
            if visit[i][j] == 1:
                continue
            stack.append((i, j))
    return False



T = int(input())
for t in range(1, T+1):
    N = int(input())
    maze = []
    start = ()
    des = ()
    for i in range(N):
        temp = input()
        for j in range(N):
            if temp[j] == '2':
                start = (i, j)
            elif temp[j] == '3':
                des = (i, j)
        maze.append(temp)
    
    if find_path():
        print(f"#{t} 1")
    else:
        print(f"#{t} 0")
    