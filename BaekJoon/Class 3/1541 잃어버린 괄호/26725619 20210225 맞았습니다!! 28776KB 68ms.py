import sys


input = sys.stdin.readline
expression = input().rstrip().split('-')
for i in range(len(expression)):
    expression[i] = list(map(int, expression[i].split('+')))
result = 0
for i in expression[0]:
    result += i

for i in range(1, len(expression)):
    for j in expression[i]:
        result -= j

print(result)