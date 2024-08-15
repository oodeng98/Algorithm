import sys


input = sys.stdin.readline


def binary_search(index):
    rank = lst[index]
    start = index
    end = len(lst) - 1
    result = -1
    while start <= end:
        middle = (start + end) // 2
        if lst[middle] <= rank + K:
            start = middle + 1
            result = middle
        elif rank + K < lst[middle]:
            end = middle - 1
    if result == -1:
        return 0
    return result - index


N, K = map(int, input().split())
students = {}
for i in range(1, N + 1):
    length = len(input().strip())
    if length in students:
        students[length].append(i)
    else:
        students[length] = [i]
        
pair = 0
for length in students:
    lst = students[length]
    for index in range(len(lst)):
        pair += binary_search(index)
        
print(pair)