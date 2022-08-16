import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
bus = {}
for i in range(m):
    temp = list(map(int, input().split()))
    try:
        bus[temp[0]][temp[1]] = temp[2]
    except:
        bus[temp[0]] = {temp[1]: temp[2]}
start, des = (map(int, input().split()))

node_price = {}
for i in range(1, n):
    node_price[i] = 0
for i in bus[start]:
    node_price[i] = bus[start][i]
checked = [start]

while True:
    min_price = 100000
    min_node = 0
    for i in node_price:
        if i in checked:
            continue
        if node_price[i] < min_price:
            min_node = i
            min_price = node_price[i]
    if min_node == des:
        break
    checked.append(min_node)
    for i in bus[min_node]:
        node_price[i] = min(node_price[i], node_price[min_node] + bus[min_node][i])
print(node_price[des])
