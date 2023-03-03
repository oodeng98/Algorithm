n, k = map(int, input().split())

candidate = [n]
check = 0
turn = 0
while True:
    next_candidate = []
    for can in candidate:
        if can == k:
            check = 1
            break
        next_candidate.append(can + 1)
        next_candidate.append(can - 1)
        next_candidate.append(can * 2)
    if check:
        break
    turn += 1
    candidate = next_candidate

result = 0
for i in candidate:
    if i == k:
        result += 1
print(turn)
print(result)