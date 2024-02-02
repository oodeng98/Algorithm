import sys


input = sys.stdin.readline

K = int(input())
dic = {}
lst = []
hor_max = 0
hor_index = -1
ver_max = 0
ver_index = -1
for i in range(6):
    dir, length = map(int, input().split())
    if dir in [1, 2]:
        if hor_max < length:
            hor_index = i
            hor_max = length
    else:
        if ver_max < length:
            ver_index = i
            ver_max = length
    lst.append(length)

result = K * (hor_max * ver_max)
if (hor_index - 1 + 6) % 6 == ver_index: # ver, hor 순서면
    result -= K * (hor_max - lst[ver_index-1]) * (ver_max - lst[(hor_index+1)%6])
else: # hor, ver 순서
    result -= K * (ver_max - lst[hor_index-1]) * (hor_max - lst[(ver_index+1)%6])

print(result)
'''
7
2 160
3 30
1 60
3 20
1 100
4 50
'''