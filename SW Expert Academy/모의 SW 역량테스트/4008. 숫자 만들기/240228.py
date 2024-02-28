import sys

sys.stdin = open('input.txt')


def perm(n):
    if n == N-1:
        permutations.append(lst.copy())
    else:
        for i in range(4):
            if 0 < operators[i]:
                lst.append(operator[i])
                operators[i] -= 1
                perm(n+1)
                lst.pop()
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
    lst = []
    permutations = []
    perm(0)
    min_value = float('inf')
    max_value = -float('inf')
    for i in permutations:
        a = nums[0]
        for index, o in enumerate(i):
            b = nums[index+1]
            a = calculate(a, b, o)
        min_value = min(min_value, a)
        max_value = max(max_value, a)
    print(f"#{t} {max_value - min_value}")