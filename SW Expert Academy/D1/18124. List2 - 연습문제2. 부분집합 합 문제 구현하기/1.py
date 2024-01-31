import sys


def comb(arr, n):
    result = []
    for i in range(1<<n): # 부분 집합의 개수, 1<<n은 2**(n)과 같음
        temp = []
        for j in range(n):
            if i & (1<<j): # 여기가 문젠디?
                temp.append(arr[j])
        result.append(temp)
    return result


sys.stdin = open("input.txt")

T = int(input())
for t in range(1, T+1):
    result = 0
    lst = list(map(int, input().split()))
    for i in range(1, 11):
        for case in comb(lst, i):
            total = 0
            if not case:
                continue
            for c in case:
                total += c
            if total == 0:
                result = 1
                break
        if result:
            break
    print(f"#{t} {result}")