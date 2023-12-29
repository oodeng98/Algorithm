T = int(input())
for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    if a == 1:
        if b == 2:
            print("B")
        else:
            print("A")
    if a == 2:
        if b == 3:
            print("B")
        else:
            print("A")
    if a == 3:
        if b == 1:
            print("B")
        else:
            print("A")
