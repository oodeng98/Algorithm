import sys

input = sys.stdin.readline

N = int(input())
for _ in range(N):
    a, *lst_a = map(int, input().split())
    b, *lst_b = map(int, input().split())
    dic_a = {i: 0 for i in range(1, 5)}
    for i in lst_a:
        dic_a[i] += 1
    dic_b = {i: 0 for i in range(1, 5)}
    for i in lst_b:
        dic_b[i] += 1

    check = 0
    for i in [4, 3, 2, 1]:
        if dic_a[i] > dic_b[i]:
            print("A")
            check = 1
            break
        elif dic_a[i] < dic_b[i]:
            print("B")
            check = 1
            break
    if check == 0:
        print("D")
