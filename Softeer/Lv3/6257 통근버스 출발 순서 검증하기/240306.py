N = int(input())
lst = list(map(int, input().split()))
count = 0
for i in range(N-2):
    small_count = [0 for _ in range(N)]
    small_c = 0
    for j in range(N):
        if lst[j] < lst[i]:
            small_c += 1
        small_count[j] = small_c
    # print(lst[i], small_count)
    for j in range(i+1, N-1):
        if lst[i] < lst[j]:
            count += lst[i] - 1 - small_count[j]
print(count)