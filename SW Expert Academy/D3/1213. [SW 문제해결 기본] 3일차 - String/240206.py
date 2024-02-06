import sys

sys.stdin = open('input.txt', encoding='UTF8')
for _ in range(10):
    t = int(input())
    str1 = input()
    str2 = input()
    print(f'#{t} {len(str2.split(str1)) - 1}')