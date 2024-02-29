import sys

sys.stdin = open('input.txt')


T = int(input())
for t in range(1, T+1):
    N, M, K, A, B = map(int, input().split())
    reception_time = list(map(int, input().split()))
    repair_time = list(map(int, input().split()))
    clients = list(map(int, input().split()))
    
    reception_list = [[] for _ in range(N)]  # 손님 이름 저장용
    reception = [0 for _ in range(N)]  # 접수가 끝나는 시간 저장
    repair_clients = []  # 손님 번호, 정비 시작 시간, 접수 창구 번호

    for index, client in enumerate(clients):
        check = 0
        for i in range(N):
            if reception[i] <= client:
                reception[i] = client + reception_time[i]
                reception_list[i].append(index+1)
                repair_clients.append((index+1, reception[i], i))
                check = 1
                break
        if check:
            continue
        min_value = float('inf')
        min_index = -1
        for i in range(N):
            if reception[i] < min_value:
                min_value = reception[i]
                min_index = i
        reception[min_index] += reception_time[min_index]
        reception_list[min_index].append(index+1)
        repair_clients.append((index+1, reception[min_index], min_index))

    repair_clients.sort(key=lambda x: (x[1], x[2]))
    repair_list = [[] for _ in range(N)]  # 손님 이름 저장용
    repair = [0 for _ in range(N)]  # 접수가 끝나는 시간 저장

    for index, client, _ in repair_clients:
        check = 0
        for i in range(M):
            if repair[i] <= client:
                repair[i] = client + repair_time[i]
                repair_list[i].append(index)
                check = 1
                break
        if check:
            continue
        min_value = float('inf')
        min_index = -1
        for i in range(M):
            if repair[i] < min_value:
                min_value = repair[i]
                min_index = i
        repair[min_index] += repair_time[min_index]
        repair_list[min_index].append(index)

    result = sum(set(reception_list[A-1]) & set(repair_list[B-1]))
    if not result:
        result = -1 
    print(f"#{t} {result}")