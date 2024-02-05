import sys

sys.stdin = open('input.txt')

def palindrome():
    for i in range(N-M+1):
        for j in range(N):
            check = 1
            for k in range(M // 2):
                if arr[i+k][j] != arr[i+M-1-k][j]:
                    check = 0
                    break
            if check:
                result = ''
                for k in range(M):
                    result += arr[i+k][j]
                return result
    for i in range(N):
        for j in range(N-M+1):
            check = 1
            for k in range(M // 2):
                if arr[i][j+k] != arr[i][j+M-1-k]:
                    check = 0
                    break
            if check:
                result = ''
                for k in range(M):
                    result += arr[i][j+k]
                return result

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    print(f"#{t} {palindrome()}")