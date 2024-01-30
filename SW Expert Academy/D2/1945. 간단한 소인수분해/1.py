import sys

sys.stdin = open("input.txt")

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [0, 0, 0, 0, 0]
    for index, x in enumerate([2, 3, 5, 7, 11]):
        while N % x == 0:
            N //= x
            arr[index] += 1
    print(f"#{t} {arr[0]} {arr[1]} {arr[2]} {arr[3]} {arr[4]}")