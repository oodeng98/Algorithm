N = int(input().strip())

lst = []
dic = {}
for i in map(int, input().split()):
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
    lst.append(i)
lst.sort()

count = 0
i = 0
while i < N:
    start = 0
    end = N - 1
    if start == i:
        start += 1
    if end == i:
        end -= 1
    while start < end:
        if lst[end] * 2 < lst[i]:
            break
        if lst[start] + lst[end] < lst[i]:  # 합이 작으면
            start += 1
        elif lst[i] < lst[start] + lst[end]:  # 합이 크면
            end -= 1
        else: # 값이 같으면
            count += dic[lst[i]]
            # print(count, lst[i])
            break
        if start == i:
            start += 1
        if end == i:
            end -= 1
    i += dic[lst[i]]
print(count)