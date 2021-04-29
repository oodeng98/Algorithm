import sys

input = sys.stdin.readline
n, m = map(int, input().split())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
# 1부터 각 점까지 이어서 만들어지는 직사각형들의 합을 구해놓으면 될 듯 싶은데?

row_sum = []
for i in data:
    temp = [0]
    total = 0
    for j in i:
        total += j
        temp.append(total)
    row_sum.append(temp)
row_sum.insert(0, [0 for x in range(len(row_sum) + 1)])

square_sum = [row_sum[0]]
for i in range(1, n + 1):
    temp = []
    for j in range(len(row_sum[i])):
        total = square_sum[-1][j] + row_sum[i][j]
        temp.append(total)
    square_sum.append(temp)

for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    big_square = square_sum[x2][y2]
    small_square = square_sum[x1 - 1][y1 - 1]
    minus_square1 = square_sum[x1 - 1][y2]
    minus_square2 = square_sum[x2][y1 - 1]
    print(big_square + small_square - minus_square1 - minus_square2)
