import sys
from math import gcd


def inverse(low):
    seq = str(bin(1000000005))[2:]
    ret = 1
    index = len(seq) - 1
    temp = low
    while index >= 0:
        if seq[index] == '1':
            ret *= temp
            ret = ret % 1000000007
        temp *= temp
        temp = temp % 1000000007
        index -= 1
    return ret


input = sys.stdin.readline
m = int(input())
result = 0
for _ in range(m):
    n, s = map(int, input().split())
    biggest = gcd(n, s)
    n = n // biggest
    s = s // biggest
    q = s * inverse(n) % 1000000007
    result = (result + q) % 1000000007
print(result)
