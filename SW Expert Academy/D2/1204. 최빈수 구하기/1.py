T = int(input())
for t in range(T):
    n = int(input())
    lst = [0 for i in range(101)]
    score = map(int, input().split())
    for i in score:
        lst[i] += 1
    print(f"#{n} {lst.index(max(lst))}")