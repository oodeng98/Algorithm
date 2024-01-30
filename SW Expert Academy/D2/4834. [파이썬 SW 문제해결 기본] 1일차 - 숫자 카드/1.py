import sys

sys.stdin = open("4834_input.txt")

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))
    dic = {}
    for i in arr:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    max_value = 0
    max_count = 0
    for i in dic:
        if max_count <= dic[i]:
            if max_count == dic[i]:
                if i < max_value:
                    continue
            max_value = i
            max_count = dic[i]
    print(f"#{t} {max_value} {max_count}")