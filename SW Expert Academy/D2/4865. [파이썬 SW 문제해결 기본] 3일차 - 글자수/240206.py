import sys

sys.stdin = open('input.txt')
T = int(input())
for t in range(1, T+1):
    check = {}
    for i in input():
        if i not in check:
            check[i] = 0
    
    for i in input():
        if i in check:
            check[i] += 1
    
    max_value = 0
    for i in check:
        if max_value < check[i]:
            max_value = check[i]
    print(f"#{t} {max_value}")