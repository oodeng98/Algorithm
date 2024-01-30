import sys

input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

result = []
for index, i in enumerate(lst):
    result.insert(-i, index + 1)
print(' '.join(map(str, result)))
