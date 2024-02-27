T = int(input())
for t in range(T):
    n = int(input())
    lst = [0 for i in range(101)]
    score = list(map(int, input().split()))
    for i in score:
        lst[i] += 1
    answer = 0
    for index, i in enumerate(lst):
        if i == max(lst):
            answer = index
    print(f"#{n} {answer}")