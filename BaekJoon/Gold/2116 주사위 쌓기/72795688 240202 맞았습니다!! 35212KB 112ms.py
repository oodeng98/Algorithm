import sys

input = sys.stdin.readline

N = int(input())
dices = []
face = {0: 5, 5: 0, 1: 3, 3: 1, 2: 4, 4: 2}
dice_lst = []
for _ in range(N):
    temp_dic = {}
    temp_lst = []
    for index, i in enumerate(map(int, input().split())):
        temp_dic[i] = index
        temp_lst.append(i)
    dices.append(temp_dic)
    dice_lst.append(temp_lst)

result = 0
for i in range(1, 7):
    start = i
    next_start = -1
    temp_result = 0
    for lst, dice in zip(dice_lst, dices):
        max_value = 0
        next_start = lst[face[dice[start]]]
        for j in range(6, 0, -1):
            if j in [start, next_start]:
                continue
            max_value = j
            break
        temp_result += max_value
        start = next_start
    result = max(result, temp_result)
print(result)
