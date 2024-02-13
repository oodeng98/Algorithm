import sys

sys.stdin = open('input.txt')

lst = [i for i in range(1, 11)]
n = len(lst)
count = 0
for i in range(2 ** n):
    total = 0
    for j in range(n):
        if i & (1 << j):
            total += lst[j]
            if 10 < total:
                break
    if total == 10:
        count += 1
print(f"#{1} {count}")