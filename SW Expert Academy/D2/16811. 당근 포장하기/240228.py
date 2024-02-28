import sys

sys.stdin = open('input.txt')


T = int(input())
for t in range(1, T+1):
    N = int(input())
    carrots = {}
    for carrot in map(int, input().split()):
        if carrot in carrots:
            carrots[carrot] += 1
        else:
            carrots[carrot] = 1
    carrots = [i[1] for i in sorted(list(carrots.items()))]
    length = len(carrots)
    result = float('inf')
    for i in range(1, length):
        for j in range(i+1, length):
            a, b, c = sum(carrots[:i]), sum(carrots[i:j]), sum(carrots[j:])
            if N // 2 < a or N // 2 < b or N // 2 < c:
                continue
            result = min(result, max(a, b, c) - min(a, b, c))
    if result == float('inf'):
        result = -1
    print(f"#{t} {result}")