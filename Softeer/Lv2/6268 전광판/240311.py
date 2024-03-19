import sys


def compare(a, b):
    if a == b:
        return 0
    result = 0
    for i in range(7):
        if number[a][i] != number[b][i]:
            result += 1
    return result


number = {'0': [1, 1, 1, 1, 1, 1, 0], '1': [0, 1, 1, 0, 0, 0, 0], '2': [1, 1, 0, 1, 1, 0, 1], '3': [1, 1, 1, 1, 0, 0, 1], '4': [0, 1, 1, 0, 0, 1, 1], 
'5': [1, 0, 1, 1, 0, 1, 1], '6': [1, 0, 1, 1, 1, 1, 1], '7': [1, 1, 1, 0, 0, 1, 0], '8': [1, 1, 1, 1, 1, 1, 1], '9': [1, 1, 1, 1, 0, 1, 1]}
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    a, b = input().split()
    len_a = len(a)
    len_b = len(b)
    if len_a < len_b:
        max_len, min_len = len_b, len_a
        long = b
    else:
        max_len, min_len = len_a, len_b
        long = a
    result = 0
    for i in range(1, min_len+1):
        result += compare(a[-i], b[-i])
    for i in range(min_len+1, max_len+1):
        for j in range(7):
            result += number[long[-i]][j]
    print(result)