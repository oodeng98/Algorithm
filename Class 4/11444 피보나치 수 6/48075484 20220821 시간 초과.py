import sys

input = sys.stdin.readline
n = int(input())
fibo = [0, 1]
for i in range(n - 1):
    fibo.append(fibo[-1] + fibo[-2])
    del fibo[0]
print(fibo[-1] % 1000000007)