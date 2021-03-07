inp = input().split()
num, k = int(inp[0]), int(inp[1])
lst = [x for x in range(1, num+1)]
result = []
while len(lst) > k-1:
    result.append(lst.pop(k-1))
    lst = lst[k-1:] + lst[:k-1]

while len(lst) != 0:
    temp = k % len(lst) - 1
    if temp < 0:
        temp += len(lst)
    result.append(lst.pop(temp))
    lst = lst[temp:] + lst[:temp]
# 0번째 나가고 자르고 1번째 나가고 자르고 2번째 나가고 자르고 이런식으로
for i in range(len(result)):
    if i == 0:
        print('<', end='')
    print(result[i], end='')
    if i != len(result) - 1:
        print(', ', end='')
    else:
        print('>', end='')