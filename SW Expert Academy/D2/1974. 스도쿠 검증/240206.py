import sys

sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    arr = [input().split() for _ in range(9)]
    check = 0
    # 가로 체크
    for i in arr:
        if len(set(i)) != 9:
            check = 1
    if check:
        print(f"#{t} 0")
        continue
    # 세로 체크
    for i in range(9):
        temp = set()
        for j in range(9):
            temp.add(arr[j][i])
        if len(temp) != 9:
            check = 1
    if check:
        print(f"#{t} 0")
        continue
    # 작은 격자 체크
    for i in range(3):
        for j in range(3):
            x, y = 3 * i, 3 * j
            temp = set()
            for k in range(3):
                for l in range(3):
                    temp.add(arr[x + k][y + l])
            if len(temp) != 9:
                check = 1
    if check:
        print(f"#{t} 0")
        continue
    print(f"#{t} 1")

