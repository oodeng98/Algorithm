import sys

input = sys.stdin.readline
n, m = map(int, input().split())
ladder_snake = {}
snake_ladder = {}
for i in range(n + m):
    key, value = map(int, input().split())
    ladder_snake[key] = value
    snake_ladder[value] = key
climb_from_start = set(ladder_snake.keys())
climb_from_end = set(ladder_snake.values())
start = {1}
end = {100}
count = 1
while True:
    from_start = set()
    for i in start:
        for j in range(1, 7):
            from_start.add(i + j)
    common = from_start & climb_from_start
    candidate_from_start = from_start - common
    if common:
        for i in common:
            candidate_from_start.add(ladder_snake[i])
    if candidate_from_start & end:
        break
    count += 1

    from_end = set()
    for i in end:
        for j in range(1, 7):
            from_end.add(i - j)
    common = from_end & climb_from_end
    candidate_from_end = from_end - common
    if common:
        for i in common:
            candidate_from_end.add(snake_ladder[i])
    if candidate_from_end & start:
        break
    count += 1

    start = candidate_from_start
    end = candidate_from_end
print(count)
