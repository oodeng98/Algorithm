import sys

sys.stdin = open('input.txt')
for t in range(1, 11):
    n = int(input())
    arr = [input() for _ in range(8)]
    result = 0
    # 가로 체크
    for s in arr:
        for i in range(8 - n + 1):
            check = 1
            for j in range(n // 2):
                if s[i+j] != s[i+n-1-j]:
                    check = 0
                    break
            if check:
                result += 1
    # 세로 체크
    for i in range(8):
        for j in range(8 - n + 1):
            check = 1
            for k in range(n // 2):
                if arr[j+k][i] != arr[j+n-1-k][i]:
                    check = 0
                    break
            if check:
                result += 1
    print(f"#{t} {result}")
