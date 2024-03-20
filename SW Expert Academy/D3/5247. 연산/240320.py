import sys


def cal(n):
    yield n + 1
    yield n - 1
    yield n * 2
    yield n - 10


def Mmaker(N, M):
    check = [0 for _ in range(1000001)]
    candidate = [N]
    check[N] = 1
    count = 1
    while True:
        new_candidate = []
        for i in candidate:
            for j in cal(i):
                if j == M:
                    return count
                if 1 <= j <= 1000000:
                    if check[j]:
                        continue
                    check[j] = 1
                    new_candidate.append(j)
        candidate = new_candidate
        count += 1


sys.stdin = open('input.txt')
T = int(input())
for t in range(1, T+1):
    print(f"#{t} {Mmaker(*map(int, input().split()))}")