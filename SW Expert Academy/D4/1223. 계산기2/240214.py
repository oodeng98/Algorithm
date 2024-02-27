import sys

sys.stdin = open('input.txt')


for t in range(1, 11):
    N = int(input())
    lst = input()
    num_stack = []
    operator_stack = []
    prior = {'+': 1, '*': 2}
    for i in lst:
        if i.isdecimal():
            num_stack.append(int(i))
            continue
        if operator_stack and prior[i] < prior[operator_stack[-1]]:
            num_stack.extend(operator_stack[::-1])
            operator_stack = [i]
        else:
            operator_stack.append(i)
    num_stack.extend(operator_stack[::-1])
    
    num = []
    operator = []
    for i in num_stack:
        if type(i) == int:
            num.append(i)
            continue
        b = num.pop()
        a = num.pop()
        if i == '+':
            num.append(a + b)
        else:
            num.append(a * b)
    print(f"#{t} {num[0]}")
