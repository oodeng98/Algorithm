inp = input().split()
num, k = int(inp[0]), int(inp[1])
lst = [x for x in range(1, num+1)]
result = []
while len(lst) > k-1:
    result.append(lst.pop(k-1))
    lst = lst[k-1:] + lst[:k-1]

result = result + lst
for i in range(len(result)):
    if i == 0:
        print('<', end='')
    print(result[i], end='')
    if i != len(result) - 1:
        print(', ', end='')
    else:
        print('>', end='')