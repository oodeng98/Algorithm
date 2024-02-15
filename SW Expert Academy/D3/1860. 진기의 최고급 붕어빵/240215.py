import sys

sys.stdin = open('input.txt')


def countSort():
    temp_lst = [0 for _ in range(11111+1)]
    result_lst = [0 for _ in range(N)]

    for i in lst:
        temp_lst[i] += 1
    for i in range(11111):
        temp_lst[i+1] += temp_lst[i]
    for i in lst:
        temp_lst[i] -= 1
        result_lst[temp_lst[i]] = i
    return result_lst

T = int(input())
for t in range(1, T+1):
    N, M, K = map(int, input().split())
    lst = list(map(int, input().split()))
    lst = countSort()
    for index, i in enumerate(lst):
        if ((i) // M) * K < index + 1:
            break
    else:
        print(f"#{t} Possible")
        continue
    print(f"#{t} Impossible")
