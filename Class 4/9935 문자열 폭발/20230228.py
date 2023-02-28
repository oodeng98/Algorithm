import sys


def read_str(idx):


input = sys.stdin.readline
target = str(input().rstrip())
bomb = str(input().rstrip())
length = len(bomb)
checkpoints = []
for index, i in enumerate(target):
    if i == bomb[0]:
        checkpoints.append(index)

index = 0
check = {}
bomb_area = {}
while index <= len(checkpoints):
    if index in check:
        index += 1
    checkpoint = checkpoints[index]
    if target[checkpoint: checkpoint + length] == bomb:
        index = max(0, index - 1)
        check[index] = 0
    else:
        index += 1
    print(index)


if not target:
    print("FRULA")
else:
    print(target)