n = int(input())
lst = [0] + list(map(int, input().split()))
up = [0 for x in range(n + 1)]
for i in range(1, n + 1):
    temp = 0
    for j in range(i):
        if lst[j] < lst[i]:
            temp = max(temp, up[j])
    up[i] = temp + 1

down = [0 for x in range(n + 1)]
lst = [0] + lst[::-1][:-1]
for i in range(1, n + 1):
    temp = 0
    for j in range(i):
        if lst[j] < lst[i]:
            temp = max(temp, down[j])
    down[i] = temp + 1

ret = 0
for i in range(1, n + 1):
    ret = max(ret, up[i] + down[i])
print(ret)
