import sys
import copy


def find_food(space, size):  # 먹을 수 있는 모든 물고기들의 위치를 표시해준다, 가는 길이 막혀있는 경우는 고려하지 않음
    food_list = []
    for i in range(len(space)):
        for j in range(len(space)):
            if 0 < space[i][j] < size[0]:
                food_list.append((i, j))
    return food_list


def find_path(space, size, present, des):  # present와 des의 거리를 return하는데, 장애물을 고려함
    new_space = copy.deepcopy(space)
    new_space[present[0]][present[1]] = 10
    temp = [present]
    count = 0
    while True:
        new_temp = []
        for i in temp:
            new_space[i[0]][i[1]] = 10
            if i[0] - 1 >= 0:  # up
                if new_space[i[0] - 1][i[1]] <= size:
                    new_temp.append((i[0] - 1, i[1]))
            if i[0] + 1 < len(space):  # down
                if space[i[0] + 1][i[1]] <= size:
                    new_temp.append((i[0] + 1, i[1]))
            if i[1] - 1 >= 0:  # left
                if space[i[0]][i[1] - 1] <= size:
                    new_temp.append((i[0], i[1] - 1))
            if i[1] + 1 < len(space):  # right
                if space[i[0]][i[1] + 1] <= size:
                    new_temp.append((i[0], i[1] + 1))
        count += 1
        if des in new_temp:
            return count
        if not new_temp:
            return 500
        temp = new_temp


input = sys.stdin.readline
n = int(input().rstrip())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))

shark_pos = 0
for i in range(n):
    for j in range(n):
        if data[i][j] == 9:
            shark_pos = (i, j)
            data[i][j] = 0

shark_size = [2, 0]
result = 0
while True:
    target = find_food(data, shark_size)
    if not target:
        break
    distance_pos = []
    for i in target:
        distance_pos.append((find_path(data, shark_size[0], shark_pos, i), i))
    if not distance_pos:
        break

    shark_size[1] += 1
    if shark_size[0] == shark_size[1]:
        shark_size[0] += 1
        shark_size[1] = 0
    distance_pos.sort(key=lambda x: (x[0], x[1][0], x[1][1]))
    result += distance_pos[0][0]
    shark_pos = distance_pos[0][1]
    data[shark_pos[0]][shark_pos[1]] = 0
print(result)
# 1, 먹을 수 있는 물고기를 찾는다
# 2, 있으면 먹으러 간다
# 3, 2를 반복하다가 안되면 엄마 상어를 찾으러 간다
