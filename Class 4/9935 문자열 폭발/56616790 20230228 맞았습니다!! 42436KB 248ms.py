target = input()
bomb = list(input())

length = len(bomb)
stack = []
last_bomb = bomb[-1]
for i in target:
    stack.append(i)
    if i == last_bomb and stack[-length:] == bomb:
        del stack[-length:]

print("FRULA" if not stack else ''.join(stack))
