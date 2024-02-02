import sys


sys.stdin = open('input.txt')
T = int(input())
for t in range(1, T+1):
    N = int(input())
    count = 1
    carrots = list(map(int, input().split()))
    max_carrot = carrots[0]
    temp_count = 1
    for i in range(1, N):
        if max_carrot < carrots[i]:
            max_carrot = carrots[i]
            temp_count += 1
        else:
            if count < temp_count:
                count = temp_count
            temp_count = 1
            max_carrot = carrots[i]
    if count < temp_count:
        count = temp_count
    print(f"#{t} {count}")