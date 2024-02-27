import sys

sys.stdin = open('input.txt')


T = int(input())
for t in range(1, T+1):
    N = int(input())
    bit_str = ''
    for _ in range(N):
        bit_str += input().strip()
    temp = ''
    print(f"#{t}", end=' ')
    for index, i in enumerate(bit_str):
        if index and index % 7 == 0:
            print(int(temp, base=2), end=' ')
            temp = ''
        temp += i
    print(int(temp, base=2))