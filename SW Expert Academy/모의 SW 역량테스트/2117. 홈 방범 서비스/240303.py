def distance(x, y, a, b):
    return abs(x - a) + abs(y - b)
 
# 운영 비용은 칸의 수
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    city = []
    for i in range(N):
        temp = input().split()
        for j in range(N):
            if temp[j] == '1':
                city.append((i, j))
     
    length = len(city)
    max_value = 1
    for i in range(N):
        for j in range(N):
            k = 1
            index = 0
            city.sort(key=lambda x: distance(x[0], x[1], i, j))
            while index < length:
                while index < length and distance(city[index][0], city[index][1], i, j) == k - 1:
                    index += 1
                if (k - 1) ** 2 + k ** 2 <= index * M:
                    max_value = max(index, max_value)
                k += 1
    print(f"#{t} {max_value}")