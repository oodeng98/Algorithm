import sys

input =  sys.stdin.readline

for _ in range(4):
    temp = list(map(int, input().split()))
    square1 = temp[:4]
    square2 = temp[4:]
    check1 = set(range(square1[0], square1[2])) & set(range(square2[0], square2[2]))
    check2 = set(range(square1[1], square1[3])) & set(range(square2[1], square2[3]))
    if len(check1) == 0 and len(check2) == 0:
        print('d')
    elif len(check1) + len(check2) == 1:
        print('c')
    elif len(check1) == 0 or len(check2) == 0:
        print('b')
    else:
        print('a')
    