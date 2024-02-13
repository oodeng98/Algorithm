import sys

sys.stdin = open('input.txt')

for t in range(1, 11):
    N = int(input())
    stack = []
    result = ''
    operator = ''
    for i in input().strip():
        if i.isdecimal():
            result += i
            continue
        if operator:
            result += i
        else:
            operator = i
    result += operator
    ret = 0
    for i in result[::-1]:
        if i.isdecimal():
            ret += int(i)
    print(f"#{t} {ret}")