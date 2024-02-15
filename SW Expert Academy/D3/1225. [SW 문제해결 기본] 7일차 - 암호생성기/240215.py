import sys

sys.stdin = open('input.txt')

def check():
    index = 0
    while True:
        for i in range(1, 6):
            lst[index] -= i
            if lst[index] <= 0:
                lst[index] = 0
                return index + 1
            index = (index + 1) % 8

try:
    while True:
        t = input().strip()
        lst = list(map(int, input().split()))
        temp = lst[0]
        for i in range(8):
            lst[i] -= (temp // 15 - 1) * 15
        index = check()
        print(f"#{t}", end=' ')
        for i in range(8):
            print(lst[(index + i) % 8], end=' ')
        print()
except Exception as e:
    pass
