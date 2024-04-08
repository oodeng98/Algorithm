import sys


def binary_search(target):
    start = 0
    end = length - 1
    while start <= end:
        middle = (start + end) // 2
        if bags[middle] == target:
            return middle
        elif bags[middle] < target:
            start = middle + 1
        else:  # target < bags[middle]
            end = middle - 1
    return start


input = sys.stdin.readline
N, K = map(int, input().split())
jewels = [tuple(map(int, input().split())) for _ in range(N)]  # weight, value
bags_set = set()
bags_dic = {}
for _ in range(K):
    bag = int(input())
    bags_set.add(bag)
    if bag in bags_dic:
        bags_dic[bag] += 1
    else:
        bags_dic[bag] = 1

jewels.sort(key=lambda x: x[1], reverse=True)
bags = sorted(list(bags_set))
length = len(bags)

result = 0
for weight, value in jewels:
    index = binary_search(weight)
    if index == length:
        continue
    check = 0
    while bags_dic[bags[index]] == 0:
        index += 1
        if index == length:
            check = 1
            break
    if check:
        continue
    bags_dic[bags[index]] -= 1
    result += value
print(result)
'''
생각 과정

bags를 오름차순으로 정렬하고, jewels를 가격 및 무게로 정렬하고 넣을 수 있다면 넣는게 맞지않나?
보석을 넣을 수 있는 가방 중 가장 작은 가방에 보석을 계속 집어넣자
만약 넣을 수 없다면 그냥 패스해야지 뭐
'''