import sys

input = sys.stdin.readline


def direction(way):
    if way == 1:  # 상
        return -1, 0
    elif way == 2:  # 하
        return 1, 0
    elif way == 3:  # 좌
        return 0, -1
    elif way == 4:  # 우
        return 0, 1


def lineup():
    x, y = N // 2, N // 2
    ret = []
    sequence = [3, 2, 4, 1]  # 좌, 하, 우, 상
    index = 0
    length = 1
    count = 1
    while True:
        for _ in range(2):
            dx, dy = direction(sequence[index % 4])
            for _ in range(length):    
                x += dx
                y += dy
                count += 1
                if N ** 2 - 1 < count:
                    while ret and ret[-1] == 0:
                        ret.pop()
                    return ret
                ret.append(grid[x][y])
            index += 1
        length += 1
        
        
def blizzard(d, s):
    x, y = N // 2, N // 2
    dx, dy = direction(d)
    for _ in range(s):
        x += dx
        y += dy
        grid[x][y] = 0
    return


def bomb():
    lst = lineup()
    while True:
        new_lst = []
        check = 0
        index = 0
        while index < len(lst):
            n = lst[index]
            if n == 0:
                index += 1
                continue
            count = 1
            zero_count = 0
            while index + count + zero_count < len(lst):
                if lst[index + count + zero_count] == n:
                    count += 1
                elif lst[index + count + zero_count] == 0:
                    zero_count += 1
                else:
                    break
            if 4 <= count:
                index += count + zero_count
                bomb_count[n] += count
                check = 1
            else:
                index += 1
                new_lst.append(n)
        lst = new_lst
        if not check:
            break
    return lst


def duplicate(lst):
    new_lst = []
    index = 0
    while index < len(lst):
        n = lst[index]
        count = 1
        while index + count < len(lst):
            if lst[index + count] == n:
                count += 1
            else:
                break
        index += count
        new_lst.append(count)
        new_lst.append(n)
    return new_lst


def rollup(lst):
    x, y = N // 2, N // 2
    sequence = [3, 2, 4, 1]  # 좌, 하, 우, 상
    index = 0
    length = 1
    count = 0
    new_grid = [[0 for _ in range(N)] for _ in range(N)]
    while True:
        for _ in range(2):
            dx, dy = direction(sequence[index % 4])
            for _ in range(length):    
                x += dx
                y += dy
                count += 1
                if len(lst) < count or N ** 2 - 1 < count:
                    return new_grid
                new_grid[x][y] = lst[count - 1]
            index += 1
        length += 1
    

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

bomb_count = [0, 0, 0, 0]
for i in range(M):
    d, s = map(int, input().split())
    blizzard(d, s)
    lst = bomb()
    lst = duplicate(lst)
    grid = rollup(lst)

result = 0
for i in range(1, 4):
    result += bomb_count[i] * i
print(result)