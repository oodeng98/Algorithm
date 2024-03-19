import sys

K, P, N = map(int, input().split())
for _ in range(N):
    K *= P
    K %= 1000000007
print(K)