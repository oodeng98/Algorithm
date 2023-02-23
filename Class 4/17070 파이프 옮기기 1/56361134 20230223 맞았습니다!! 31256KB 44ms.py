import sys


def move(tail, direction):
    if tail == 0:
        return
    else:
        count[tail][direction] += 1
        print(tail, count)
    if direction == 0:  # 파이프가 가로로 놓여있을 때
        move(*right(tail))
        move(*diagonal(tail))
    elif direction == 1:  # 파이프가 대각선으로 놓여있을 때
        move(*right(tail))
        move(*diagonal(tail))
        move(*down(tail))
    else:  # 파이프가 세로로 놓여있을 때
        move(*diagonal(tail))
        move(*down(tail))


def right(tail):
    if tail[1] + 1 < size:
        if home[tail[0]][tail[1] + 1] == 0:
            tail = (tail[0], tail[1] + 1)
            return tail, 0
    return 0, 0


def diagonal(tail):
    if tail[0] + 1 < size and tail[1] + 1 < size:
        if home[tail[0]][tail[1] + 1] + home[tail[0] + 1][tail[1]] + home[tail[0] + 1][tail[1] + 1] == 0:
            tail = (tail[0] + 1, tail[1] + 1)
            return tail, 1
    return 0, 0


def down(tail):
    if tail[0] + 1 < size:
        if home[tail[0] + 1][tail[1]] == 0:
            tail = (tail[0] + 1, tail[1])
            return tail, 2
    return 0, 0


input = sys.stdin.readline
size = int(input())
home = []
for _ in range(size):
    home.append(list(map(int, input().split())))

count = {(0, 1): [1, 0, 0]}
for i in range(1, size):
    count[(i, 1)] = [0, 0, 0]


def solution():
    for row in range(size):
        for col in range(2, size):
            if row == 0:
                if home[row][col] == 0:
                    count[(row, col)] = count[(row, col - 1)]
                else:
                    count[(row, col)] = [0, 0, 0]
                continue
            a = count[(row, col - 1)][0] + count[(row, col - 1)][1]
            b = 0
            c = count[(row - 1, col)][1] + count[(row - 1, col)][2]

            if home[row][col]:
                count[(row, col)] = [0, 0, 0]
                continue

            if home[row - 1][col - 1] + home[row][col - 1] + home[row - 1][col] == 0:  # 아무것도 안막힌 경우
                b = sum(count[(row - 1, col - 1)])
            elif home[row - 1][col - 1]:  # 대각선 막힌 경우
                if home[row - 1][col]:  # 위도 막힌 경우
                    c = 0
                    if home[row][col - 1]:  # 왼쪽도 막힌 경우
                        a = 0
                    else:
                        a = count[(row, col - 1)][0]
                else:  # 위는 안막힌 경우
                    c = count[(row - 1, col)][2]
                    if home[row][col - 1]:  # 왼쪽도 막힌 경우
                        a = 0
                    else:
                        a = count[(row, col - 1)][0]
            else:  # 대각선 안막힌경우
                if home[row - 1][col]:  # 위는 막힌 경우
                    c = 0
                    if home[row][col - 1]:  # 왼쪽도 막힌 경우
                        a = 0
                    else:
                        a = count[(row, col - 1)][0] + count[(row, col - 1)][1]
                else:  # 위도 안막힌 경우
                    c = count[(row - 1, col)][1] + count[(row - 1, col)][2]
                    if home[row][col - 1]:  # 왼쪽만 막힌 경우
                        a = 0
            count[(row, col)] = [a, b, c]

    print(sum(count[(size-1, size-1)]))


solution()
