import sys

sys.stdin = open('input.txt')


def perm(n):
    if n == N-1:
        a = nums[0]
        for index, o in enumerate(lst):
            b = nums[index+1]
            a = calculate(a, b, o)
        min_max[0] = min(min_max[0], a)
        min_max[1] = max(min_max[1], a)
    else:
        for i in range(4):
            if operators[i]:
                lst[n] = operator[i]
                operators[i] -= 1
                perm(n+1)
                lst[n] = ''
                operators[i] += 1
            

def calculate(a, b, oper):
    if oper == '+':
        return a + b
    if oper == '-':
        return a - b
    if oper == '*':
        return a * b
    if oper == '/':
        return int(a / b)


operator = ['+', '-', '*', '/']
T = int(input())
for t in range(1, T+1):
    N = int(input())
    operators = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    lst = ['' for _ in range(N-1)]
    min_max = [float('inf'), -float('inf')]
    perm(0)
    print(f"#{t} {min_max[1] - min_max[0]}")