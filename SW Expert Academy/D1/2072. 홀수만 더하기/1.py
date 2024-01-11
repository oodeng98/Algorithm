T = int(input())
for i in range(1, T + 1):
    lst = map(int, input().split())
    total = 0
    for j in lst:
        if j % 2:
            total += j
    print(f"#{i} {total}")