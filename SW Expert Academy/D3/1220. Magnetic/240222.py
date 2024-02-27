import sys

sys.stdin = open('input.txt')


for t in range(1, 11):
    N = int(input())
    table = [input().split() for _ in range(N)]
    # 1은 N, 2는 S
    result = 0
    for i in range(N):
        temp = ''
        for j in range(N):
            if table[j][i] != '0':
                temp += table[j][i]

        temp = temp.lstrip('2')
        temp = temp.rstrip('1')
        l = '1'
        r = '2'
        while temp:
            temp = temp.lstrip(l)
            temp = temp.rstrip(r)
            result += 1
            l, r = r, l
    print(f"#{t} {result}")