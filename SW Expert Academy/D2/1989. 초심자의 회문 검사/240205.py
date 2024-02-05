import sys


sys.stdin = open('input.txt')
T = int(input())
for t in range(1, T+1):
    str1 = input()
    length = len(str1)
    check = 1
    for i in range(length // 2):
        if str1[i] != str1[length-1-i]:
            check = 0
            break
    if check:
        print(f"#{t} 1")
    else:
        print(f"#{t} 0")