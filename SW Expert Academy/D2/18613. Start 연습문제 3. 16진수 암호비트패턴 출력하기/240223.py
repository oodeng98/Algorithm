import sys

sys.stdin = open('input.txt')


bit_pattern = {
    '001101': 0, 
    '010011': 1, 
    '111011': 2, 
    '110001': 3, 
    '100011': 4, 
    '110111': 5, 
    '001011': 6, 
    '111101': 7, 
    '011001': 8, 
    '101111': 9
}

T = int(input())
for t in range(1, T+1):
    num = ''
    for i in input().strip():
        num += bin(int(i, base=16))[2:].zfill(4)
    num = num.strip('0')
    num = num.zfill(6 * (len(num) // 6 + 1))
    print(f"#{t}", end=' ')
    temp = ''
    for i in range(len(num)):
        temp += num[i]
        if temp in bit_pattern:
            print(bit_pattern[temp], end=' ')
            temp = ''
    print()