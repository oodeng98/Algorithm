import sys

sys.stdin = open('s_input.txt')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(tuple(map(int, input().split())))

    P = int(input())
    lst = []
    for _ in range(P):
        lst.append(int(input()))
    dic = {x:0 for x in lst}
    for i in arr:
        for j in range(i[0], i[1]+1):
            if j in dic:
                dic[j] += 1
    result = f"#{t}"
    for i in lst:
        result = result + " " + str(dic[i])
    print(result)
    