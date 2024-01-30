import sys
from itertools import combinations

input = sys.stdin.readline
lst = []
for i in range(9):
    lst.append(int(input()))
for comb in combinations(lst, 7):
    if sum(comb) == 100:
        temp = list(comb)
        temp.sort()
        for i in temp:
            print(i)
        break
