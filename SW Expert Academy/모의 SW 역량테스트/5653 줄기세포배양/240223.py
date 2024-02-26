import sys

sys.stdin = open('input.txt')


def delta(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        yield x + dx[i], y + dy[i]


T = int(input())
for t in range(1, T+1):
    N, M, K = map(int, input())
    area = [[0 for _ in range(M+300)] for _ in range(N+300)]
    cells = {}
    activate_cells = {}
    # 150, 150자리에 기존 0, 0을 집어넣을 것
    for i in range(N):
        for j, value in enumerate(map(int, input().split())):
            area[150+i][150+j] = value
            cells[(150+i, 150+j)] = [value, value]  # 비활성 체크, 죽음 체크

    for i in range(K):
        for cell in cells:
            cells[cell][0] -= 1
            if cells[cell][0] == -1:
                for x, y in delta(*cell):
                    if area[x][y] == 0:
                        cells[(x, y)] = [cells[cell][0], cells[cell][0]]
                activate_cells[cell] = cells[cell][1]
                del cells[cell]
                
                # activate_cells로 이동
                pass

    print(f"#{t} ")