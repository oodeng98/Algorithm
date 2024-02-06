import sys

sys.stdin = open('input.txt')

def sudo():
    # 가로 체크
    for i in arr:
        check_dic = {}
        for j in i:
            if j in check_dic:
                return 0
            check_dic[j] = 0
    # 세로 체크
    for i in range(9):
        check_dic = {}
        for j in range(9):
            if arr[j][i] in check_dic:
                return 0
            check_dic[arr[j][i]] = 0
    # 작은 격자 체크
    for i in range(3):
        for j in range(3):
            x, y = 3 * i, 3 * j
            check_dic = {}
            for k in range(3):
                for l in range(3):
                    if arr[x + k][y + l] in check_dic:
                        return 0
                    check_dic[arr[x + k][y + l]] = 0
    return 1

T = int(input())
for t in range(1, T+1):
    arr = [input().split() for _ in range(9)]
    print(f"#{t} {sudo()}")
