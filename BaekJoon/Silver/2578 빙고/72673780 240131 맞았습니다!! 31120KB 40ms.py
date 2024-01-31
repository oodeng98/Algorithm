import sys


def bingo_check():
    result = 0
    for i in blank_bingo:
        if sum(i) == 5:
            result += 1
    for i in range(5):
        temp_sum= 0
        for j in range(5):
            temp_sum += blank_bingo[j][i]
        if temp_sum == 5:
            result += 1
    temp_sum1 = 0
    temp_sum2 = 0
    for i in range(5):
        temp_sum1 += blank_bingo[i][i]
        temp_sum2 += blank_bingo[i][4-i]
    if temp_sum1 == 5:
        result += 1
    if temp_sum2 == 5:
        result += 1
    if result >= 3:
        return True
    return False


input = sys.stdin.readline

blank_bingo = [[0 for _ in range(5)] for _ in range(5)]
my_bingo = {}
for i in range(5):
    for j, num in enumerate(map(int, input().split())):
        my_bingo[num] = (i, j)

check = 0
for i in range(5):
    for index, j in enumerate(map(int, input().split())):
        x, y = my_bingo[j]
        blank_bingo[x][y] = 1
        if i < 2:
            continue
        if bingo_check():
            check = 1
            break
    if check:
        break
print(i * 5 + index + 1)
