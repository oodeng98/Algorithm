n = int(input())
if n == 1:
    print(0)
    print(1)
else:
    lst = [0 for _ in range(1000001)]
    numbers = [n]
    check = 0
    while True:
        next_numbers = []
        for i in numbers:
            if i % 3 == 0:
                if not lst[i // 3]:
                    lst[i // 3] = i
                    next_numbers.append(i // 3)
            if i % 2 == 0:
                if not lst[i // 2]:
                    lst[i // 2] = i
                    next_numbers.append(i // 2)
            if not lst[i - 1]:
                lst[i - 1] = i
                next_numbers.append(i - 1)
            if lst[1]:
                check = 1
                break
        if check:
            break
        numbers = next_numbers
    path = [1]
    while lst[path[-1]] != n:
        path.append(lst[path[-1]])
    path.append(lst[path[-1]])
    print(len(path) - 1)
    for i in path[::-1]:
        print(i, end=' ')
