import sys

input = sys.stdin.readline
target = str(input().rstrip())
bomb = str(input().rstrip())
length = len(bomb)
while True:
    temp = target.find(bomb)
    if temp == -1:
        break
    target = target[:temp] + target[temp + length:]
if not target:
    print("FRULA")
else:
    print(target)