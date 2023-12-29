start = 0
finish = max(data)
check = 0
k = 0
while start <= finish and k < 35:
    temp = 0
    middle = (start + finish) // 2
    for i in data:
        temp += max(i - middle, 0)
        if temp > target:
            break
    if temp == target:
        print(middle)
        check = 1
        break
    elif temp > target:
        start = middle + 1
    else:
        finish = middle - 1
    k += 1
if start > finish and check == 0:
    print(middle - 1)