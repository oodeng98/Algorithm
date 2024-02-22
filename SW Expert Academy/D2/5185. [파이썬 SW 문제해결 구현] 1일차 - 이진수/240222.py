import sys

sys.stdin = open('input.txt')


change = {}
for i in range(16):
    change[hex(i)[2:]] = bin(i)[2:].zfill(4)

T = int(input())
for t in range(1, T+1):
    N, num_str = input().split()
    print(f"#{t}", end=' ')
    for i in num_str.lower():
        print(change[i], end='')
    print()