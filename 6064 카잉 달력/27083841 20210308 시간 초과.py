import sys


input = sys.stdin.readline
num = int(input())

for i in range(num):
    m, n, x, y = map(int, input().split())
    if abs(x - y) % 2 == 1 and n % 2 == 0:
        # 분자가 계속 홀수다 => 분모가 홀수만 가능하다
        # 계속 홀수인 경우-> y-x가 홀수인 경우+n이 짝수인 경우
        print(-1)
        continue
    elif m == n and x != y:
        print(-1)
        continue
    result = y - x
    while result % m != 0:
        result += n
    print(result + x)
