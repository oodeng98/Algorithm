import sys


input = sys.stdin.readline


def binary_search():
    rank = lst[i]
    start = i
    end = len(lst)
    result = -1
    while start < end:
        middle = (start + end) // 2
        if lst[middle] < rank + K:
            start = middle + 1
            result = middle
        elif rank + K < lst[middle]:
            end = middle - 1
        else:
            result = middle
            break
    if result == -1:
        return 0
    return result - i


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
    lst = sorted(students[length])
    for i in range(len(lst)):
        pair += binary_search()
        
print(pair)