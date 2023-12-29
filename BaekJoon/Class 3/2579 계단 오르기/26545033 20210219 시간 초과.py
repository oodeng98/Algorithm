import sys


def down_stair(n, stair):  # n은 무조건 밟아야 하는 계단의 층수
    if n == 1:
        return stair[1]
    elif n == 2:  # 위에서부터 내려오고, n은 무조건 밟아야 하므로 n==2일때 1은 무조건 포함하는게 이득
        return stair[1] + stair[2]
    elif n == 3:
        return stair[3] + max(stair[1], stair[2])
    return max(stair[n] + stair[n-1] + down_stair(n-3, stair), stair[n] + down_stair(n-2, stair))


input = sys.stdin.readline
num = int(input())
stairs = {'0': 0}
for i in range(1, num+1):
    stairs[i] = int(input())

print(down_stair(num, stairs))