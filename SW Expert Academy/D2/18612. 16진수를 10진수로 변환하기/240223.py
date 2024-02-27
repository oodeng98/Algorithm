import sys

sys.stdin = open('input.txt')


T = int(input())
for t in range(1, T+1):
    print(f"#{t}", end=' ')
    temp = ''
    temp_len = 0
    for i in input().strip():
        temp += bin(int(i, base=16))[2:].zfill(4)
        temp_len += 4
        if 7 <= temp_len:
            print(int(temp[:7], base=2), end=' ')
            temp = temp[7:]
            temp_len -= 7
    print(int(temp, base=2))
