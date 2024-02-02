import math
import sys

sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    count = 0
    for i in range(1, N):
        count += int(math.sqrt(N ** 2 - i ** 2))
    count *= 4
    count += 4 * N + 1
    print(f'#{t} {count}')