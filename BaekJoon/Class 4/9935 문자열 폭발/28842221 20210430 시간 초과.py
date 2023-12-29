import sys

input = sys.stdin.readline
target = str(input().rstrip())
bomb = str(input().rstrip())
while bomb in target:
    temp = target.split(bomb)
    target = ''.join(temp)
if not target:
    print("FRULA")
else:
    print(target)