n, k = map(int, input().split())

checklist = [0 for _ in range(100001)]
candidate = [n]
check = 0
turn = 0
while True:
    next_candidate = []
    for can in candidate:
        if can == k:
            check = 1
            break
        for i in [can + 1, can - 1, can * 2]:
            if not checklist[i]:
                next_candidate.append(i)
            checklist[i] += 1
    if check:
        print(turn)
        print(checklist[k])
        break
    turn += 1
    candidate = next_candidate
