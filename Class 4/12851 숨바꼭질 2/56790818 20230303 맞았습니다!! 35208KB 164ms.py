n, k = map(int, input().split())
if n == k:
    print(0)
    print(1)
else:
    checklist = [0 for _ in range(100001)]
    checklist[n] = 1
    candidate = [n]
    check = 0
    turn = 0
    while True:
        next_candidate = {}
        for can in candidate:
            for i in [can + 1, can - 1, can * 2]:
                if 0 <= i <= 100000:
                    if not checklist[i]:
                        if i == k:
                            check = 1
                        if i in next_candidate:
                            next_candidate[i] += checklist[can]
                        else:
                            next_candidate[i] = checklist[can]
        for i in next_candidate:
            checklist[i] = next_candidate[i]
        turn += 1
        if check:
            print(turn)
            print(checklist[k])
            break
        candidate = list(next_candidate.keys())
