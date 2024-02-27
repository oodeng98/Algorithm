import sys


sys.stdin = open('input.txt')
for t in range(1, int(input()) + 1):
    N = int(input()) // 10
    if N % 2 == 1:
        print(f"#{t} {int((4 ** ((N + 1) // 2) - 1) / 3)}")
    else:
        print(f"#{t} {int(2 * (4 ** (N // 2) - 1) / 3 + 1)}")
