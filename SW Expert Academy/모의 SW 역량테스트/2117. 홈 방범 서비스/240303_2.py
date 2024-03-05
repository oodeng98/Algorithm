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
            distances = [abs(x - i) + abs(y - j) for x, y in city]
            count = [0 for _ in range(2 * N)]
            for d in distances:
                count[d] += 1
            for d in range(2 * N - 1):
                count[d+1] += count[d]
            for k in range(2 * N - 1, 0, -1):
                if (k - 1) ** 2 + k ** 2 <= count[k-1] * M and max_value < count[k-1]:
                    max_value = count[k-1]
    print(f"#{t} {max_value}")