import sys


def four_square(n):
    c = 1
    check = 0
    temp = [n]
    while True:
        temp_temp = temp
        temp = []
        for i in temp_temp:
            for j in one:
                if j < i:
                    temp.append(i - j)
        for i in temp:
            if i in one:
                check = 1
                break
        c += 1
        if check == 1:
            break
    return c


input = sys.stdin.readline
num = int(input())
one = [x ** 2 for x in range(223, 0, -1)]
if num in one:
    print(1)
else:
    print(four_square(num))