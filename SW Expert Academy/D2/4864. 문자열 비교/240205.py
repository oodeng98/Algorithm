import sys


sys.stdin = open('input.txt')
T = int(input())
for t in range(1, T+1):
    str1 = input().strip()
    str2 = input().strip()
    if str1 in str2:
        print(f"#{t} 1")
    else:
        print(f"#{t} 0")