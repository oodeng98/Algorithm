import sys


sys.stdin = open("input.txt")

for t in range(1, 11):
    case = int(input())
    arr = []
    for _ in range(100):
        arr.append(list(map(int, input().split())))
    dia1 = 0
    dia2 = 0
    hor_max = 0
    ver_max = 0
    for i in range(100):
        dia1 += arr[i][i]
        dia2 += arr[i][99-i]
        hor = 0 # 가로
        ver = 0 # 세로
        for j in range(100):
            hor += arr[i][j]
            ver += arr[j][i]
        if hor_max < hor:
            hor_max = hor
        if ver_max < ver:
            ver_max = ver
    result = 0
    for i in [dia1, dia2, hor_max, ver_max]:
        if result < i:
            result = i
    print(f"#{t} {result}")