import sys
from collections import deque

input = sys.stdin.readline


def direction_change(current_direction, rl):
    if current_direction == 'U':
        if rl == 'L':
            current_direction = 'L'
        else:
            current_direction = 'R'
    elif current_direction == 'R':
        if rl == 'L':
            current_direction = 'U'
        else:
            current_direction = 'D'
    elif current_direction == 'D':
        if rl == 'L':
            current_direction = 'R'
        else:
            current_direction = 'L'
    elif current_direction == 'L':
        if rl == 'L':
            current_direction = 'D'
        else:
            current_direction = 'U'
    return current_direction


def move(current_direction, position):
    a, b = position
    x, y = a, b
    if current_direction == 'U':
        x -= 1
    elif current_direction == 'R':
        y += 1
    elif current_direction == 'D':
        x += 1
    elif current_direction == 'L':
        y -= 1
    return x, y


def game_over_check(a, b):
    if 1 <= a <= N and 1 <= b <= N and (a, b) not in snake_set:
        return False
    return True


N = int(input())
K = int(input())
apple_position = set(tuple(map(int, input().split())) for _ in range(K))
L = int(input())
snake_direction_change = deque([input().split() for _ in range(L)])

snake = deque([(1, 1)])
snake_set = set()
snake_set.add((1, 1))
snake_direction = 'R'

t = 1
while True:
    a, b = move(snake_direction, snake[0])
    if game_over_check(a, b):
        # print(f'{t}초에 game over')
        print(t)
        break
    snake.appendleft((a, b))
    snake_set.add((a, b))

    if (a, b) in apple_position:
        # print('사과 냠냠')
        apple_position.remove((a, b))
    else:
        snake_set.remove(snake.pop())

    if snake_direction_change:    
        if t == int(snake_direction_change[0][0]):
            # print(f'{t}초 방향 전환')
            snake_direction = direction_change(snake_direction, snake_direction_change[0][1])
            snake_direction_change.popleft()
    t += 1
    
    
'''
뱀의 시작 위치는 0, 0, 시작 방향은 오른쪽
시작 위치에는 사과가 없다
'''