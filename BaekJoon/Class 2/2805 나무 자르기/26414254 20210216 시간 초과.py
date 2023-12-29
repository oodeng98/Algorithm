inp = input().split()
num, target = int(inp[0]), int(inp[1])
data = list(map(int, input().split()))

start = 0
finish = max(data)
while start <= finish:
    temp = 0
    middle = (start + finish) // 2
    for i in data:
        temp += max(i - middle, 0)
        if temp > target:
            break
    if temp == target:
        break
    elif temp > target:
        start = middle + 1
    else:
        finish = middle - 1
if temp < target:
    print(middle - 1)
else:
    print(middle)