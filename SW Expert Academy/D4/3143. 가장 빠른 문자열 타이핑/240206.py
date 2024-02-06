import sys

sys.stdin = open('input.txt')
for t in range(1, int(input())+1):
    s1, s2 = input().split()
    count = -1
    for i in s1.split(s2):
        count += len(i) + 1
    print(f"#{t} {count}")