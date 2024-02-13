import sys

sys.stdin = open('input.txt')
for t in range(1, int(input()) + 1):
    result = 0
    count = 0
    batch = input()
    i = 0
    length = len(batch)
    while i < length:
        if batch[i] == '(':
            if batch[i+1] == ')':
                result += count
                i += 2
                continue
            else:
                count += 1
        else:
            count -= 1
            result += 1
        i += 1
    print(f"#{t} {result}")
