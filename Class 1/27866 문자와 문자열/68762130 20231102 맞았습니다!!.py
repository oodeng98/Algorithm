import sys

input = sys.stdin.readline
target = input().strip()
index = int(input().strip())
print(target[index - 1])