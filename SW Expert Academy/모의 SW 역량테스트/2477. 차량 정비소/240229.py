import sys

sys.stdin = open('input.txt')


T = int(input())
for t in range(1, T+1):
    N, M, K, A, B = map(int, input().split())
    reception_time = list(map(int, input().split()))
    repair_time = list(map(int, input().split()))
    clients = map(int, input().split())
    
    reception_list = [[] for _ in range(N)]  # 손님 이름 저장용
    reception = [0 for _ in range(N)]  # 접수가 끝나는 시간 저장
    repair_clients = []  # 손님 번호, 정비 시작 시간, 접수 창구 번호

    for index, client in enumerate(clients):
        min_value = float('inf')
        reception_num = -1
        for i in range(N):
            if reception[i] <= client:
                reception[i] = client + reception_time[i]
                reception_num = i
                break
            if reception[i] < min_value:
                min_value = reception[i]
                reception_num = i
        else:   
            reception[reception_num] += reception_time[reception_num]
        reception_list[reception_num].append(index+1)
        repair_clients.append((index+1, reception[reception_num], reception_num))

    repair_clients.sort(key=lambda x: (x[1], x[2]))
    repair_list = [[] for _ in range(N)]  # 손님 이름 저장용
    repair = [0 for _ in range(N)]  # 정비가 끝나는 시간 저장

    for index, client, _ in repair_clients:
        min_value = float('inf')
        repair_num = -1
        for i in range(M):
            if repair[i] <= client:
                repair[i] = client + repair_time[i]
                repair_num = i
                break
            if repair[i] < min_value:
                min_value = repair[i]
                repair_num = i
        else:    
            repair[repair_num] += repair_time[repair_num]
        repair_list[repair_num].append(index)

    result = sum(set(reception_list[A-1]) & set(repair_list[B-1]))
    if not result:
        result = -1 
    print(f"#{t} {result}")