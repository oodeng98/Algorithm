import sys

sys.stdin = open('input.txt')


T = int(input())
for t in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    count = 0
    for i in range(N):
        x, y = lst[i]
        for j in range(i+1, N):
            a, b = lst[j]
            if a < x:
                if y < b:
                    count += 1
            else:  # x < a
                if b < y:
                    count += 1
    print(f"#{t} {count}")