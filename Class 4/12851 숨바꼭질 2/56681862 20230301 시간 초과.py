n, k = map(int, input().split())

candidate = {n: 1}
check = 0
turn = 0
while True:
    next_candidate = {}
    for can in candidate:
        if can == k:
            check = 1
            break
        for i in [can + 1, can - 1, can * 2]:
            if i in next_candidate:
                next_candidate[i] += 1
            else:
                next_candidate[i] = 1
    if check:
        break
    turn += 1
    candidate = next_candidate

print(turn)
print(candidate[k])