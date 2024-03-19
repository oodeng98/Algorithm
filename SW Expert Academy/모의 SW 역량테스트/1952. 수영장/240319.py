import sys


sys.stdin = open('input.txt')
T = int(input())
for t in range(1, T+1):
    day, month, month3, year = map(int, input().split())
    lst = list(map(int, input().split()))
    cost = [float('inf') for _ in range(12)]
    cost[0] = min(lst[0] * day, month)
    cost[2] = month3
    cost[11] = year
    
    for i in range(11):
        cost[i+1] = min(cost[i+1], cost[i] + min(lst[i+1] * day, month))
        cost[min(i+3, 11)] = min(cost[min(i+3, 11)], cost[i] + month3)
    print(f"#{t} {cost[-1]}")