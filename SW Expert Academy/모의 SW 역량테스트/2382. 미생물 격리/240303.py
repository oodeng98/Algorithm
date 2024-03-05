def move(x, y, direction):
    if direction == 1:
        return x - 1, y
    if direction == 2:
        return x + 1, y
    if direction == 3:
        return x, y - 1
    if direction == 4:
        return x, y + 1
     
     
def kill(x, y, num, direction):
    if x == 0 or x == N-1 or y == 0 or y == N-1:
        return x, y, num // 2, uturn(direction)
    return x, y, num, direction
     
     
def uturn(direction):
    if direction == 1:
        return 2
    if direction == 2:
        return 1
    if direction == 3:
        return 4
    if direction == 4:
        return 3
 
 
T = int(input())
for t in range(1, T+1):
    N, M, K = map(int, input().split())
    microbes = {}
    for _ in range(K):
        x, y, n, direction = map(int, input().split())
        microbes[(x, y)] = (n, direction)
 
    for _ in range(M):
        new_microbes = {}
        checklist = {}
        for microbe in microbes:
            x, y, n, direction = *microbe, *microbes[microbe]
            x, y, n, direction = kill(*move(x, y, direction), n, direction)
            if not n:
                continue
            if (x, y) in new_microbes:
                if checklist[(x, y)][0] < n:
                    checklist[(x, y)] = (n, direction)
     
                new_microbes[(x, y)] += n
            else:
                checklist[(x, y)] = (n, direction)
                new_microbes[(x, y)] = n
        for i in checklist:
            new_microbes[i] = (new_microbes[i], checklist[i][1])
        microbes = new_microbes
 
    result = 0
    for microbe in microbes:
        result += microbes[microbe][0]
    print(f"#{t} {result}")