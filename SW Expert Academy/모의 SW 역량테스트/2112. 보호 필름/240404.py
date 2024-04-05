# import sys
from itertools import combinations
 
def check(arr_copy):
    for j in range(W):
        count = 1
        for i in range(1, D):
            if arr_copy[i][j] == arr_copy[i-1][j]:
                count += 1
                if K <= count:
                    break
            else:
                count = 1
        else:
            if K <= count:
                break
            return False
    return True
 
 
def insert():
    for n in range(1, K):  # 변경할 필름의 개수
        for comb in combinations(candidate, n):  # 개수만큼 필름 선택
            for case in range(2**n):
                seq = bin(case)[2:].zfill(n)  # 0->A, 1->B
                arr_copy = [i for i in arr]
                for i in range(n):
                    arr_copy[comb[i]] = seq[i] * W
                if check(arr_copy):
                    return n
    else:
        return K
 
 
# sys.stdin = open('input.txt')
T = int(input())
for t in range(1, T+1):
    D, W, K = map(int, input().split())
    arr = [input().split() for _ in range(D)]
    if check(arr):
        print(f"#{t} {0}")
        continue
    candidate = [i for i in range(D)]
    print(f"#{t} {insert()}")