import sys

input = sys.stdin.readline
a, b, c = map(int, input().split())
for i in range(b):
    a *= a
    if a > c:
        a = a % c
print(a % c)
"""
10*10=100->4가 나머지
100*10=1000->4가 나머지
a = c + A
a*a = ac+Aa = ac+Ac+AA 
a*a*a = AAa->AAA
결국 나머지만 이용해서 연산하면 된다
"""