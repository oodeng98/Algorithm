import sys

sys.stdin = open("input.txt")

T = int(input())
for t in range(1, T+1):
    N = int(input())
    dic = {i: 0 for i in map(int, input().split())}
    result = []
    for i in range(5):
        min_value = float('inf')
        max_value = 0
        for j in dic:
            if j < min_value:
                min_value = j
            if max_value < j:
                max_value = j
        del dic[max_value]
        del dic[min_value]
        result.append(max_value)
        result.append(min_value)
    print(f"#{t} " + ' '.join(map(str, result)))