n = int(input())
lst = list(map(int, input().split()))
lst.sort()
print(lst[n // 2])