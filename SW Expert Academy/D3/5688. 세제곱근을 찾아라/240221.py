import sys

sys.stdin = open('input.txt')


def cube_root(n):
    i = 2
    result = 1
    while i ** 3 <= n:
        if n % i ** 3 == 0:
            n //= i ** 3
            result *= i
            continue
        i += 1
    if n == 1:
        return result
    return -1
    


T = int(input())
for t in range(1, T+1):
    N = int(input())
    if N == 1:
        print(f"#{t} {1}")
        continue
    
    print(f"#{t} {cube_root(N)}")