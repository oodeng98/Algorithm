import sys


input = sys.stdin.readline
num = int(input())
total_data = []
for i in range(num):
    total_data.append(tuple(map(int, input().split())))
total_data.sort(key=lambda x: (x[0], x[1]))
finish = (-1, 0)
count = 0
for i in range(num):
    if total_data[i][0] >= finish[1]:
        if finish[1] == total_data[i][0] and finish[1] == total_data[i][1]:
            count += 1
            continue
        finish = total_data[i]
        count += 1
    else:
        if total_data[i][0] > finish[0]:
            if total_data[i][1] < finish[1]:
                finish = total_data[i]
        # total_data[i][1] 가짜 min값으로 가져간다 v
        # total_data[i][1] 이랑 계속 비교를 했는데
        # 만에 하나 min값이 갱신되어도 -> 시작 시간이 느린데 끝나는 시간이 더 빠른 그런 회의가 있다 를 의미하고
        # total_data[i][0]이 가짜 min값보다 커졌어, 근데 가짜 min값이 그대로야 -> 진짜 min
print(count)