import sys

input =  sys.stdin.readline

for _ in range(4):
    temp = list(map(int, input().split()))
    square1 = temp[:4]
    square2 = temp[4:]
    checkx = set(range(square1[0], square1[2] + 1)) & set(range(square2[0], square2[2] + 1))
    checky = set(range(square1[1], square1[3] + 1)) & set(range(square2[1], square2[3] + 1))
    if len(checkx) == 0 or len(checky) == 0:
        print('d')
    elif len(checkx) == 1 and len(checky) == 1:
        print('c')
    elif len(checkx) == 1 or len(checky) == 1:
        print('b')
    else:
        print('a')
    print(checkx, checky)
    # x,y중 하나만 겹치면? 그걸 해결 못하네