import sys
import itertools

input = sys.stdin.readline
n, m = map(int, input().split())
city = []
for i in range(n):
    city.append(list(map(int, input().split())))

bhc = []
house = []
for i in range(n):
    for j in range(len(city[0])):
        if city[i][j] == 2:
            bhc.append((i, j))
        elif city[i][j] == 1:
            house.append((i, j))
bhc_select = list(itertools.combinations(range(0, len(bhc)), m))
distance = []
for i in bhc_select:
    distance_temp = 0
    for j in house:
        temp = []
        for k in i:
            temp.append(abs(j[0] - bhc[k][0]) + abs(j[1] - bhc[k][1]))
        distance_temp += min(temp)
    distance.append(distance_temp)
print(min(distance))
