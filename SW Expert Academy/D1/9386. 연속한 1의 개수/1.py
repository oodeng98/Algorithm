import sys

sys.stdin = open('input1.txt')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, list(input())))
    max_length = 0
    temp = 0
    for i in arr:
        if i == 1:
            temp += 1
        else:
            if max_length < temp:
                max_length = temp
            temp = 0
    if max_length < temp:
        max_length = temp
    print(f"#{t} {max_length}")
