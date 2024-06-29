import sys

input = sys.stdin.readline


N, M = map(int, input().split())  # 입국심사대 N개, 상근이와 친구들 총 M명
table_time = [int(input()) for _ in range(N)]
fast_table = min(table_time)

start = 0
finish = fast_table * M
while start < finish:
    middle = (start + finish) // 2
    count = 0
    for table in table_time:
        count += middle // table

    if count < M:  # 처리해야 하는 인원보다 적게 처리했다면
        start = middle + 1  # 오른쪽에서 탐색
    else:  # 처리해야 하는 인원보다 많게 처리했다면
        finish = middle
print(start)
'''
https://www.acmicpc.net/problem/3079
모든 애들을 한 곳에 몰아넣고, 계속 돌리다가 남은 시간이 처음부터 처리하는 시간보다 많이 남은 경우를 빼았아오면 되는 것이 아닌가?
- 근데 제약조건 보니까 이렇게 하면 안될 것 같음
결과물은 입국심사대 중 하나의 배수와 같다
최소 시간은 0, 최대 시간은 가장 짧은 입국심사대 * M으로 두고 시작하는 것
'''