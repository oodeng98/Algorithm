import sys

sys.stdin = open('input.txt')


convert = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9,
}

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    code = ''
    for _ in range(N):
        temp = input().strip('0')
        if code:
            continue
        if temp:
            code = temp.zfill(56)
    check = 0
    result = 0
    for i in range(1, 9):
        temp = convert[code[7*(i-1):7*i]]
        result += temp
        if i % 2:
            check += temp * 3
        else:
            check += temp
    if check % 10:
        print(f"#{t} 0")
    else:
        print(f"#{t} {result}")
