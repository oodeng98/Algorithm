import sys


def down_stair(n, stair):
    if n == 0:
        return 0
    if n == 1:
        return stair[1]
    if n == 2:
        return stair[1] + stair[2]
    return max(stair[n] + stair[n-1] + down_stair(n-3, stair), stair[n] + down_stair(n-2, stair))


input = sys.stdin.readline
num = int(input())
stairs = ['0floor']
for i in range(num):
    stairs.append(int(input()))

print(down_stair(num, stairs))