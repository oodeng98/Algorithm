num = int(input())
for i in range(num):
    data = input()
    # print(data)
    stack = 0
    check = 0
    for j in range(len(data)-1):
        if data[j] == '(':
            stack += 1
        else:
            stack -= 1
            if stack < 0:
                check = 1
                break
    if check != 1 and stack == 1 and data[-1] == ')':
        print('YES')
    else:
        print('NO')