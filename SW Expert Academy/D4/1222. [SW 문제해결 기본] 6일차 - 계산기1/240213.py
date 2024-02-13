import sys

sys.stdin = open('input.txt')

for t in range(1, 11):
    N = int(input())
    result = 0
    for i in input().split('+'):
        result += int(i)
    print(f"#{t} {result}")