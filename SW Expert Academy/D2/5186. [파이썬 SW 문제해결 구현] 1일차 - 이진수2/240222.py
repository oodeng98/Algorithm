import sys

sys.stdin = open('input.txt')


def convert(n):
    result = ''
    count = 1
    while count <= 12:
        n *= 2
        if 1 <= n:
            result += '1'
            n -= 1
            if n == 0:
                break
        else:
            result += '0'
        count += 1
    else:
        return 'overflow'
    return result


T = int(input())
for t in range(1, T+1):
    N = float(input())
    print(f"#{t} {convert(N)}")
    